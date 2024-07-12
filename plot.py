from flask_restful import Resource, reqparse
from flask_app.models.function import FunctionModel

class Plot(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'function_id',
        type=int,
        required=True,
        help='Function ID cannot be left blank!'
    )
    parser.add_argument(
        'output_path',
        type=str,
        required=True,
        help='Output path cannot be left blank!'
    )

    @staticmethod
    def post():
        data = Plot.parser.parse_args()
        function = FunctionModel.find_by_id(data['function_id'])
        
        if not function:
            return {'message': 'Function does not exist.'}, 404
        
        output_path = function.save_plot_by_id(data['function_id'], data['output_path'])
        
        return output_path, 200
