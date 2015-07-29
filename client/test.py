# -*- coding: utf-8 -*-
__author__ = 'wayne'
from Crypto.PublicKey import RSA
import requests, json
public_key_path = 'public_key.pem'
token = 'shanshan'
nonce = '12345678'

def getPublicKey():
    f = open(public_key_path, 'r')
    key = RSA.importKey(f.read())
    f.close()
    return key

def encryptMessage(message):
    p_key = getPublicKey()
    result = p_key.encrypt(token, nonce)
    #print 'client encrypt message %s' % result
    return result

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/message/'
    safe_url = 'http://127.0.0.1:8000/safe_message/'
    session = requests.Session()
    message = encryptMessage(token)
    data = {
        'message': str(message),
    }
    r = session.post(safe_url, json.dumps(data))
    print r.text