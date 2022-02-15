def fact3(n):
	if n<=1:
		return 1
	else:
                
		return n*fact3(n-1)

if __name__== "__main__" :
        print(fact3(5))
