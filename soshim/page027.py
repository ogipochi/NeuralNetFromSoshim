import urllib.request
import urllib.parse
# urlを開く際にパラーメータを渡す
API = "http://api.aoikujira.com/zip/xml/get.php"

values={
    'fmt':'xml',
    'zn':'1500042'
}
params=urllib.parse.urlencode(values)
print(params)
url=API+"?"+params
print("url=",url)

data=urllib.request.urlopen(url).read()
text=data.decode("utf-8")
print(text)