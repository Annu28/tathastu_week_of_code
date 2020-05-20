def Pri(N):
    a = 2
    k = N // 2
    while k >= a:
        if N % a == 0:
            return False
        a += 1
        k = N // a
    return True

def Pallindrome(n):
    N = str(n)
    L = len(N)
    for i in range(L // 2):
        if N[i] != N[L - 1 - i]:
            return False
    return True

def odd(n):
    if n % 2 == 0:
        return False
    return True

def Armstrong(num):
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10
        sum += digit ** 3  
        temp //= 10  
    if num == sum:  
        return True 
    return False

def ABC():
    number = int(input("Enter the number: "))
    if(Pri(number)):
        print("number is a prime number")
    if(odd(number)):
        print("number is an odd number")
    else :
        print("number is an even number")
    if(Pallindrome(number)):
        print("number is a pallindrome number")
    if(Armstrong(number)):
        print("number is an armstrong number")

ABC()
