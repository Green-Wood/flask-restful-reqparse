from datetime import datetime
from flask_restful import inputs
import pytz


if __name__ == '__main__':
    time = inputs.datetime_from_iso8601("2019-07-14T02:08:07.018Z")
    zone = pytz.timezone('Asia/Chongqing')
    print(pytz.all_timezones)