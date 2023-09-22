str1 = input()
pat = int(input())
num = len(str1)

for i in str1:
    if num >= pat:
        print(i*num)
        num-=1
    else:
        num=len(str1)
        print(i*num)
        num-=1