num = int(input())

for i in range(num,0,-1):
    if i%3 == 0 and i%5 == 0:
        print(int(i/3))
        break