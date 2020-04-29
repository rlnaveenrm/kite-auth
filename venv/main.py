import logging
import json
from kiteconnect import KiteConnect
import authentication

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="v1w7029zlz5daycp")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

# url = kite.login_url()
#
# print(url)
#
#
# data = kite.generate_session("KqpOzQYyouaEnvZLd7RcDBJrC91I3E6j", api_secret="2dzsdypnfa44rm2sfr6cr17va0ic07fd")
#
# print(data["access_token"])

kite.set_access_token(authentication.access_token)


print(json.dumps(kite.positions(),indent = 2))
# # Place an order
# try:
#     order_id = kite.place_order(tradingsymbol="INFY",
#                                 exchange=kite.EXCHANGE_NSE,
#                                 transaction_type=kite.TRANSACTION_TYPE_BUY,
#                                 quantity=1,
#                                 order_type=kite.ORDER_TYPE_MARKET,
#                                 product=kite.PRODUCT_NRML)
#
#     logging.info("Order placed. ID is: {}".format(order_id))
# except Exception as e:
#     logging.info("Order placement failed: {}".format(e.message))
#
# # Fetch all orders
# kite.orders()
#
# # Get instruments
# kite.instruments()
#
# # Place an mutual fund order
# kite.place_mf_order(
#     tradingsymbol="INF090I01239",
#     transaction_type=kite.TRANSACTION_TYPE_BUY,
#     amount=5000,
#     tag="mytag"
# )
#
# # Cancel a mutual fund order
# kite.cancel_mf_order(order_id="order_id")
#
# # Get mutual fund instruments
# kite.mf_instruments()