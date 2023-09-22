dic = { 1 : list(), 2 : list(), 3 : list()}

for i in range(3):
    for j in range(3):
        dic[i+1].append(int(input()))
x = int(input())
temp = sorted(dic[x])
dic[x] = temp
print(dic[x],dic[x][2],dic[x][0])