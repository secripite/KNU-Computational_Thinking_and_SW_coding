fir = int(input())
sec = int(input())


num1 = 0
num2 = 0

alll = fir & sec
num1 += alll & 1
alll >>= 1
num1 += alll & 1
alll >>= 1
num1 += alll & 1
alll >>= 1
num1 += alll & 1

one = fir | sec
num2 += one & 1
one >>= 1
num2 += one & 1
one >>= 1
num2 += one & 1
one >>= 1
num2 += one & 1


print(num1)
print(num2)
