from tkinter import font
from sklearn.semi_supervised import LabelSpreading
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title ('Decay Well Production Predicted by Machine Learning')
st.text('Data was gather from Kaggle Datasets')

st.markdown('#### This is a web app to make predictions of well-production using Machine Learning instead of Curve Decay Formula')

data = pd.read_csv(r'C:\Users\USUARIO\Documents\GitHub\Oil-Gas-Projects\API Oil Production\Datasets\Oil_prod_curve.csv')
st.write(data.describe())

formation_dist = data.Basin_name.value_counts()
st.bar_chart(formation_dist)

st.header('Distribution Oil Production by Month')
fig, ax = plt.subplots(1,1)
sns.boxplot(data=data, x=data.Month_Ord, y=data.Oil)
ax.set_xlabel('Month', fontsize=8)
ax.set_ylabel('Oil Production', fontsize=8)
ax.set_xlim(-0.5,20.5)
ax.set_ylim(0,40000)
ax.tick_params(axis='y', labelsize=6)
ax.tick_params(axis='x', labelsize=6)
st.pyplot(fig)


sum_produ = data.groupby('API').sum()['Oil']
st.line_chart(sum_produ)

st.sidebar.title('Analytics')
st.sidebar.radio('SHEETS',options=['Home','Plots', 'Tables','Forecasting'])