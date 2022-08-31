# 當 main.py 殺死某進程時，因為無法運作 main ，會呼叫此程式來重新執行 main.py

from time import sleep
from os import system
sleep(7)
system("python main.py")   # 執行 main.py
