#「人工知能」を含むツイートを取得してください。
import time
from requests_oauthlib import OAuth1Session
import json
import datetime, time, sys
 
CK = 'AxH3XJGIeqsz8IcnROFYhMIxq'                             # Consumer Key
CS = 'RdJRXRvVTncJ9K0I0aEUZr34NLi9E2lT3p3tHqQOqMUSLu8wwg'         # Consumer Secret
AT = '728488434826772481-158c2BioeYhEDOQoIuiYzq1xxgv2VtV' # Access Token
AS = 'H5TrpQnd86JXCq9gPxnxk2CsTZYLYhzhEo4dtD3hajqh5'         # Accesss Token Secert
 
session = OAuth1Session(CK, CS, AT, AS)
 
url = 'https://api.twitter.com/1.1/search/tweets.json'
res = session.get(url, params = {'q':u'人工知能', 'count':100})
res_text = json.loads(res.text)
for tweet in res_text['statuses']:
    print ('-----')
    print (tweet['created_at'])
    print (tweet['text'])