import numpy as np

if __name__ == "__main__":
	'''
	This will create a 3x3 numpy array object like so:
	
	1 2 3
	4 5 6
	7 8 9
	 
	'''
	a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


	'''
	This will get the third row of values 
	[get list @ index 2, get all values in this list] 
	so b = [4,5,6]
	'''
	b = a[2, :]



	'''
	This will flatten the array a to a 1d array with all of the values
	so c = [1,2,3,4,5,6,7,8,9]
	'''
	c = a.reshape(-1)


	'''
	this will create a 5x1 vector of random floating point numbers randomly sampled from
	a normal distrobution
	'''
	f = np.random.randn(5, 1)


	'''
	f>0 will create a boolean array where every element is compared 
	to 0 those that are greater will have true at that index those that are less will
	have false. A numpy array can be indexed by booleans where any index that
	is true in the boolean array will have a coresponding value appear in the
	resultant array. So g will contain any values in f that mee the condition 
	f>0
	'''
	g = f[f > 0]


	'''
	zeros will create a vector of zeros with length 10 the addition will add .5 to 
	all values in the vector so the result will be a vector containing 10 0.5 floats
	'''
	x = np.zeros(10) + 0.5


	'''
	this will create a vector of ones whose size will be the length of another vector x so in
	this case 10. It will then perform scalar multiplication on the vector. The result will
	be a vector of length 10 containing all 0.5 floats
	'''
	y = 0.5 * np.ones(len(x))


	'''
	This will perform vector addition between x and y the result will be a vector of length 10
	containing all 1s.
	'''
	z = x + y


	'''
	this will create an array that spans the range 1 to 100 [exclusive] 
	with a default step size of 1 so [1,2,3,..99].
	'''
	a = np.arange(1, 100)

	'''
	The slice notation is as follows list[<start>:<stop>:<step>]
	By default this will span the entire list if no args are given
	the step of minus 1 will step backwards through the list reversing it
	
	refecerenced:
	https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python#:~:text=The%20notation%20that%20is%20used,stop_index%3E%2C%20%5D
	'''
	b = a[::-1]


	'''
	given 1 argument this function will create a vector with range 0 to n-1 and randomly permute 
	[shuffle] all of the values in the generated array. If given an array it would shuffle it. so
	in this case we create a vector [0,1,2,..9] and randomly permute it
	'''
	c = np.random.permutation(10)



	########################part b################################################

	#1
	y = np.array([1, 2, 3, 4, 5, 6])
	z = y.reshape(3,2)

	#2
	x = np.max(z)
	r,c = np.where(z==x)
	r = r[0]
	c = c[0]

	#3
	v = np.array([1, 8, 8, 2, 1, 3, 9, 8])
	x = np.count_nonzero(v == 1)

	#4
	n = 4
	DiceRolls = np.random.randint(1,7,size = n)




	##################################part c########################################

