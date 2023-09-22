foodA = list()
foodB = list()
foodC = list()

kitchen = list()

A=0
B=0
C=0

for i in range(4):
    n = int(input())
    while True:
        x = input()
        if x == '0' or x == 'end':
            break
        elif x == 'foodA':
            foodA.append(n)
        elif x == 'foodB':
            foodB.append(n)
        elif x == 'foodC':
            foodC.append(n)

while True:
    y = input()
    if y == '0':
        break
    kitchen.append(y)

for j in range(len(kitchen)):
    try:
        if kitchen[j] == 'foodA':
            print(foodA[A])
            A+=1
        elif kitchen[j] == 'foodB':
            print(foodB[B])
            B+=1
        elif kitchen[j] == 'foodC':
            print(foodC[C])
            C+=1
    except:
        print('AHH')