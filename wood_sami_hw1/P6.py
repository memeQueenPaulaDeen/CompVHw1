import cv2
import math
import numpy as np


class Kernal:

	def __init__(self,N,sigma):
		self.N = N
		self.sigma = sigma
		self.frontBit = 1 / (sigma ** 2 * 2 * math.pi)
		self.k = np.zeros((N, N))
		self.idxMin = int(N / 2)
		for i in range(N):
			for j in range(N):
				x, y = self.getXYfromIDX(i, j)
				self.k[i, j] = self.frontBit * math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))



	def getXYfromIDX(self,i,j):
		x = i-self.idxMin
		y = j-self.idxMin
		return x, y


class Image:

	paddingOffset = None

	def __init__(self,fpath):
		self.image = cv2.imread(fpath, 0) #np.array([[1,2,3],[4,5,6],[7,8,9]])#
		self.height = len(self.image)
		self.width = len(self.image[0])

	def setPadding(self,width):

		#from numpy docs @ https://numpy.org/doc/stable/reference/generated/numpy.pad.html
		def pad_with(vector, pad_width, iaxis, kwargs):
			pad_value = kwargs.get('padder', 10)
			vector[:pad_width[0]] = pad_value
			vector[-pad_width[1]:] = pad_value

		padded = np.pad(self.image, width, pad_with, padder=0)
		self.paddingOffset = width
		self.padded = padded




	def convolve(self,k):
		#thankfully kernal is symetric so no flipy bois
		for r in range(self.height):
			#print(r)
			for c in range(self.width):
				cellVal= 0
				for y in range (k.N):
					for x in range(k.N):
						cellVal += self.padded[r+x,c+y] * k.k[x,y]
				self.image[r,c] = cellVal
		# print("plz")
		# print(self.image)



if __name__ == '__main__':
	fpath = 'inputP6.jpg'

	I1 = Image(fpath)
	kern = Kernal(5, 1.414)
	I1.setPadding(kern.idxMin)
	cv2.imshow("preconvolve", I1.image)
	I1.convolve(kern)
	cv2.imshow("postconvolve3", I1.image)


	cv2.waitKey(0)