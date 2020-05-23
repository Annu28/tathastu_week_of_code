def add(coll, size,sum):
    addcoll = []
    if size == 1:
        for x in coll:
            addcoll.append(sum + x)
        return addcoll
    L2 = list(coll)
    for x in coll:
        L2.remove(x)
        addcoll.extend(add(L2,size-1,sum + x))
    return addcoll

def addi(coll,size):
    addcoll = list(coll)
    for i in range (2, size + 1):
        addcoll.extend(add(List,i,0))
    number = 1
    while True:
        if number not in addcoll:
            print("The least integer which is not present in the list and also cannot be represented as the addition of sub-elements is",number)
            break
        number += 1

size = int(input("Enter the no of elements in the list: "))
coll = []
print("Enter the elements in list.")
for i in range(size):
    coll.append(int(input()))
addi(coll, size)
