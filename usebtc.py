#!/usr/bin/python

import mxnbtc

exchange = mxnbtc.BTCExchange()

dolares = exchange.get_usd_mxn()
peso = exchange.get_btc_mxn(4)

bitcoins = exchange.get_mxn_btc(1000)

print dolares
print peso
print bitcoins
