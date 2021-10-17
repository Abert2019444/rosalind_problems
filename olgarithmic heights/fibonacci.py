#prints the the number on the fibonacci seq which n correspond to.
def f(x):
	if x==0:
		return 0
	if x==1:
		return 1
	else:
		return f(x-1)+f(x-2)
print(f(24))
