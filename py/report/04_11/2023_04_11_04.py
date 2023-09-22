Str1 = list(input())
Str1 = set(Str1)
Str2 = list(input())
Str2 = set(Str2)
set1 = Str1^Str2
Str3 = list(set1)
print(sorted(Str3,reverse=True))