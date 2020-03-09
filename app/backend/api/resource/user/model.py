from sqlalchemy import UniqueConstraint
from __main__ import db

class User(db.Model):
    __tablename__ = "User"

    __table_args__ = (
        UniqueConstraint("Email", name="UIX_User_Emails"),
    )

    ID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(150))
    LastName = db.Column(db.String(150))
    Email = db.Column(db.String(150))
