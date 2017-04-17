#イテレータをつかった読み込み
poem=''
fin=open('source/relativity2','rt')
for line in fin:
    poem+=line
    print(poem)
fin.close()
print(len(poem))