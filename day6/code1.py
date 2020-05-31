def abc(str): 
	n = len(str)  
	b = [[0 for x in range(n)]for y in range(n)] 
	for i in range(n): 
		b[i][i] = 1
	for cl in range( 2, n+1): 
		for i in range(n - cl + 1): 
			j = i + cl - 1
			if (str[i] == str[j] and cl == 2): 
				b[i][j] = 2
			elif (str[i] == str[j]): 
				b[i][j] = b[i + 1][j - 1] + 2
			else: 
				b[i][j] = max(b[i][j - 1],b[i + 1][j]) 
	return b[0][n - 1] 
def minimumNumberOfDeletions( str): 
	n = len(str) 
	b = abc(str)  
	return (n - b) 

if __name__ == "__main__": 
	str=input("Enter the String: ")
	print( "Minimum number of deletions required = ", minimumNumberOfDeletions(str))
