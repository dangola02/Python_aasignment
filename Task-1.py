def toString(a):
	return ''.join(a)

def permute(a, l, r):
	if l == r:
		print(toString(a))
	else:
		for i in range(l, r + 1):
			a[l], a[i] = a[i], a[l]
			permute(a, l + 1, r)
			a[l], a[i] = a[i], a[l]

# Main
string = input("enter letters divided by comma ")
y=string.split(',')
n = len(y)
permute(y, 0, n-1)