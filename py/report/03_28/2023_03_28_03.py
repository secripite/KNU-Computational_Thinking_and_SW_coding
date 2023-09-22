x = int(input())

sum2=0
temp=1

for i in range(x):
    temp += i
    sum2 += temp
    
print(f'{sum2}')
