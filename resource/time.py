from flask_restful import Resource, reqparse, inputs
import pytz


def GMT8_time(iso_time):
    time = inputs.datetime_from_iso8601(iso_time)
    zone = pytz.timezone('Asia/Chongqing')
    return time.astimezone(zone)


class Time(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('time', type=GMT8_time)

    def post(self):
        args = self.parser.parse_args()
        time = args['time']
        print(time.date())
        print(time.hour)
        print(time.minute)
        print(time.second)
        print(time.microsecond)
        print(time.tzinfo)
        return 'lala'


