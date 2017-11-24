#This python module creates a test set from the California housing data
#
#Steven Large
#October 17th 2017

import numpy as np
import hashlib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit


def SplitTrainTest(Data, testRatio):
	
	ShuffledIndices = np.random.permutation(len(Data))
	TestSetSize = int(len(Data)*testRatio)
	TestIndices = ShuffledIndices[:TestSetSize]
	TrainIndices = ShuffledIndices[TestSetSize:]

	return data.iloc[TrainIndices], data.iloc[TestIndices]


def TestSetCheck(Identifier, testRatio, hash):

	return hash(np.int64(Identifier)).digest()[-1] < 256*testRatio


def SplitTrainSet_ByID(Data, testRatio, ID_Column, hash = hashlib.md5):

	IDs = Data[ID_Column]

	inTestSet = IDs.apply(lambda id_: TestSetCheck(id_, testRatio, hash))

	return Data.loc[~inTestSet], Data.loc[inTestSet]


def SplitTrainTest_SkLearn(testSize, Data, RandomState):

	TrainSet, TestSet = train_test_split(Data, test_size=testSize, random_state=RandomState)

	return TrainSet, TestSet


def IncomeStratifiedSplitting(Data, testSize = 0.20, Modifier = "income_cat"):

	Data["income_cat"] = np.ceil(Data["median_income"] / 1.5)
	Data["income_cat"].where(Data["income_cat"] < 5, 5.0, inplace = True)

	split = StratifiedShuffleSplit(n_splits=1, test_size = testSize, random_state = 42)

	for train_index, test_index in split.split(Data, Data["income_cat"]):
		strat_train_set = Data.loc[train_index]
		strat_test_set = Data.loc[test_index]

	return strat_train_set, strat_test_set