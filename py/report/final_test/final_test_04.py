price = []

while True:
    x = int(input())
    if x == 0:
        break
    price.append(x)

big = 0
small = price[0]
resert = 0

for i in price:
    
    if i < big:
        small = i
        continue
    elif i > big:
        big = i
    
    if resert < big - small:
        resert = big - small

print(resert)