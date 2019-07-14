from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage


class File(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=FileStorage, location='files')

    def post(self):
        args = self.parser.parse_args()
        file = args['file']
        file.save('test.jpg')