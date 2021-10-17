#1,1,2,3,5,8,13
# equation f=f(x-1)+f(x-2)
#kind of like fibonecci but childs are multiply by a factor

def rec(month,offspring):
	parent=1
	child=1
	for i in range(month-1):
		# temp=new
		# new=old
		# old=temp+old
		#or 
		child,parent=parent,parent+(child*offspring)
		#or recursion
		print(child)

rec(31,2)



# print(rec1(5,3))
