#文字数の上限を指定してファイルを読みだす

poem=''
fin=open('source/relativity','rt')
chunk=100
#while True:でbreakされるまで繰り返し
while True:
    fragment=fin.read(chunk)
    if not fragment:
        break
    poem+=fragment
    print(len(poem))

fin.close()
print(len(poem))