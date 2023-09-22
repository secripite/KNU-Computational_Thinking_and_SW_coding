N = int(input())

for i in range(N):
    print('%d'%(i+1),end='')
print()

if N % 2 != 0:
    for i in range(1,N+1):
        if i % 2 == 1:
            print('%d'%(i),end='')
        else:
            print('_',end='')
    print()

    for i in range(1,N+1):
        if i % 2 == 0:
            print('%d'%(i),end='')
        else:
            print('_',end='')

if N % 2 == 0:
    for i in range(1,N+1):
        if i % 2 == 0:
            print('%d'%(i),end='')
        else:
            print('_',end='')
    print()

    for i in range(1,N+1):
        if i % 2 == 1:
            print('%d'%(i),end='')
        else:
            print('_',end='')