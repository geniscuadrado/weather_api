# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
from fastapi import FastAPI
from typing import Optional

from app.config import Config
from app.data.elastic_db import ElasticsSearchDB
from app.services.scrap_info import WeatherInformation
from app.services.parse_info import ParseInfo

app = FastAPI()

config = Config()

@app.get("/weather/{city_id}")
def read_item(city_id: int):
    
    weather_info =  WeatherInformation(config)
    parse_info = ParseInfo()

    data_raw = weather_info.get_weeather_info(city_id)
    data_parsed = parse_info.set_parse(data_raw)

    return data_parsed

@app.put("/elasticsearch/{city_id}")
def read_item(city_id: int):
    weather_info =  WeatherInformation(config)
    parse_info = ParseInfo()

    elastic_db = ElasticsSearchDB(config)

    data_raw = weather_info.get_weeather_info(city_id)
    data_parsed = parse_info.set_parse(data_raw)

    for day in data_parsed:
        elastic_db.set_ealastic_db(city_id, day.__dict__)

    return data_parsed

@app.get("/elasticsearch/{city_id}")
def read_item(city_id: int):
    
    elastic_db = ElasticsSearchDB(config)
    data_parsed = elastic_db.get_ealastic_db(city_id)

    return data_parsed