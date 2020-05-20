num = int(input("Enter the Value of n: "))
for i in range(num):
    print((str(num - i) + "*") * (num - 1 - i) + str(num - i))
for i in range(1,num + 1):
    print((str(i) + "*") * (i - 1) + str(i))
