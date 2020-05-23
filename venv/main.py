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

url = 'https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI'
stock_id = url.split('/')[-2]
print(stock_id)
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

doc_ref = db.collection(u'stocks').document(stock_id)
doc_ref.set({
    u'bse': bse,
    u'nse': nse,
})

def convert_to_unix(last_updated):
    time.mktime(datetime.datetime.strptime(last_updated, "%d/%m/%Y").timetuple())
