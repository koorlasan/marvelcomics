#import requests
import time
import hashlib
#import json


#def check(numofcomics):
#    if type(numofcomics) is int:
#        if 0 < numofcomics <= 100:
#            return True
#        if numofcomics <= 0:
#            print('Number of comics must be greater than 0')
#       else:
#            print('You may not request more than 100 items')
#    return False


publickey = "058789c458e2a5c666c1878c07fdc37b"
privatekey = "277608909782d353e372ac535074386bdb3d8815"
ts = round(time.time())
mystring = str(ts) + privatekey + publickey
hash_object = hashlib.md5(mystring.encode())
mygateway = f'https://gateway.marvel.com/v1/public/comics?orderBy=title&format=comic&formatType=comic&ts={str(ts)}&apikey={publickey}&hash={hash_object.hexdigest()}'

#while True:
#    try:
#        numofcomics = int(input('Number of comics: '))
#        if check(numofcomics):
#            break
#    except ValueError:
#        print('Invalid value. Try again.')

#while True:
#    title = input('Search for: ')
#hash_object = hashlib.md5(mystring.encode())
#mygateway = f'https://gateway.marvel.com/v1/public/comics?orderBy=title&format=comic&formatType=comic&ts={str(ts)}&apikey={publickey}&hash={hash_object.hexdigest()}'
 #   res = requests.get(mygateway).json()
 #   comics = res['data']['results']
#&titleStartsWith={title}
#&limit={numofcomics}