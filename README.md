# Discord-Bot-ELM

自製的 DC bot 可以在 Replit 持續運行， <br>
因為參考了蠻多教學，但並沒有一個統一可行的版本<br>
所以東拼西奏好不容易試成功了

<br>

## 1. 此 Bot 的功能
- 有人加入 dc 伺服器時會打招呼
- 利用 "reaction role name" ( 點選 emoji ) 方式選擇身分組
- 簡單對話
- 隨機發送 meme (來源url: 'https://www.reddit.com/r/dankmemes/new.json?sort=hot')
- 隨機發送貓咪圖片 (來源url: 'https://www.reddit.com/r/cat/new.json?sort=hot')
<br>

## 2. 文件說明
- main.py : bot 的主程式
- keep_alive.py : 用 Flask 製作出的簡單網頁，目的是為了可以用 [UpTime bot](https://uptimerobot.com/)定期造訪，
使 bot 可以在 Replit 持續運行
- restarter.py : 當有進程發生問題時，會利用此程式重啟 main.py
<br>

## 3. 自訂義
如果要自訂義一個 bot 的功能，只要更改有 @client.event 的函數即可<br>
開頭即尾端視情況進行修改，那邊主要是設定權限、使 bot 活著 <br>
更多指令介紹可參見 [discord.py](https://discordpy.readthedocs.io/en/stable/index.html)<br>
<br>
------------2022/9/6 更新 ---------------<br>
不知道為什麼 Replit 容易斷線，最後換一個每月 1 鎂的 host 了 ( 無須 keep_alive )
