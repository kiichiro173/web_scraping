import requests

url = 'https://www.kaggle.com/kiii1234/notebooks'
response = requests.get(url)

response.encoding = response.apparent_encoding

filename = "download2.txt"
#f = open(filename , mode = "w")#ファイルを書き込みモードで開いている
#f.write(response.text)
#f.close()

#with構文を使用するとファイルを開いて閉じるということを省略して書くことができる
with open(filename , mode = "w") as f:
    f.write(response.text)
