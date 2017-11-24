#this python script contains the preprocessing and data preparation scripts for the California housing data
#
#Steven Large
#October 26th 2017

import pandas as pd
from sklearn.preprocessing import Imputer


#--------------- DATA CLEANING -----------------------

#Example -> bedrooms attribute has missing values in some cases, so what to do with those?
#
# housing.dropna(subset = ["total_bedrooms"]) 			--> first option, drop all data from the districts that have no entries for the data 
#
# housing.drop("total_berooms", axis=1)  				--> second option, drop the entire data set for total bedrooms
#
# median = housing["total_bedrooms"].median() 			--> thitd option, set the values to some value (the median)
#
# sklearn Imupter class also provides a way to deal with this (using the third option)
#
# CODE FOR THIS:

def CleanDataHoles(Data, EmptyAttribute):

	imputer = Imputer(strategy = "median")
	NewData = housing.drop(EmptyAttribute, axis = 1) 				#This line drops the ocean proximity from a copy of the data because we can only compute the median on numerical attributes
	imputer.fit(housing_num)

	TransformedData = imputer.transform(housing_num)

	CleanData = pd.DataFrame(X, columns = housing_num.columns())

	return CleanData

