# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
from unittest.mock import patch

from ..config import Config
from ..data.elastic_db import ElasticsSearchDB


class TestElastic:

    def test_elastic_db(self, dummy_elasticdb, dummy_elastic):
        config = Config()
        elasticDB = dummy_elasticdb

        id_place  = config.get_id_name_test()

        with patch("fastApi_docker.app.data.elastic_db.Elasticsearch.search",
            return_value=config.get_elastic_info_test()) as patched:
                response = dummy_elasticdb.get_ealastic_db(dummy_elastic)

        assert response['hits']['total']['value'] > 0

   