""" Library Import put on the top"""
import pickle 


"""
#
# This file consist of the essential functions to run the program.
# Please dont change any of this functions
#
"""

def saveModel(model, filename):
    pickle.dump(model, open(f'ModelArchive/{filename}','wb'))

def loadModel(filename):
    return pickle.load(open(f'ModelArchive/{filename}','rb'))


"""
#
# Teams, please add your code below. 
#
"""


