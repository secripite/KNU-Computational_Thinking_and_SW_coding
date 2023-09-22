import random
num = []

while True:
  temp = random.randint(1,1000)
  if num.count(temp) == 0:
    num.append(temp)
  if len(num) == 15:
    break


for i in range(len(num)):
    min = num[i]
    min_num = i
    for j in range(i,len(num)):
        if min > num[j]:
            min = num[j]
            min_num = j
    num[i], num[min_num]= num[min_num], num[i]
    print(num)
print(num)