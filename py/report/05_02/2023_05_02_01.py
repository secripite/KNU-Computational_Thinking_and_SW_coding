def calculator(a):
    return(eval(a))

a = []

for i in range(3):
    a.append(input())

print(calculator(a[0]+a[2]+a[1]))