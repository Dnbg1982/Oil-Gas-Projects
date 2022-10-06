import streamlit as st
import pandas as pd
st.title ('Decay Well Production Predicted by Machine Learning')
st.text('Data was gather from Kaggle Datasets')

st.markdown('#### This is a web app to make predictions of well-production using Machine Learning instead of Curve Decay Formula')

data = pd.read_csv(r'C:\Users\USUARIO\Documents\GitHub\Oil-Gas-Projects\API Oil Production\Datasets\Oil_prod_curve.csv')
st.write(data.describe())

formation_dist = data.formation.value_counts()
st.bar_chart(formation_dist)