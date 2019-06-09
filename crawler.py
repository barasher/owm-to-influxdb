import argparse
import requests
import logging
import json
import sys

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
STATION_URL_PARAM = 'id'
APPID_URL_PARAM = 'appid'
UNIT_URL_PARAM = 'units'
UNIT_URL_VALUE = 'metric'

LOG_FORMAT = '%(asctime)s [%(levelname)-5.5s] %(message)s'

RET_CODE_OK = 0
RET_CODE_ERROR = 2

def main():

    try:
        logging.basicConfig(format=LOG_FORMAT, stream=sys.stderr)
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--appid', required=True, help='OpenWeatherMap app ip')
        parser.add_argument('-s', '--station', required=True, help='Station identifier')
        parser.add_argument('-l', '--location', required=True, help='Location')
        args = parser.parse_args()

        params={STATION_URL_PARAM: args.station, APPID_URL_PARAM: args.appid, UNIT_URL_PARAM: UNIT_URL_VALUE}
        r = requests.get(BASE_URL, params=params)
        if r.status_code != 200:
            logging.error('Unexpected status code: {}'.format(r.status_code))
            return RET_CODE_ERROR

        raw = r.json()
        print('weather,location={} temp={},pressure={},humidity={} {}'.format(args.location,
            raw['main']['temp'],
            raw['main']['pressure'],
            raw['main']['humidity'],
            raw['dt']*(10**9)))

        return RET_CODE_OK

    except Exception as e:
        logging.error('Error: {}'.format(e))
        return RET_CODE_ERROR


if __name__ == '__main__':
    sys.exit(main())
