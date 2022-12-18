# Oil Price Prediction using ML
Oil is still one most important assets in the world. Therefore, oil prices  affect the economy of producer and consumer countries as well. Time series Machine Learning could help traders to find seasonal and stationary patterns of oil consumption change oil prices. Since, commodities prices vary depending on several factors such as wars, diseases among others it is extremely complicated to understand the price behaviour but at least predictable component can be understood with Machine Learning Techniques. 

GOAL
------------------------------------------------------------------------------------------------------------------------------------------
Use Time Series analysis to determine if there is some kind of pattern in how oil price move around the year.

DATA
------------------------------------------------------------------------------------------------------------------------------------------
- Crude oil prices per barrel back to 1946. The price of oil shown is adjusted for inflation using the headline CPI (https://www.macrotrends.net/1369/crude-oil-price-history-chart).
- Oil rents by country (https://data.worldbank.org/indicator/NY.GDP.PETR.RT.ZS).

MODEL BREAKTROUGH
-------------------------------------------------------------------------------------------------------------------------------------------
1. In Time Series is critical to determine key dates which change oil price dramatically as was mentioned before.
 Key Dates:
  - gulf_war = '1990-10-2'
  - attack_911 = '2001-9-11' 
  - fina_crisis = '2008-9-25'
  - peak_shale = '2014-6-20'
  - covid_19 = '2019-12-31'
  - war_rus_ukr = '2022-04-24'
  
  ![image](https://user-images.githubusercontent.com/100526221/208325085-67886d56-2e81-4c4a-9b09-e70180c71d0a.png)

2. Choose a date when the pattern seems stabilized (without great changes), to train the model.
3. Check for stationarity and seasonality.
4. Try different models changing number of moving average and autoregressive periods.
5. Evaluate residuals.
6. Do the same process with the returns.
7. Visualize prediction vs real values.
![image](https://user-images.githubusercontent.com/100526221/208325983-b055c192-0885-4300-a291-8a66df34db16.png)
