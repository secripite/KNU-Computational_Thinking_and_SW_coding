x = input()

for i in range(len(x)):
    for j in range((i)%3+1):
        print(x[i],end='')
    print()