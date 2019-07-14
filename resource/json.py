from flask_restful import Resource, reqparse


class ParseJson(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("age", type=int)

    def post(self):
        args = self.parser.parse_args()
        print(args['name'])
        print(args['age'])
        return 'haha'
