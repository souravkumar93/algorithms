if __name__ == '__main__':
	list = [2,3,4,5,67,7,8,9,2,45,46,5]
	temp = []
	temp.push(list[0])
	i = 1
	while(len(temp) > 0):
        next=list[i]
		top = temp.pop()
		if next > top
		  print('next greater element of '+ str(top) + " --- "+ str(next))
        else:
            temp.push(next)
			i++