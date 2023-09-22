for i in range(9,0,-1):
    for j in range(1,8):
        x= i*100 +j
        if 5<=i<=8 and 6<=j:
            break
        else:
            print('%4d'%(x),end='')
    print()
