num = int(input())

five = num // 500
num %= 500
hund = num //100
num %= 100
fi = num // 50
num %= 50
ten = num // 10
num %= 10
print(five, hund, fi, ten, num)
