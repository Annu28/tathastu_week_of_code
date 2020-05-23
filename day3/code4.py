def duplicate(collection):
    duplicatecollection = []
    for x in collection:
        if x not in duplicatecollection:
            duplicatecollection.append(x)
    return duplicatecollection

size = int(input("Enter the no of elements: "))
print("Enter the element")
collection = []
for i in range(size):
    collection.append(input())
print("collection after removing the duplicates is:", duplicate(collection))
