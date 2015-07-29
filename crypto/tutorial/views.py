# -*- coding: utf-8 -*-
from django.shortcuts import render
from Crypto.PublicKey import RSA
from django.http import HttpResponse
import os,json
# Create your views here.
token = 'shanshan'
private_key_path = 'private_key.pem'
public_key_path = 'public_key.pem'
result = 'laoshifu'
nonce = '12345678'

def initialKey():
    key = RSA.generate(2048)
    f = open(private_key_path,'w')
    f.write(key.exportKey())
    f.close()
    return key

def keyIsExist(file_name):
    return os.path.exists(file_name)

def generatePublicKey(key):
    public_key = key.publickey()
    return public_key

def checkMessage(cipher_text):
    if(keyIsExist(private_key_path)):
        f = open(private_key_path, 'r')
        key = RSA.importKey(f.read())
        cipher = cipher_text.split(',')[0][2:-1].decode('string-escape')
        message = (cipher,)
        result = key.decrypt(message)
        return result == token
    else:
        #initialKey()
        return False

def message(request):
    if request.method == 'GET':
        f = request.GET
        message = f.get('message')
        return HttpResponse(json.dumps({'result': token}), content_type="application/json")

def safe_message(request):
    if request.method == 'POST':
        data = json.loads(request.body).get('message')
        #data = data.encode('UTF-8')
        if checkMessage(data):
            return HttpResponse(json.dumps({'result': token}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'result': 'please contact admin for public key'}), content_type="application/json")



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


def test(request):
    message = encryptMessage(token)
    result = checkMessage(message)
    print result
    return HttpResponse(json.dumps({'result': result}), content_type="application/json")