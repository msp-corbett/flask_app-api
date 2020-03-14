from app.backend.api.resource.base_model import Entity
from app import db

class Widget_X(db.model, Entity):
    __tablename__ = 'Widget_X'

    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1040), nullable=True)

    def __repr__(self):
        return f"{self.name}: {self.description}"
