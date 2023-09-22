str1 = input()

num = 1
for i in str1:
    if num %2 == 0 and num % 3 == 0:
        print(i*4)
    elif num % 2 == 0:
        print(i*2)
    elif num % 3 == 0:
        print(i*3)
    else:
        print(i)
    num+=1