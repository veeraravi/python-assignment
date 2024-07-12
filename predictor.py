from flask_restful import Resource, reqparse
from flask_app.models.function import FunctionModel

class Predictor(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'function_id',
        type=int,
        required=True,
        help='Function ID cannot be left blank!'
    )
    parser.add_argument(
        'value',
        type=float,
        required=True,
        help='Value cannot be left blank!'
    )

    @staticmethod
    def post():
        data = Predictor.parser.parse_args()
        function = FunctionModel.find_by_id(data['function_id'])
        
        if not function:
            return {'message': 'Function does not exist.'}, 404
        
        result = function.predict_by_id(data['function_id'], data['value'])
        return result, 200
