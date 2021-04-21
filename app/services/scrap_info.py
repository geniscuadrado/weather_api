# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
import json
import requests

import logging

from ..constanst import CONST
from ..code_error import CodeError


class WeatherInformation:

    def __init__(self, config):
        self.log = logging.getLogger('Weather App Get Info API')
        self.config = config
        self.url = config.get_url_weather()
        self.api_key = config.get_api_key()

    def get_weeather_info(self, param):

        try:
            response = requests.get(
                '{}/json/?lan=es&apid={}&lid={}'.format(self.url, self.api_key, param)
            )

            resp = json.loads(response.text)

        except Exception as error:
            self.log.error(str(error))

            resp = error

        return resp
