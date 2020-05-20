n=int(input("number of terms"))
n1=0
n2=1
count=0
if n<=0:
    print("enter a positive integer")
elif n==1:
    print("fibonacci series upto")
    print(n1)
else:
    print("fibonacci series")
    while count<n:
        print(n1)
        terms=n1+n2
        n1=n2
        n2=terms
        count+=1
