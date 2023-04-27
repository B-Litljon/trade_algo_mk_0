import urllib.parse
import hashlib
import hmac
import base64
import requests
import time

base_url = "https://api.binance.us"

def get_binanceus_signature(data, secret):
    postdata = urllib.parse.urlencode(data)
    message = postdata.encode()
    byte_key = bytes(secret, 'UTF-8')
    mac = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
    return mac

def binanceus_request(uri_path, data, api_key, api_secret):
    headers = {}
    headers['X-MBX-APIKEY'] = api_key
    signature = get_binanceus_signature(data, api_secret)
    payload={
        **data,
        "signature": signature,
    }
    req = requests.get((base_url + uri_path), params=payload, headers=headers)
    return req.text