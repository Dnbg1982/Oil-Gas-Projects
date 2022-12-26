""" Library Import put on the top"""
import pandas as pd
from Common.Config import Tunable_PARAMETER



"""
#
# This file consist of the essential functions to run the program.
# Please dont change any of this functions
#
"""


def getSluggingClass(df, WHPFluctuationTreshold=None):
    """
    This function create the Slugging feature depending on WHPFluctuationTreshold as a treshold
    WHPFluctuationTreshold is tunable parameter to be optimised 
    """
    if WHPFluctuationTreshold is None:
        WHPFluctuationTreshold = Tunable_PARAMETER['WHP_FLUCTUATION_TRESHOLD']
    temp_df = df.copy()
    temp_df.loc[temp_df['WHP Fluctuation (%)'] <= WHPFluctuationTreshold,'SluggingClass'] = 'Non-Slugging'
    temp_df.loc[temp_df['WHP Fluctuation (%)'] > WHPFluctuationTreshold,'SluggingClass'] = 'Slugging'
    return temp_df


"""
#
# Teams, please add your code below. 
#
"""

