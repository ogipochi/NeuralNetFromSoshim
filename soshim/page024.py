import urllib.request

url="http://uta.pw/shodou/img/28/214.png"
savename="result/test023.png"

mem=urllib.request.urlopen(url).read()

with open(savename,mode="wb")as f:
    f.write(mem)
    print("保存しました")