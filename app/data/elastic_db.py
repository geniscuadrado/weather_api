# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
import json
from pprint import pprint
import requests
import urllib

from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer

import os,sys
import logging


class ElasticsSearchDB:

    def __init__(self, config):
        self.log = logging.getLogger('Weather Info ElasticSearch')
        self.config = config
        self.url = config.get_url_elastic()
        self.index_elastic = config.get_index_elastic()

    def set_ealastic_db(self, id_place, day):
        uri = '{}/{}/_doc/{}_{}'.format(self.url, self.index_elastic ,id_place, day['date'])

        json_body = json.dumps({ 
          'date': day['date'],
          'temperature_max':day['temperature_max'],
          'temperature_min':day['temperature_min'],
          'humidity':day['humidity'],
          'wind':day['wind'],
          'name':day['name'],
          'id_name': str(id_place),
          'country':day['country']
        })

        headers = {
            'Content-Type': 'application/json',
        }

        try:
            resp = requests.put(uri, headers=headers, data=json_body)
            try:
                resp_text = json.loads(resp.text)
            except:
                resp_text = resp.text
        except Exception as error:
            self.log.error(str(error))
            resp_text = error

        return resp_text

    def get_ealastic_db(self, id_place):
        elastic_client = Elasticsearch(hosts=["localhost"])

        uri = '{}/{}/_doc/_search?pretty'.format(self.url, self.index_elastic)

        query_body = {
            "query": {
                "match": {
                    "id_name": str(id_place)
                }
            }
        }

        try:
            resp = elastic_client.search(index=self.index_elastic, body=query_body)
        except:
            self.log.error(str(error))
            resp = error

        return resp