# Seismic Inversion Using XGBoost
Seismic inversion converts original reflectivity data, as typically recorded routinely, from an interface property to a rock property known as impedance, which itself is the multiplication of sonic velocity and bulk density. Most oil and gas companies now use seismic inversion to increase the resolution and reliability of the data and to improve estimation of rock properties including porosity and net pay.

GOAL
-------------------------------------------------------------------------------------------------------------------------------------
Using well logs seismic inversion was perform in order to make a better estimation of rock attributes.

DATA
-------------------------------------------------------------------------------------------------------------------------------------
Data used in this project came from open data (3D Poseidon from Australia). Seismic acquisition in 2009 by ConoPhilips.

EVALUATION
-------------------------------------------------------------------------------------------------------------------------------------
- MAE = (1/n) * Σ|yi – xi|
- R^2 = coefficient of determination \ RSS = sum of squares of residuals \ TSS = total sum of squares \
- ME: maximum residual error

VISUALIZATION
-------------------------------------------------------------------------------------------------------------------------------------
Plotting well features taking 6 wells as sample.
![image](https://user-images.githubusercontent.com/100526221/207198547-97f5a645-9dd2-4102-aa90-063051cef26f.png)

MODEL BREAKTHROUGH
-------------------------------------------------------------------------------------------------------------------------------------
