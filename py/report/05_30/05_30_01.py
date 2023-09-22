import random
num = []

while True:
  temp = random.randint(1,1000)
  if num.count(temp) == 0:
    num.append(temp)
  if len(num) == 15:
    break


for i in range(len(num)-1):
    for j in range(len(num)-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
    print(num)
