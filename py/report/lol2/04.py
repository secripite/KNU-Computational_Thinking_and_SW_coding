list1 = [[0 for _ in range(4)] for _ in range(4)]

list2 = []

answer = []

for i in range(4):
    for j in range(4):
        x = int(input())
        if x == -99:
            list2.append([i,j])
        list1[i][j] = x

total = 0
num = 0
for i in range(4):
    if num == 4:
        break
    for j in range(4):
        if num == 4:
            break

        if list1[i][j] == -99:
            total = 0
            num = 0
            break
        else:
            total+=list1[i][j]
            num+=1


if (sum(list1[list2[0][0]])+99)>0:
    answer.append(total-(sum(list1[list2[0][0]])+99))
    list1[list2[0][0]][list2[0][1]] = answer[0]
else:
    answer.append(total-(list1[0][list2[0][1]]+list1[1][list2[0][1]]+list1[2][list2[0][1]]+list1[3][list2[0][1]]+99))
    list1[list2[0][0]][list2[0][1]] = answer[0]

if (sum(list1[list2[1][0]])+99)>0:
    answer.append(total-(sum(list1[list2[1][0]])+99))
    list1[list2[1][0]][list2[1][1]] = answer[1]
else:
    answer.append(total-(list1[0][list2[1][1]]+list1[1][list2[1][1]]+list1[2][list2[1][1]]+list1[3][list2[1][1]]+99))
    list1[list2[1][0]][list2[1][1]] = answer[1]

if (sum(list1[list2[2][0]])+99)>0:
    answer.append(total-(sum(list1[list2[2][0]])+99))
    list1[list2[2][0]][list2[2][1]] = answer[2]
else:
    print(list2[2][1])
    answer.append(total-(list1[0][list2[2][1]]+list1[1][list2[2][1]]+list1[2][list2[2][1]]+list1[3][list2[2][1]]+99))
    list1[list2[2][0]][list2[2][1]] = answer[2]

if (sum(list1[list2[3][0]])+99)>0:
    answer.append(total-(sum(list1[list2[3][0]])+99))
    list1[list2[3][0]][list2[3][1]] = answer[3]
else:
    answer.append(total-(list1[0][list2[3][1]]+list1[1][list2[3][1]]+list1[2][list2[3][1]]+list1[3][list2[3][1]]+99))
    list1[list2[3][0]][list2[3][1]] = answer[3]


print(answer)