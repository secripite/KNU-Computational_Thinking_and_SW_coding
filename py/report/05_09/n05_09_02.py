import n05_09_01

num1 = (n05_09_01.prime(int(input())))
num2 = (n05_09_01.prime(int(input())))

list1 =[]

for i in num1:
    if i in num2:
        list1.append(i)
        num2.pop(num2.index(i))

print(list1)