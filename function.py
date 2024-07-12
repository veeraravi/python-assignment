from flask_restful import Resource, reqparse
from flask_app.models.function import FunctionModel

class Function(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'function_id',
        type=int,
        required=True,
        help='Function ID cannot be left blank!'
    )
    parser.add_argument(
        'y_intercept',
        type=float,
        required=True,
        help='Y-intercept cannot be left blank!'
    )
    parser.add_argument(
        'slope',
        type=float,
        required=True,
        help='Slope cannot be left blank!'
    )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help='Description cannot be left blank!'
    )

    @staticmethod
    def post():
        data = Function.parser.parse_args()
        if FunctionModel.find_by_id(data['function_id']):
            return {'message': 'Function already exists.'}, 400
        
        if not FunctionModel.verify_description(data['description']):
            return {'message': 'Description has improper brackets.'}, 400
        
        function = FunctionModel(**data)
        function.save_to_db()
        
        return {'message': 'Function has been saved.'}, 200
