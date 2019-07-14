from flask_restful import Resource, reqparse


class Multi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('age', type=int, action='append')
    parser.add_argument('name', type=str, action='append')

    def post(self):
        args = self.parser.parse_args()
        print(args)
        return "nana"
