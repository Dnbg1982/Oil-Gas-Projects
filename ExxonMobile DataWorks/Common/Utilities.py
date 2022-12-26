""" Library Import put on the top"""
import pandas as pd

"""
#
# This file consist of the essential functions to run the program.
# Please dont change any of this functions
#
"""

def getCompleteDataset():
    return pd.read_csv("../Dataset/complete_well_data.csv")

def getTrainDataset():
    return pd.read_csv("../Dataset/train_well_data.csv")
    
def getTestDataset():
    return pd.read_csv("../Dataset/test_well_data.csv")



"""
#
# Teams, please add your code below. 
#
"""


