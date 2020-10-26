import datetime
import json
import pymongo
import requests_oauthlib
import tqdm
from requests_oauthlib import OAuth1Session

#Twitter DevelopersサイトでAPIキーを発行
api_key = 'Lu3q4oWtRfIkUjRwPbWmVq6PG'
api_secret = 'oT7mFfDTYue0wHk1wxeRlBBwR00mS5pjFyeTR8TDABFbFU7mju'
access_token_key = '894736756926316544-EgRXWn3NNb0EmRpldPyxUAGO77ovFkK'
access_token_secret = 'KFp2hhShhA5DEFc2kMfWqz81AJicf8mpAaCODKPEt8YCe'
#Twitter Streaming APIを実行
session = OAuth1Session(api_key, api_secret, access_token_key, access_token_secret)

uri = "https://stream.twitter.com/1.1/statuses/sample.json?language=ja"
r = session.get(uri, stream=True)
r.raise_for_status()
#サンプリングされたツイートをMongoDBに格納
mongo = pymongo.MongoClient()
for line in tqdm.tqdm(r.iter_lines(), unit='tweets', mininterval=1):
    if line:
        tweet = json.loads(line)
        #データ受信時のタイムスタンプを追加
        tweet['_timestamp'] = datetime.datetime.utcnow().isoformat()
        mongo.twitter.sample.insert_one(tweet)