#This python module contains the visualization routines for California housing ML data set
#
#Steven Large
#October 17th 2017

import matplotlib.pyplot as plt

#from pandas.tools.plotting import scatter_matrix
from pandas.plotting import scatter_matrix

def PandaHistogram(Data, FileName = "NONE", Show = True): 		#Default filename will not write the resulting graph to file, and default will show plot

	Data.hist(bins=50, figsize=(20,15))
	if FileName != "NONE":
		plt.savefig(FileName)
	
	if Show == True:
		plt.show()
		plt.close()


def LongLatPlot(Data, FileName = "NONE", Show = True): 						#This routine plots the data as longitude vs latitude 

	Data.plot(kind = "scatter", x = "longitude", y = "latitude", alpha = 0.4, s = Data["population"]/100, label = "population", figsize = (10,7), c = "median_house_value", cmap = plt.get_cmap("jet"), colorbar = True)
	plt.legend()
	if FileName != "NONE":
		plt.savefig(FileName)

	if Show == True:
		plt.show()
		plt.close()


def PlotCorrMatrix(Data, FileName = "NONE", Show = True):

	Attributes = ["median_house_value","median_income","total_rooms","housing_median_age"]
	scatter_matrix(Data[Attributes], figsize = (12,8))
	if FileName != "NONE":
		plt.savefig(FileName)

	if Show == True:
		plt.show()
		plt.close()


def PlotMedianIncomeCorrMatrix(Data, FileName = "NONE", Show = True):

	Data.plot(kind = "scatter", x = "median_income", y = "median_house_value", alpha = 0.1)
	if FileName != "NONE":
		plt.savefig(FileName)

	if Show == True:
		plt.show()
		plt.close()

