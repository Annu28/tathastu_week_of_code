  
def Next(a,n): 
     for i in range(n-1,0,-1): 
         if a[i] > a[i-1]: 
             break
     if i == 1 and a[i] <= a[i-1]: 
         print "Next number not possible"
         return
     x = a[i-1] 
     smallest = i 
     for j in range(i+1,n): 
         if a[j] > x and a[j] < a[smallest]: 
             smallest = j
     a[smallest],a[i-1] = a[i-1], a[smallest] 
     x = 0
     for j in range(i): 
         x = x * 10 + a[j] 
     a = sorted(a[i:]) 
     for j in range(n-i): 
         x = x * 10 + a[j] 
     print "Next number with set of digits is",x 
dig = "534976"         
  
a = map(int ,dig)  
Next(a, len(dig)) 
