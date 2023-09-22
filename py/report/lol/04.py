N = int(input())

sum1 = 0
sum2 = 0

for i in range(1,N+1):
    if i % 2 == 0:
        sum1+=i
    if i % 3 == 0:
        sum2+=i

print(sum1,sum2)