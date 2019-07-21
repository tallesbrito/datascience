import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

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
#x = [(-1, 1),(0, -1),(10, 1)]
#y = [1,-1,1]

x = [(-1, 1),(0, -1),(10, 1),(7,3),(-2,4),(3,3),(-2,3)]
y = [-1,-1,1,1,-1,1,-1]

outputs = [perceptron(w,e,b) for e in x]
size = len(y)
turn = 0

maxiterations = 1000
iterations = 0

while not vecequal(y,outputs) and iterations<maxiterations:
	print(turn,w,b)
	print(y,outputs)
	
	outputs[turn] = perceptron(w,x[turn],b)
	if  outputs[turn] != y[turn]:
		w = vecsum(w,scalarproduct(y[turn],x[turn]))
		b = b + y[turn]
	
	turn = (turn + 1) % size
	iterations+=1

print("CONVERGENCE REACHED!")
print(turn,w,b)
print(y,outputs)

def color(v):
	if v==1:
		return 'b'
	elif v==-1:
		return 'r'
	else:
		return 'k'

maxcoord = max(max(x)) + 5
plt.xlim(-maxcoord, maxcoord)
plt.ylim(-maxcoord, maxcoord)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.quiver(0,0,w[0],w[1],angles='xy',scale_units='xy', scale=1)

for i,pair in enumerate(x):
	plt.scatter(pair[0], pair[1], color=color(y[i]));

if w[1]!=0:
	xline = np.linspace(-maxcoord, maxcoord, 100)
	yline = [(-b-w[0]*e)/w[1] for e in xline]
else:
	xline = [-b/w[0]] * 100
	yline = np.linspace(-maxcoord, maxcoord, 100)

plt.plot(xline, yline);

plt.show();
