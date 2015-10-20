import numpy as np

def trace(Matrix):
	trace = 0
	for i in range(len(Matrix)):
		trace += Matrix[i,i]
	return trace

def main():
	M = np.array([[1,2],[3,4]])
	print trace(M)

if __name__ == '__main__':
	main()