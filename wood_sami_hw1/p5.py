import numpy as np
import matplotlib.pylab as plt


def createFile(path,DataSource):
	np.savetxt(path, DataSource, fmt='%d')

def getFreq(list):
	list = list.reshape(-1).tolist()
	freqDict = {}
	for x in list:
		freqDict[x] = list.count(x)
	return freqDict

if __name__ == '__main__':

	#1
	path = 'inputP5A.npy'
	DataSource = np.random.randint(1, 255, (100, 100))
	#createFile(path,DataSource)
	A = np.loadtxt('inputP5A.npy', dtype=int)
	f = getFreq(A)
	valueFreqList = sorted(f.items(), key=lambda x: x[1], reverse=True)
	print("Ordered Intensity List")
	print(valueFreqList)
	#valueFreqList = sorted(f.items())
	x, y = zip(*valueFreqList)  # unpack a list of pairs into two tuples
	#plt.plot(y)

	fig, ax = plt.subplots()
	scatter = ax.scatter(x , y, c=y)
	ax.legend(*scatter.legend_elements(),title='Frequency of value',bbox_to_anchor=(.9, .6),loc='center left')
	plt.title('sorted frequncy scatter')
	plt.xlabel('value')
	plt.ylabel('frequncy')
	plt.show()
	#fig1.savefig('Frequncy_VS_value_5_c_1.png')


	#2
	plt.hist(x, density=False, bins=20)
	plt.title('image value histogram 20 buckets')
	plt.xlabel('value')
	plt.ylabel('frequncy')
	plt.show()
	#fig2.savefig('Value_Histogram_5_c_2.png')


	#3
	x = [M for SubA in np.split(A,2, axis = 0) for M in np.split(SubA,2, axis = 1)][2]
	plt.matplotlib.pyplot.imshow(x,interpolation='none')
	plt.title('matrix X 5.c.3')
	plt.show()
	#fig3.savefig('Left_Quad_5_c_3.png')
	path = 'outputP5X.npy'
	createFile(path,x)


	#4
	Y = A - np.mean(A)
	plt.matplotlib.pyplot.imshow(Y, interpolation='none')
	plt.title('matrix y 5.c.4')
	plt.show()
	#fig4.savefig('Average_Diffed_5_c_4.png')
	path = 'outputP5Y.npy'
	createFile(path,Y)

	#5
	Z = np.ones((100,100))*255
	Z[A <= np.mean(A) ] = 0
	Z = [[red,0,0] for row in Z for red in row]
	Z = np.array(Z, dtype=np.uint8).reshape((100, 100, 3))
	plt.matplotlib.pyplot.imshow(Z, interpolation='none')
	plt.title('matrix z 5.c.5')
	plt.show()
	plt.matplotlib.pyplot.imshow(Z, interpolation='none')
	plt.title('matrix z 5.c.5')
	plt.savefig('outputP5Z.png')


	print()



	#####references

	'''
	https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
	https://stackoverflow.com/questions/37266341/plotting-a-python-dict-in-order-of-key-values/37266356
	https://stackoverflow.com/questions/12811981/slicing-python-matrix-into-quadrants
	'''