from os import environ
import requests
from flask import (
    render_template, url_for, redirect,
    current_app, request, session)
from flask_login import (
    login_required, logout_user, current_user, login_user)
from flask_principal import (
    AnonymousIdentity, Identity, RoleNeed, UserNeed,
    identity_changed, identity_loaded,)
from werkzeug.urls import url_parse
from sqlalchemy import exc
from app import db, sys_admin_permission, user_permission
from . import auth_route
from .models import User


@auth_route.route('/.auth/login/aad/callback')
def auth():
    """ Callback/redirectURI for AzureAD authentication. """
    return redirect(url_for('auth_route.login'))


@auth_route.route('/login')
def login():
    """ Login route

    In Production Login Page is https://login.microsoftonline.com

    After User is authenticated by Microsoft (Azure AD) they are redirected
    here for authorisation.
    """

    # No Dev login page.
    # Mimic being redirected from MSFT.
    if environ.get('FLASK_ENV') == 'development':
        user = db.session.\
            query(
                User).\
            filter(
                User.username == 'dev.test@local.com').\
            first()
        
        login_user(user)
        
        identity_changed.send(
           current_app._get_current_object(),
           identity=Identity(user.username))
        
        next_page = request.args.get("next")

        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.home")
        
        return redirect(next_page)


    accessToken = request.headers.get('X-MS-TOKEN-AAD-ACCESS-TOKEN')

    headers = {
        'Authorization': 'Bearer {0}'.format(accessToken),
        'User-Agent': 'FlaskApp/1.0'}

    r = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers)

    user = User.query.\
        filter(
            User.username == r.json().get('userPrincipalName')).\
        first()

    # For MSFT authenticated but unauthorised Users
    if user is None:
        return 403

    login_user(user)

    identity_changed.send(
        current_app._get_current_object(),
        identity=Identity(user.username))

    return redirect(url_for("main.home"))


def do_logout():
    """ Logout user """
    logout_user()
    
    for key in ("identity.name", "identity.auth_type"):
        session.pop(key, None)
    
    identity_changed.send(
        current_app._get_current_object(), identity=AnonymousIdentity())


@auth_route.route("/logout")
@login_required
@user_permission.require(http_exception=404)
def logout():
    """ Log out the currently logged in user. """
    
    do_logout()
    
    return redirect('{0}/.auth/logout'.format(request.host_url))


@identity_loaded.connect
def on_identity_loaded(sender, identity):
    """ Handle the identity_loaded signal. 
    
    From Flask-Principal
    """
    
    # Set the identity user object
    identity.user = current_user

    # Add the UserNeed to the identity
    if hasattr(current_user, "username"):
        identity.provides.add(UserNeed(current_user.username))

    # Assuming the User model has a list of roles, update the
    # identity with the roles that the user provides
    if hasattr(current_user, "permission"):
        for i in current_user.permission:
            identity.provides.add(RoleNeed(i.permission_details.name))
