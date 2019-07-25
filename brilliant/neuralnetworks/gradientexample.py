def vecsum(a,b):
	return [e1 + e2 for e1,e2 in zip(a,b)]

def scalarproduct(c,a):
	return [c*e for e in a]

v = 0.01
wi	= [1,0]
i = 0

while wi != [0,0] and i<100:
	wi = vecsum(scalarproduct(-v,wi),wi)
	print(wi)
	i+=1

print("steps:")
print(i)

