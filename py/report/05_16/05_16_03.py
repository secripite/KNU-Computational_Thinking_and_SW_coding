x= 1
num = []
while True:
    x= int(input())
    if x == 0:
        break
    num.append(x)

print(num)
flag = 0
for i in range(len(num)):
    min = num[i]
    min_num = i
    for j in range(i,len(num)):
        if min > num[j]:
            min = num[j]
            min_num = j
    num[i], num[min_num]= num[min_num], num[i]
    if flag == 1:
        break
    print(num)
print(num)