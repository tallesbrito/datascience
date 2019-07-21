def vecsum(a,b):
	return [e1 + e2 for e1,e2 in zip(a,b)]

def scalarproduct(c,a):
	return [c*e for e in a]

def dotproduct(a,b):
	return sum([e1*e2 for e1,e2 in zip(a,b)])

def perceptron(w,x,b):
	out = dotproduct(w,x) + b
	if out == 0:
		return 0
	elif out > 0:
		return 1
	elif out < 0:
		return -1

def vecequal(a,b):
	return all([e1 == e2 for e1,e2 in zip(a,b)])

b = 0
w = [0,0]
x = [(-1, 1),(0, -1),(10, 1)]
y = [1,-1,1]
outputs = [perceptron(w,x[0],b),perceptron(w,x[1],b),perceptron(w,x[2],b)]
size = len(y)
turn = 0

while not vecequal(y,outputs):
	print(turn,w,b)
	print(y,outputs)
	
	outputs[turn] = perceptron(w,x[turn],b)
	if  outputs[turn] != y[turn]:
		w = vecsum(w,scalarproduct(y[turn],x[turn]))
		b = b + y[turn]
	
	turn = (turn + 1) % size
	raw_input("Press Enter to continue...")

print("CONVERGENCE REACHED!")
print(turn,w,b)
print(y,outputs)
