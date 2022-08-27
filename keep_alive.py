# 利用 Flask 建立程式(之後會利用 "UpTime bot" 定時造訪此網頁，使機器人不會停止運行 )

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "hello im alive!"
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
