def prime(num):
    arr =[]
    n=2
    while True:
        if num % n == 0:
            arr.append(n)
            num /= n
        else:
            n+=1
        if n >num:
            break

    return arr

if __name__ == '__main__':
    print(prime(int(input())))