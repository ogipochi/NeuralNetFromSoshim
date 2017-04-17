# coding:utf-8
import urllib.request

url="http://uta.pwshodou/img/28/214.png"
savename="result/test.png"

mem=urllib.request.urlopen(url).read()

with open(savename,mode="wb") as f:
     f.write(mem)
     print("保存しました")