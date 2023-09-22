tons = list(map(int, input().split()))

time = 0
num = 0
flag = 1

que1 = []
que2 = []
que3 = []
stack = []


while True:
    
    
    if num >= len(tons) and len(stack) == 0:
        break
    if num < len(tons) and flag == 1:
        i = tons[num]
        num+=1
        flag = 0
    elif num >= len(tons):
        i = 0
    
    print('next : ' + str(i))

    print("==================")
    print(time)
    print(que1)
    print(que2)
    print(que3)
    print(stack)
    time+=1

    if i != 0:
        if sum(stack)+i <= 10 and len(stack)+1 <= 3:
            stack.append(i)
            flag = 1

            if len(que3) == 0:
                que3.append(i)
            elif len(que2) == 0:
                que2.append(i)
                if len(que3) != 2:
                    que3.insert(0,0)
            elif len(que1) == 0:
                que1.append(i)
                if len(que2) != 2:
                    que2.insert(0,0)

        else:
            if len(que1) == 1:
                que1.insert(0,0)
            elif len(que1) == 2:
                print('out : '+ str(que1[1]))
                stack.pop()
                que1 = []
            elif len(que1) == 0 and len(que2) == 2:
                print('out : '+ str(que2[1]))
                stack.pop()
                que2 = []
            elif len(que1) == 0 and len(que3) == 2:
                print('out : '+ str(que3[1]))
                stack.pop()
                que3 = []
                time-=1

            if len(que2) == 1:
                que2.insert(0,0)

            if len(que3) == 1:
                que3.insert(0,0)

    else:
        if len(que1) == 1:
            que1.insert(0,0)
        elif len(que1) == 2:
            print('out : '+ str(que1[1]))
            stack.pop()
            que1 = []
        elif len(que1) == 0 and len(que2) == 2:
            print('out : '+ str(que2[1]))
            stack.pop()
            que2 = []
        elif len(que1) == 0 and len(que3) == 2:
            print('out : '+ str(que3[1]))
            stack.pop()
            que3 = []
    print("==================")
    print()
    

print("==================")
print(time)
print(que1)
print(que2)
print(que3)
print(stack)
print("==================")
print()
print('total time : ' + str(time))