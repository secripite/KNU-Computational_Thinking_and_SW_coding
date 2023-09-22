with open('test.txt','w+') as f1:
    x = int(input())

    for i in range(1,x+1):
        f1.write(str(i)+' lines\n')

    x = int(input())
    if x < 10:
        num = (x-1)*9
    elif x < 100:
        num = 81
        num += (x-10)*10
    else:
        num = 981
        num += (x-100)*11

    

    f1.seek(num,0)
    string = f1.readline().strip()

    print(string)