from flask_restful import Resource
from flask_login import login_required

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
            pass
        else:
            # return single resource
            pass


    def post(self,):
        # create resource
        pass


    def put(self, pk_id):
        # create/update resource
        pass


    def patch(self, pk_id):
        # Update single resource
        pass


    def delete(self, pk_id):
        # Remove single resource
        pass