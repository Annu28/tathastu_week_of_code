def sack(n, b):
    if n == 0 or len(b) == 0:
        return 0
    if len(b) == 1:
        if b[0][0] > n:
            return 0 
        return b[0][1]  
    if b[0][0] > n:
        return sack((n, b[1:]))
    return max(b[0][1] + sack(n - b[0][0], b[1:]), sack(n, b[1:]))
size =  int(input("Enter the number of items: "))
b = []
for i in range(size):
    n = int(input("Enter the weight for item number " + str(i + 1) + ": "))
    value = int(input("Enter the value for item number " + str(i + 1) + ": "))
    b.append((n,value))
n = int(input("Enter the value of weight capacity: "))
print("The maximum value of weight value pair is ", sack(n, b))
