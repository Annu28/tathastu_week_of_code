n=int(input('Enter size of dictionary'))
dic={}
dicnew={}
for i in range(n):
    key=int(input('Enter the '+str(i+1)+'key'))
    value=int(input('Enter the '+str(i+1)+'value'))
    dic[key]=value
    if( dic[key] not in list(dicnew.values())):
        dicnew[key]=value
print(dicnew)
