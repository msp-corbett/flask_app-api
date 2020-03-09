from app.backend.api.resource.user.model import User
from __main__ import db, login

@login.user_loader
def load_user(username):

    return User.query.get(username)

class Permission(db.Model): # type: ignore
    """ Table of available Permissions """

    __tablename__ = "Permission"

    ID = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False)

    name = db.Column(
        db.String(128),
        nullable=False)

    def __repr__(self):
        return f"Permission {self.name}"


class UserPermission(db.Model): # type: ignore
    """ Class to map available permissions to a user. """

    __tablename__ = "UserPermission"

    UserId = db.Column(
        db.Integer,
        db.ForeignKey('User.ID'),
        primary_key=True)

    PermissionId = db.Column(
        db.Integer,
        db.ForeignKey('Permission.ID'),
        primary_key=True)

    user_details = db.relationship(
        'User',
        backref='permission',
        lazy="select")

    permission_details = db.relationship(
        'Permission',
        backref='user',
        lazy="select")

    def __repr__(self):
        return f"User: {self.user_details.username}, Permission {self.permission_details.name}"
