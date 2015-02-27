#!/usr/bin/python

import mxnbtc

exchange = mxnbtc.BTCExchange()

dolares = exchange.get_usd_mxn()

print dolares
