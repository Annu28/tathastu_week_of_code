n=int(input('Enter the number of elements'))
dr=list(map(int,input('Enter elements seprated by space').split()))
odd=[]
even=[]
for i in dr:
    if i%2==0:
       even.append(i) 
    else:
        odd.append(i)
end=sorted(odd)[::-1]
even=sorted(even)
for i in even:
    end.append(i)
print(end)
