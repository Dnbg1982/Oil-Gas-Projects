from tkinter import font
from tokenize import group
from sklearn.semi_supervised import LabelSpreading
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import numpy as np
import plotly.express as px

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

st.markdown('### Forecasting Model')
model = pickle.load(open(r'C:\Users\USUARIO\Documents\GitHub\Oil-Gas-Projects\API Oil Production\Notebooks\Oil_pred.pkl','rb'))

def main():
    API = st.text_input('Well_num')
    Formation_ID = st.text_input('Formation')
    Basin_ID = st.text_input('Basin')
    Lateral_Length = st.text_input('Lateral_Length')
    Month_Ord  = st.text_input('Month_After_Peak')

    if st.button('Predict'):
        makeprediction = model.predict(np.array([[API,Formation_ID, Basin_ID, Lateral_Length, Month_Ord]], dtype=object))
        output = round(int(makeprediction[0]),2)
        st.success(f'This well is going to produce around: {output} barrels in month {Month_Ord} after the peak')

if __name__ == '__main__':  
    main()    

st.markdown('### Interactive Plot')

wells = data.API.unique()[:20]

data_f = data[(data.Month_Ord <= 36) & (data.API.isin(wells))]
x_axis_op = data_f.Month_Ord
y_axis_op = st.selectbox('Select Y-Axis', options=data_f.columns[[2,6]])
groups = st.selectbox('Grouped', options=data_f.columns[7:9])

plot = px.box(data_f, x=x_axis_op, y=y_axis_op, color=groups)
st.plotly_chart(plot)

data.mean()
