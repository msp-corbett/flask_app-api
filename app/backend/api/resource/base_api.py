from sqlalchemy import exc
from flask import jsonify
from flask_restful import Resource
from flask_login import login_required
from app import db

class BaseAPI(Resource):

    decorators = [
        'login_required'
    ]

    def __init__(self):
        super().__init__()
        self.db_model = None



    def get(self, pk_id):
        if pk_id is None:
            # return list of resouce
            result = db.session.query(self.db_model).all()
        else:
            # return single resource
            result = db.session.\
                query(
                    self.db_model).\
                filter(
                    self.db_model.ID == pk_id).\
                first()

        return jsonify(result), 200

    def post(self,):
        # create resource
        body_content = request.json

        # TODO: Validate data with marshmallow schema

        new_model = self.db_model(**content)
        try:
            db.session.add(new_model)
            db.commit()
            data, response = {"Success": "New Item Created"}, 200
        except exc.SQLAlchemyError:
            db.session.rollback()
            data, response = {"Error": "Item creation failed"}, 200
        
        return jsonify(data), response

    def put(self, pk_id):
        # create/update resource
        pass


    def patch(self, pk_id):
        # Update single resource
        pass


    def delete(self, pk_id):
        # Remove single resource
        pass