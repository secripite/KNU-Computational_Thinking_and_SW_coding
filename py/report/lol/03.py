N = int(input())

if N % 2 != 0:
    for i in range(1,N+1):
        if i%2!=0:
            print(i,end=' ')
        else:
            print(N-i+1,end=' ')

else:
    for i in range(1,N+1):
        if i%2!=0:
            print(i,end=' ')
        else:
            print(N-i+2,end=' ')
