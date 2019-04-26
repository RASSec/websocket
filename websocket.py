#coding=utf-8
#codz=yds
import re
import threading
from websocket import create_connection

def test_DNS_Servers():
    global count
    lock.acquire()
    while True:
        ws = create_connection("ws://123.1.1.1:9010/ajaxchattest")
        ws.send("Hello, World>>1")##发送消息 eg:{'id':'1','un':'xx'}
        result = ws.recv()##接收消息
        count=count+1
        #print (result)
        #ws.close()
        print (count)
    lock.release()
lock=threading.Lock()

count=0
threads = []
for i in range(1000):
    t = threading.Thread(target=test_DNS_Servers)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print (count)
print ('All Done!')
