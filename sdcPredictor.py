import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

import io
import requests

poly_reg = PolynomialFeatures(degree = 4)
lin_reg2 = LinearRegression()

class SdcPredictor(object):
	"""docstring for SdcPredictor"""
	def __init__(self, salary = 0):
		
		# lin_reg = LinearRegression()		
		# lin_reg.fit(X, y)

		# self.regr
		self.importData()
		self.fit()

		self.salary = salary
	
	def importData(self):
		#importing dataset

		url     = "https://raw.githubusercontent.com/gurjeetsdc/sdcml/master/data/Position_Salaries.csv"
		s       = requests.get(url).content
		print(s)
		dataset = pd.read_csv(io.StringIO(s.decode('utf-8')))
		#dataset = pd.read_csv("https://github.com/gurjeetsdc/sdcml/blob/master/data/Position_Salaries.csv")

		X = dataset.iloc[:,1:2].values
		y = dataset.iloc[:,-1].values
		self.X = X
		self.y = y;

	def fit(self):
		self.X_poly = poly_reg.fit_transform(self.X)
		lin_reg2.fit(self.X_poly, self.y)

	def predict( self, exp = 1 ):
		result = lin_reg2.predict( poly_reg.fit_transform(exp))
		return result
		

	def getX(self):
		return self.X

	def gety(self):
		return self.y

	def addSalary(self, salary):
		self.salary += salary

	def getSalary(self):
			return self.salary				