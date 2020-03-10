from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_args
from app.backend.api.resource.user.model import User, UserSchema
from app.backend.api.api_error import APIError
from app.backend.api.utility.query_filter import filter_query
from app import db

class ClientAPI(Resource):

    decorators = [
        'login_required'
    ]

    def __init__(self):
        super().__init__()
        self.model = User
        self.schmea = UserSchema


    @use_args({'filters': fields.Str(missing=''), 'pageSize': fields.Int(missing=25), 'page': fields.Int(missing=1)})
    def get(self, args, pk_id):
        if pk_id is None:
            # return a list of resource
            if args['filters']:
                try:
                    # query model with filter(s) passed in url parameters
                    result_list = filter_query(query=db.session.query(self.model), raw_filters=args['filters'], model=self.model)
                except APIError as err:
                    return {"Error": err.error_source}, err.error_code
            else:
                result_list = db.session.query(self.model)

            # paginate results with offset
            offset = (args['page'] - 1) * args['pageSize']

            result_list = result_list.offset(offset).limit(args['pageSize'])
            schema = self.schmea(many=True)
            result_list = schema.dump(result_list)

            return result_list, 200
        else:
            # return single resource
            result = db.session.query(self.model).filter(self.model.ID == pk_id).first()
            result = self.schmea.dump(result)

            return result_list, 200



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