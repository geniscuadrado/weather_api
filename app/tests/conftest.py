# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
import pytest

from ..config import Config 
from ..data.elastic_db import ElasticsSearchDB


@pytest.fixture()
def dummy_response():
    config = Config()
    return config.get_parse_info_test()

@pytest.fixture()
def dummy_elasticdb():
    config = Config()
    elasticDB = ElasticsSearchDB(config)
    return elasticDB

@pytest.fixture()
def dummy_elastic():
    config = Config()
    return config.get_elastic_info_test()

