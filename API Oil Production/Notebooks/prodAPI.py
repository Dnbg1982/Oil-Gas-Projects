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

data = pd.read_csv(r'C:\Users\USUARIO\Documents\GitHub\Oil-Gas-Projects\API Oil Production\Datasets\Oil_prod_curve.csv')

st.title('DECAY WELL PRODUCTION PREDICTED BY MACHINE LEARNING')
st.text('Data was gather from Kaggle Datasets')

st.markdown('#### This is a web app to make predictions of well-production using Machine Learning instead of Curve Decay Formula')

st.sidebar.title('Analytics')
options = st.sidebar.radio('SHEETS',options=['Home','Tables','Plots','Interactive Plots','Forecasting'])

def describe(df):
    st.markdown('### Data Statistics')
    st.write(data.describe())



def plots(df):
    st.header('Descriptive Plots')
    st.markdown('### Number of Wells by Basin')
    formation_dist = df.Basin_name.value_counts()
    st.bar_chart(formation_dist)

    st.markdown('### Distribution Oil Production by Month')
    fig, ax = plt.subplots(1,1)
    sns.boxplot(data=df, x=df.Month_Ord, y=df.Oil)
    ax.set_xlabel('Month', fontsize=8)
    ax.set_ylabel('Oil Production', fontsize=8)
    ax.set_xlim(-0.5,20.5)
    ax.set_ylim(0,60000)
    ax.tick_params(axis='y', labelsize=6)
    ax.tick_params(axis='x', labelsize=6)
    st.pyplot(fig)

    st.markdown('### Cummulative production by well over the time')
    sum_produ = df.groupby('Month_Ord').sum()['Oil']
    st.line_chart(sum_produ)



def forecast():
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

def interactive_plot(df):
    st.header('Interactive Plot')
    st.markdown('### Oil production by Basin or Formation')
    np.random.seed(81)
    wells = np.random.choice(df.API.unique(), 20)

    data_f = df[(df.Month_Ord <= 36) & (df.API.isin(wells))]
    x_axis_op = data_f.Month_Ord
    y_axis_op = data_f.Oil
    groups = st.selectbox('Grouped', options=data_f.columns[7:9])

    plot = px.box(data_f, x=x_axis_op, y=y_axis_op, color=groups, width=800, height=500)
    st.plotly_chart(plot)

if options == 'Tables':
    describe(data)
elif options == 'Interactive Plots':
    interactive_plot(data)
elif options == 'Forecasting':
    forecast()
elif options == 'Plots':
    plots(data)
