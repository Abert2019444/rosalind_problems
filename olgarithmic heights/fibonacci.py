#prints the the number on the fibonacci seq which n correspond to.
def f(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		return f(n-1)+f(n-2)
print(f(24))
