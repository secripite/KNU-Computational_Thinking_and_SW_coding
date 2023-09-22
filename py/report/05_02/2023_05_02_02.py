def measure(a):
    i = 2
    arr=[]
    while i*2<=a:
        if a%i==0:
            arr.append(i)
        i+=1
    return(arr)
    
print(measure(int(input())))
