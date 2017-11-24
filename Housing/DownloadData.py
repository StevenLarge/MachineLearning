#This python script imports the California housing data for input into a ML optimization scheme
#
#Steven Large
#October 17th 2017

import os
import tarfile
import pandas as pd
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "DataSet/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def FetchHousingData(HousingURL=HOUSING_URL, HousingPath=HOUSING_PATH):

	if not os.path.isdir(HousingPath): 									#Create the directory if it doesn't exist
		os.makedirs(HousingPath)

	tgz_Path = os.path.join(HousingPath, "housing.tgz") 				#Writepath for the data
	urllib.request.urlretrieve(HousingURL, tgz_Path)					
	Housing_tgz = tarfile.open(tgz_Path)
	Housing_tgz.extractall(path = HousingPath)
	Housing_tgz.close() 


def LoadHousingData(HousingPath = HOUSING_PATH):
	
	csv_path = os.path.join(HousingPath, "housing.csv")
    
	return pd.read_csv(csv_path)


