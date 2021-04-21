# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:47:45 2021

@author: geniscuadrado@gmail.com
"""
from ..models.day_info import Day


class ParseInfo:

    def set_parse(self, data_to_parse):
        days_info = []
        locality_name = ""
        locality_country = ""

        for key, value in data_to_parse.items():
            if key.startswith('locality'):
                locality_name = value['name']
                locality_country = value['country']

            if key.startswith('day'):
                day_info = Day(
                    value['date'],
                    value['temperature_max'],
                    value['temperature_min'],
                    value['humidity'],
                    value['wind'],
                    locality_name,
                    locality_country
                )
                days_info.append(day_info)
        
        return days_info
         