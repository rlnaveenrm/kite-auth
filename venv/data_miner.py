import firebase_admin
import time
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./fs_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
url = 'https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT'
stock_id = url.split('/')[-1]


# Create a callback on_snapshot function to capture changes
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(u'Received document snapshot: {}'.format(doc.to_dict()))

doc_ref = db.collection(u'stocks').document(stock_id)

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)

while True:
    time.sleep(1)
