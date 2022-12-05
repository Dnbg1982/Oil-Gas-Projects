# Lithofacies Classification Competition Kaggle
Facies characterization in the rock is significant for exploration phase and estimation of reservoir production. Specialists spend hundreds of hours examining rock properties in order to label different layers. An incorrect classification could cost millions and project failure. Hence, machine learning model could colaborate petroleum professionals determining the facies faster and more accurate.

![image](https://user-images.githubusercontent.com/100526221/204417041-44d0164c-e68b-47c0-9684-28bacb509f82.png)

GOAL
--------------------------------------------------------------------------------------------------------------------------
Making Lithofacies Classification Model Using ML Algorithms

DATA
--------------------------------------------------------------------------------------------------------------------------
Datasets was taken from FORCE 2020 Competition organized by Canadian Well Logging Society CWLS 

EVALUATION
-------------------------------------------------------------------------------------------------------------------------
Evaluation will be done with a penalty matrix given by the competition. Given the dataset is not balanced we could use F1-score or Recall to evaluate model performance.

PROJECT BREAKDOWN
-------------------------------------------------------------------------------------------------------------------------
1. Some datasets were explored, not only the competitor, but also different .las files to understand the structure of the data and how the log data is collected. Therefore, the lassio and welly libraries were used.

2. Data Preprocessing
   - Data was evaluated with pandas profiling.
   - For uniform and smooth preprocesing datasets given were concatenated.
   - Drop columns which were not going to be used and fill na values.
   - Get sample to train the model (Since my computer power I diminished the number of wells choosing random wells to train the model).

3. Data Visualization
   - Visualize data distribution to look how different classes were balanced.

4. Building Model
  - Split the preporcessed data into X and Y
  - Function was made to evaluate model performance.
  - Different algorithms were used XGBosst, RandomForest and KNN

5. Improving model
  - Data augmentation
  - Parameters were tuned using RandomizedSEarch CV

RESULTS
-------------------------------------------------------------------------------------------------------------------------
Current best matrix score from XGBoost 
Contest metric: 0.6 ( -0.79 )
