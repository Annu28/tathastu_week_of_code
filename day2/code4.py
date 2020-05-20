n=int(input("enter number"))
for i in range(2*n-1):
    if(i<n):
        print('*'*(n-i)+' '*2*i+'*'*(n-i))
    else:
        print('*'*(i-n+2)+' '*(4*(n-1)-2*i)+'*'*(i-n+2))
