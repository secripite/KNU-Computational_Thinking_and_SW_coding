while True:
    x = int(input())
    if x == 0 or x == 1:
        break
    else:
        for i in range(2,x+1):
            if x // i == 1:
                print('Prime Number')
                break
            elif x % i == 0 and x != i:
                print('No Prime Number')
                break
