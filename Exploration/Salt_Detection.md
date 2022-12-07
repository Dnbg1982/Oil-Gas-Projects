# Salt Detection Using Neural Networks
Salt bodies bounce sound waves erratically becoming one of the main issues in seismic surveys. Characterization of this bodies is extremely difficult due to complex shapes and unpredicted changes in impedance and velocity. Therefore, to help geologists identify salt bodies more accurately, I built a machine learning model based on deep learning.

   ![image](https://user-images.githubusercontent.com/100526221/205788477-679e9699-720d-463e-a952-ba7d480b90b9.png)

GOAL
------------------------------------------------------------------------------------------------------------------------
Differentiate the part of subsurface which is salt.

DATA
------------------------------------------------------------------------------------------------------------------------
The set of images was gotten from Kaggle Salt Detection Competition. Images were chosen in various locations at random subsurface spots. (https://www.kaggle.com/competitions/tgs-salt-identification-challenge/data)

EVALUATION
------------------------------------------------------------------------------------------------------------------------
Model was evaluated on the mean average precision at different intersection over union (IoU) thresholds.

VISUALIZATION
------------------------------------------------------------------------------------------------------------------------
Training dataset was explored where mask recognize salt bodies in a sample of 20 random images.
![image](https://user-images.githubusercontent.com/100526221/206059385-1342379c-54c3-447b-b88e-37c9bdeec66a.png)


MODEL BREAKDOWN
------------------------------------------------------------------------------------------------------------------------
