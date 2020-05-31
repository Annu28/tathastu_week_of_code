n=int(input('Enter size of list'))
print('Enter elements of list seprated by space')
a=list(map(int,input('Enter elements').split()))
for i in range(len(a)-1):
    a[i]=max(a[i+1:])
print(a)
