N1 = int(input())
N2 = int(input())

list1 = list()

for i in range(1,N1+1):
    if N1 % i == 0 and N2 % i == 0:
        list1.append(i)

print(list1)