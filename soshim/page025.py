import urllib.request

# データの取得
#urlの先には
# [ip] API_URI=http://api.aoikujira.com/ip/get.php REMOTE_ADDR=103.5.140.134 REMOTE_HOST=103.5.140.134 REMOTE_PORT=54894 HTTP_HOST=api.aoikujira.com HTTP_USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36 HTTP_ACCEPT_LANGUAGE=ja,en-US;q=0.8,en;q=0.6 HTTP_ACCEPT_CHARSET= SERVER_PORT=80 FORMAT=ini
url="http://api.aoikujira.com/ip/ini"
res=urllib.request.urlopen(url)
data=res.read()

text = data.decode("utf-8")
print(text)