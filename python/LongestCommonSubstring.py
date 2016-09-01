#longest common substring has many application. In web search, if we find the 
#smallest number changes that are needed to change the one word into another
#A change here is an insertion , deletion or replacement.

def LCSLength(X,Y):
	if not X or not Y:
		return ""
	
	x,m,y,n = X[0],X[1:],Y[0],Y[1:]
	
	if x == y:
		return x + LCSLength(m,n)
	else:
		return max(LCSLength(X,n),LCSLength(m,Y),key=len)
	
print LCSLength("hello","monu")