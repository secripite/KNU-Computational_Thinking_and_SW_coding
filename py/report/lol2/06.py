num = int(input())

if num <= 10:
    print(20)
elif num <= 20:
    print(20 + (num-10)*1)
else:
    if (num-20) % 4 == 1 or (num-20) % 4 == 3:
        print(30 + int((num-20)/2)+1)
    else:
        print(30 + int((num-20)/2))