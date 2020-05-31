n=int(input('enter the size of tuple'))

t=tuple(map(int,input('enter element of tuple seprated by space:').split()))

dr=int(input('enter the element to find it occurence:'))

print(t.count(dr))
