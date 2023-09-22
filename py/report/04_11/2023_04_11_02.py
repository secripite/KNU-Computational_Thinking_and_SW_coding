list1 = list()

for _ in range(3):
    list1.append(input())

for i in range(3):
    list1[i] = list1[i]+input()
print(list1)