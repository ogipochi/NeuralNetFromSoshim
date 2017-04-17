import urllib.request
# urlを指定してresultフォルダにコピーする
# retrieveとは検索の意
url="http://uta.pw/shodou/img/28/214.png"
savename="result/test023.png"

urllib.request.urlretrieve(url,savename)
print("保存しました")