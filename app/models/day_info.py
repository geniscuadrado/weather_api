# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
from typing import Dict


class Day:
    date: str
    temperature_max: int
    temperature_min: int
    humidity: int
    wind: int
    name: str
    country: str

    def __init__(
        self, date: str, temperature_max: int, temperature_min: int, humidity: int, wind: int, name: str, country: str
        ) -> None:
        self.date = date
        self.temperature_max = temperature_max
        self.temperature_min = temperature_min
        self.humidity = humidity
        self.wind = wind
        self.name = name
        self.country = country