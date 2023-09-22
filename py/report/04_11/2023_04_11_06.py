dic = {'a':7,'b':9,'c':11,'d':13,'e':3,'f':20,'g':5,'h':30,'i':2,'j':5}

s = input()
n = 0
for i in range(len(s)):
    n += dic[s[i]]

print(n/len(s))