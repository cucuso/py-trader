#import gemini
import requests
import time
import json
import base64
import hmac
import hashlib


base_url = "https://api.sandbox.gemini.com"
endpoint = "/v1/order/new"
url = base_url + endpoint

gemini_api_key = "account-TzWDjoSksCU7VYHv4jVS"
gemini_api_secret = "mZr7JAfBkEnCY79QWkTM1CQK46z".encode()

def execute_trade(side):
    print(f'executing [{side}] trade')
    payload_nonce = time.time()

    payload = {
        "request": "/v1/order/new",
        "nonce": payload_nonce,
        "symbol": "btcusd",
        "amount": "1",
        "price": "30633.00",
        "side": "buy",
        "type": "exchange limit",
        "options": ["maker-or-cancel"]
    }

    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

    request_headers = {'Content-Type': "text/plain",
                       'Content-Length': "0",
                       'X-GEMINI-APIKEY': gemini_api_key,
                       'X-GEMINI-PAYLOAD': b64,
                       'X-GEMINI-SIGNATURE': signature,
                       'Cache-Control': "no-cache"}

    response = requests.post(url,
                             data=None,
                             headers=request_headers)

    new_order = response.json()
    print(new_order)