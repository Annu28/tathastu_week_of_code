def PER(string,step=0):
    if step == len(string):
        print("".join(string))
    for i in range(step,len(string)):
        string_copy=[c for c in string]
        string_copy[step],string_copy[i]=[i],string_copy[step]
        PER(string_copy,step+1)
print(PER('one'))
        
