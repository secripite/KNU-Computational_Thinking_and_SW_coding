num = list()

while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)

num = sorted(num)

if len(num)%2!=0:
    print(num[len(num)//2])
else:
    print(num[len(num)//2-1])
    