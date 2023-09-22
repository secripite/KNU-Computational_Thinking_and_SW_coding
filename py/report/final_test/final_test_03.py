num = int(input())

resert = 0

for i in range(1,num+1):
    resert += (-1)**(i-1)*i

print(resert)