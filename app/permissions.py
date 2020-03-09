from flask_principal import (
    Permission, RoleNeed)

user_permission = Permission(RoleNeed('user'))
admin_permission = Permission(RoleNeed('admin'))
god_permission = Permission(RoleNeed('god'))