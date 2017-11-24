#This python module is the main driver routine completes the ML pipeline
#
#Steven Large
#October 18th 2017

import DownloadData
import Visualization
import InitializeTestSet
import WriteData
import Preprocessing

#---------------------------Download and Initialize Data--------------------------------#
# 								  October 20th 2017										#
#						Steven Large 			slarge@sfu.ca 							#
#---------------------------------------------------------------------------------------#


DownloadData.FetchHousingData() 			#Create DataSet directory and download data into it as a csv file

housing = LoadHousingData() 				#Import the data from csv into a pandas data structure

VisualizeData.PandaHistogram(housing,'Histogram.pdf',False)

#HousingTrain,HousingTest = InitializeTestSet.SplitTrainTest(housing, 0.20)

HousingTrain,HousingTest = InitializeTestSet.IncomeStratifiedSplitting(housing)

Visualization.LongLatPlot(housing,'GeoPlot.pdf',False)			#This is a coloured plot of the housing data in a longitude-latitude axes

CorrMatrix = housing.corr() 								#This is the correlation matrix for the housing data set

Visualization.PlotCorrMatrix(housing,'CorrelationMatrix.pdf',False)

Visualization.PlotMedianIncomeCorrMatrix(housing,'MedianIncomeScatter.pdf',False)


#Create new attributes

housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"] = housing["population"]/housing["households"]

housing2 = HousingTrain.drop("median_house_value", axis = 1) 							 			#Creates a copy of the data in "median housing value"
hosuing_labels = HousingTrain["median_house_value"].copy()

housing_tr = Preprocessing.CleanDataHoles(housing, "ocean_proximity") 								#Clean the data, by calculating the median of empty attribute cells

#-----------------------------Train and Optimize Model----------------------------------#
# 								  October 20th 2017										#
#						Steven Large 			slarge@sfu.ca 							#
#---------------------------------------------------------------------------------------#







#------------------------------Test and Evaluate Model----------------------------------#
# 						   		  October 20th 2017										#
#						Steven Large 			slarge@sfu.ca 							#
#---------------------------------------------------------------------------------------#










