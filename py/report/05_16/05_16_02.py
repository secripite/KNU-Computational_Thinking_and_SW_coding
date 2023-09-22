x= 1
num = []
while True:
    x= int(input())
    if x == 0:
        break
    num.append(x)

print(num)
for i in range(len(num)-1):
    for j in range(len(num)-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
    print(num)
