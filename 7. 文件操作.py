with open('./test.txt','r') as f:
    text = f.read()
    times = text.count('第')
    print(times)