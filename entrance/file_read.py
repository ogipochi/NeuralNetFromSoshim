# そのままファイルを読みだしその値を返す

fin = open('source/relativityBig','rt')
poem = fin.read()
fin.close()
print(len(poem))