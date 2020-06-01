import firebase_admin
import time
from firebase_admin import credentials
from firebase_admin import firestore
import indicators_stock
import math
import random
import pandas as pd
import numpy as np
from datetime import date, datetime
import preprocessing
import matplotlib.pyplot as plt 
import collections


cred = credentials.Certificate("./fs_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
url = 'https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT'
stock_id = url.split('/')[-2]
date_today = date.today()
date_formated = date_today.strftime("%b %d")
time_period = 14
# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        data_fbase = doc.to_dict()
        #print(data_fbase)
        data_received =  [int(float(x)) for a,x in data_fbase.items()]
        time_received =  [datetime.strptime(a, '%b %d, %H:%M') for a,x in data_fbase.items()]
        time_received =  [datetime.strftime(a, '%H:%M') for a in time_received]
        idx = np.argsort(time_received)
        high = max(data_received[:time_period])
        low = min(data_received[:time_period])
        last_value = data_received[len(data_received)-1]
        last_value_loockback = data_received[-time_period]
        print(last_value_loockback)
        william_R = indicators_stock.calulcate_percent_r(highest_high = high, lowest_low= low, close = last_value)
        mom = indicators_stock.calculate_mom(close_values_now = last_value, close_values_lookback=last_value_loockback)
        roc = indicators_stock.calculate_roc(close_values_now = last_value, close_values_lookback=last_value_loockback)
        print(f'William R: {william_R}')
        print(f'MoM: {mom}')
        print(f'ROC: {roc}')


print(date_formated)
doc_ref = db.collection(u'stocks').document(stock_id).collection(u'nse').document(date_formated)

virtual_cash = 10000
stop_loss = None
profit_percentage = None
# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)

while True:
    time.sleep(1)
