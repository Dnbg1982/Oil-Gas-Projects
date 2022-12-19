# Oil Production Forecasting Using XGBoost Competition By Kaggle
Appraisal phase could be one of the most important stage in oil industry. Since, here is where feasibility of a project based on field's oil production. To determine how many barrels reservoir engineers use a formula to estimate decay curve of production. However,  could machine learning approach do abbeter job?

GOAL
---------------------------------------------------------------------------------------------------------------------------------------------------
Predict the first three years cum of a producing well starting from peak of production.

DATA
---------------------------------------------------------------------------------------------------------------------------------------------------
- Harmony_data.csv - file contains a batch of features for both the training and test sets
- IHS_data.csv - file contains another batch of features for both the training and test sets
- test_APIs.csv - contains list of APIs you'll use for the test set
- sampleSubmission.csv - a sample submission file in the correct format
- production_data_train.csv - production data for the training set
- production_data_test.csv - production data for the test set

EVALUATION
-----------------------------------------------------------------------------------------------------------------------------------------------------
Models are evaluated using the mean absolute error between the predicted and actual three years cumulative production. MAE measures the average magnitude of the errors in a set of predictions, without considering their direction.

MODEL BREAKDOWN
----------------------------------------------------------------------------------------------------------------------------------------------------
1. Explore data and check null values.
2. Compare number of wells in the different datasets.
3. Map well features into train and data sets
4. Plot oil production of some random wells.

![image](https://user-images.githubusercontent.com/100526221/208330597-8901761b-4b70-400f-b6c1-a4a8e6cfad9e.png)
5. Transform features into categorical variables
6. Sort by values by descending date, filter data to start from the peak adn drop NaN.
7. Splitting data into train and test sets.
8. Building models using ARIMA and XGBoost.
9. Feature importance.

![image](https://user-images.githubusercontent.com/100526221/208330835-b72f9409-9fa2-4184-ab89-9888631ced9b.png)
10. Forecast and validate visualizing the results.

![image](https://user-images.githubusercontent.com/100526221/208330891-5341fdd6-d0f3-4bcc-9ab3-2e110907a5b1.png)

 
