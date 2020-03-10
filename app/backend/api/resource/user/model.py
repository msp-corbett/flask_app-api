from sqlalchemy import UniqueConstraint
from marshmallow import post_dump, pre_load,  post_load
from app import db, ma

class User(db.Model):
    __tablename__ = "User"

    __table_args__ = (
        UniqueConstraint("Email", name="UIX_User_Emails"),
    )

    ID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(150))
    LastName = db.Column(db.String(150))
    Email = db.Column(db.String(150))


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
