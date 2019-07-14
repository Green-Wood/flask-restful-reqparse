from flask import Flask
from flask_restful import Api
from resource.json import ParseJson
from resource.multi_args import Multi
from resource.time import Time
from resource.file import File

app = Flask(__name__)
api = Api(app)

api.add_resource(ParseJson, '/json')
api.add_resource(Multi, '/multi')
api.add_resource(Time, '/time')
api.add_resource(File, '/file')

if __name__ == '__main__':
    app.run(debug=True)

