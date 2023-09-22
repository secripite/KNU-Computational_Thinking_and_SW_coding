num = int(input())

with open('test1.txt','w+') as file:
    
    for i in range(num,0,-1):
        for j in range(10):
            x = i - j
            if x > 0:
                file.write(str(x)+" ")
        file.write("\n")