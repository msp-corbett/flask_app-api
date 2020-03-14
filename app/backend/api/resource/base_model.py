from app import db

class Entity(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    CreatedBy = db.Column(db.String(100), nullable=False)
    CreatedByUserID = db.Column(db.Integer, nullable=False)
    CreatedDate = db.Column(db.DateTime)
    LastEditedBy = db.Column(db.String(100, nullable=False))
    LastEditedByUserID = db.Column(db.Integer, nullable=False)
    LastEditedDate = db.Column(db.DateTime)