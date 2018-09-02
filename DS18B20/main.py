#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

# Copyright (C) 2016, shima-nigoro
# This software is under the terms of Apache License v2 or later.

import linecache
import ambient
import time
import requests

DEVICE_NAME='28-01131e75b0c8'

DEVICE_PATH='/sys/bus/w1/devices/'
FILE_NAME='/w1_slave'

ambi = ambient.Ambient(<channelID>, "<apikey>")


class DS18B20():
    def __init__(self):
        self.raw = linecache.getline(DEVICE_PATH + DEVICE_NAME + FILE_NAME,2)[29:]
        self.value = round(float(self.raw) / 1000.0, 1)

if __name__ == "__main__":
    while True:
      print "raw value = " + DS18B20().raw
      print "temperature = " + str(DS18B20().value)

      if DS18B20().value < 25:
        # turn on of the water heater
        requests.get('https://maker.ifttt.com/trigger/under_water_temp/with/key/<ifttt key>')
      elif DS18B20().value > 27:
        # turn off of the water heater
        requests.get('https://maker.ifttt.com/trigger/over_water_temp/with/key/<ifttt key>')


      json={}
      json["d3"]=DS18B20().value
      try:
        ambi.send(json)
      except Exception:
        pass
      time.sleep(300) 
