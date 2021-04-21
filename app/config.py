# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
import json
import logging
import os

class Config():

    def __init__(self):
        self.config_json = {}
        if os.name == 'nt':
            config_file_full_path = os.path.dirname(__file__) + os.sep + os.sep + 'config.json'
        else:
            config_file_full_path = os.path.join(os.path.dirname(__file__),'config.json')

        with open(config_file_full_path) as config_file:
            self.config_json = json.load(config_file)

    def get_log_level(self):
        level = logging.INFO
        if 'logging' in self.config_json.keys() and 'level' in self.config_json['logging'].keys():
            if self.config_json['logging']['level'] == "DEBUG":
                level = logging.DEBUG
            elif self.config_json['logging']['level'] == "INFO":
                level = logging.INFO
            elif self.config_json['logging']['level'] == "WARNING":
                level = logging.WARNING
            elif self.config_json['logging']['level'] == "ERROR":
                level = logging.ERROR
            elif self.config_json['logging']['level'] == "CRITICAL":
                level = logging.CRITICAL
        return level

    def get_log_format(self):
        log_format = '[%(name)s] [%(levelname)s] %(message)s'
        if 'logging' in self.config_json.keys() and 'format' in self.config_json['logging'].keys():
            log_format = self.config_json['logging']['format']
        return log_format

    def get_url_weather(self):
        return self.config_json['url']['weather'] if 'url' in self.config_json.keys()  else "https://api.tutiempo.net"

    def get_url_elastic(self):
        return self.config_json['url']['elastic'] if 'url' in self.config_json.keys()  else "http://localhost:9200"
    
    def get_api_key(self):
        return self.config_json['api_key'] if 'api_key' in self.config_json.keys()  else "qsTqqaa4aqa7qbl"

    def get_index_elastic(self):
        return self.config_json['index_elastic'] if 'index_elastic' in self.config_json.keys()  else "location"

    def get_id_name_test(self):
        return self.config_json['test']['id_name'] if 'id_name' in self.config_json.keys()  else "99461"

    def get_parse_info_test(self):
        return self.config_json['test']['parse_info']

    def get_elastic_info_test(self):
        return self.config_json['test']['parse_elastic']