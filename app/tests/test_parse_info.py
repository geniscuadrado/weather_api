# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
import json

from ..config import Config
from ..services.parse_info import ParseInfo


class TestParseInfo:

    def test_parse_info(self, dummy_response):
        config = Config()
        parse_info = ParseInfo()
        
        data_parsed = parse_info.set_parse(dummy_response)[0]
        data_json_parsed  = json.dumps(data_parsed.__dict__)

        expected_data = {'date': '2021-4-11', 'temperature_max': 25, 'temperature_min': 14, 'humidity': 80, 'wind': 10, 'name': 'Ambalavao', 'country': 'Madagascar'}

        for key, value in data_parsed.__dict__.items():
            assert key  in expected_data and value == expected_data[key]