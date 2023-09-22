a = {1:'g'}
name = [0,0,0]
for i in range(3):
    name[i] = input()
    a[name[i]] = 1

for i in range(3):
    a[name[i]] = input()

print(a[input()])