N = int(input())

for i in range(N,0,-1):
    sum1 = 1
    for j in range(1,N+1):
        if j < i:
            print('  ',end='')
            continue
        else:
            print('%2d'%(j),end='')
            sum1*=j
    print('%7d'%(sum1))         
