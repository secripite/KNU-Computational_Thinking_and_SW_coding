num = int(input())


list1 = [0, 0, 0, 0]

if num % 80 < num % 100:
    list1[1] = num//80
    num%=80
    list1[2] = num//50
    num%=50
    list1[3] = num//10
else:
    list1[0] = num//100
    num%=100
    list1[1] = num//80
    num%=80
    list1[2] = num//50
    num%=50
    list1[3] = num//10

print(list1)