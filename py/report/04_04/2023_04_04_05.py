N = int(input())
sum1 = 0
Big = 0
Small = 0

Big = N // 10
sum1 += Big * 8
sum1 += N
    
if N % 10 > 5 :
    sum1 += 8
    Big+=1
else:
    sum1 += 5
    Small = 1

print(Big)
print(Small)
print(sum1)
