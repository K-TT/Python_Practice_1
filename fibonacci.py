def fib(n):
   a=1
   b=2
   fibList=[a,b]

   if n>2:
       for x in range (n-2):
           c=a+b
           fibList.append(c)
           a=b
           b=c


   print("The first "+str(n)+" elements of Fibonacci sequence:")     
   print(fibList)     
           
       
if __name__== "__main__" :
	    
        print(fib(5))
        print(fib(10))
        print(fib(20))
   
