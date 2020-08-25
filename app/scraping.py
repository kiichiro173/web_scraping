import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def get_udemy_info():
  url =  'https://scraping-for-beginner.herokuapp.com/udemy'

  r = requests.get(url)
  soup = BeautifulSoup(r.text,'html.parser')

  name = soup.select('.card-title')[0].string

  n_subscribers = soup.select('.subscribers')[0].string
  n_subscribers = int(n_subscribers.split('：')[1])

  n_reviews = soup.select('.reviews')[0].string
  n_reviews = int(n_reviews.split('：')[1])

  results = {
      'name':name,
      'n_subscribers':n_subscribers,
      'n_reviews':n_reviews
  }

  return results

def write_data():
  df = pd.read_csv("./data.csv")

  #新規データ
  _results = get_udemy_info()

  #書き込みデータ
  date = datetime.datetime.today().strftime("%Y/%m/%d")
  subscribers = _results["n_subscribers"]
  reviews = _results["n_reviews"]
  results = pd.DataFrame([[date , subscribers , reviews]] , columns = ['date' , 'subscribers' , "reviews"])

  df = pd.concat([df,results])
  df.to_csv('data.csv' , index=False)
  print("完了しました")

if __name__=="__main__":
      write_data()