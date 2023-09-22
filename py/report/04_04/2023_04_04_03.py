F = int(input())
C = int(input())

for i in range(F,0,-1):
    for j in range(1,C+1):
        x = i*100 + j-i+1
        if j < i:
            print('    ',end='')
        else:
            print('%4d'%(x),end='')
    print()
