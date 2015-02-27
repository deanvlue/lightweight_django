#!/usr/bin/python
from __future__ import division
import os, sys, json
import requests

"""
print "1 Bitcoin es igual a {0} Pesos Mexicanos".format(mxnbtc)
print "1 Peso Mexicano equivale a {0} Bitcoins, {1} satoshis".format(btcmxn, satoshimxn)
print "Buy: {0}".format( usdbtc_buy * usdmxn)
print "Sell: {0}".format( usdbtc_sell * usdmxn)
print "Last: {0}".format( usdbtc_last * usdmxn)
"""

class BTCExchange:

    def __init__(self):
        usd_btc_url ='https://blockchain.info/ticker'
        usd_mxn_url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDMXN%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
   
        r_usd_mxn = requests.get(usd_mxn_url)
        r_usd_btc = requests.get(usd_btc_url)
    
        self.usdbtc_buy = float(r_usd_btc.json()["USD"]["buy"])
        self.usdbtc_sell = float(r_usd_btc.json()["USD"]["sell"])
        self.usdbtc_last = float(r_usd_btc.json()["USD"]["last"])
        self.usdmxn = float(r_usd_mxn.json()["query"]["results"]["rate"]["Ask"])
        self.mxnbtc = float("{0:.4f}".format(self.usdbtc_buy * self.usdmxn))
        self.btcmxn = float("{0:.8f}".format(1 / self.mxnbtc))
        self.satoshimxn = self.btcmxn * 100000000

    def get_usd_mxn(self,pesos=0):
        if pesos != 0:
            return pesos * self.usdmxn
        else:
            return self.usdmxn

