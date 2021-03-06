#!/usr/bin/env python

from utils import readurl
from price import Price
from exchange import Exchange

import json
import shutil
import wget
import os

#example for gdax_btc_url = "https://api.gdax.com/products/BTC-USD/ticker"
base_url = "https://api.gdax.com/products/"

class Gdax(Exchange):

   def __init__(self):
      self.name = "Gdax"

   def get_rates(self):
      self.price = Price()
      self.price.btc = self.get_price("BTC")
      self.price.ltc = self.get_price("LTC")
      self.price.bch = self.get_price("BCH")
      self.price.eth = self.get_price("ETH")

   def get_price(self, currency):
      url = base_url + currency + "-USD/ticker"
      cache_file_name = ".gdax" + currency + ".json"
      jsonfile = readurl(url, cache_file_name)
      price = float(jsonfile['price'])
      return  price

