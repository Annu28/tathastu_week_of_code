nlist=int(input('Enter the size of tuple list'))
ntuple=int(input('Enter the size of tuples'))
dr_list=[]
for i in range(nlist):
    t=tuple(map(int,input('Enter the element of tuple'+str(i+1)+' seprated by space:').split()))
    dr_list.append(t)
n=int(input('Enter index number of element about which you want to short list'))
for i in range(len(dr_list)):
    for j in range(i+1,len(dr_list)):
        if(dr_list[i][n]>dr_list[j][n]):
            dr_list[i],dr_list[j]=dr_list[j],dr_list[i]
print(dr_list)
