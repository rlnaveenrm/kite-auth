import requests
from bs4 import BeautifulSoup
import time
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./fs_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

url = 'https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT'
stock_id = url.split('/')[-2]
print(stock_id)



while True:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    bse = {}
    nse = {}
    price = soup.select('.span_price_wrap')
    last_updated = soup.select('.display_lastupd')
    bse['price'] = price[0].text
    nse['price'] = price[1].text
    bse['last_updated'] = last_updated[0].text
    nse['last_updated'] = last_updated[1].text
    print(nse['last_updated'])
    doc_ref = db.collection(u'stocks').document(stock_id).collection(u'nse').document(nse['last_updated'].split(',')[0])
    doc_ref.set({nse['last_updated']: nse['price']}, merge=True)
    time.sleep(60)


