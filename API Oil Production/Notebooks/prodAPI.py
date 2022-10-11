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

def home():
    st.text('Data was gather from Kaggle Datasets')
    st.markdown('#### This is a web app to make predictions of well-production using Machine Learning instead of Curve Decay Formula')

st.sidebar.title('Analytics')
options = st.sidebar.radio('SHEETS',options=['Home','Tables','Plots','Interactive Plots','Forecasting'])

def describe(df):
    st.markdown('### Data')
    st.write(data.head()[['API','Oil','Formation_name', 'Basin_name', 'Lateral_Length', 'Month_Ord', 'Basin_ID']])

    st.markdown('### Data Statistics')
    st.write(data.describe())

def plots(df):
    st.header('Descriptive Plots')
    st.markdown('### Number of Wells by Basin')
    formation_dist = df.Basin_name.value_counts()
    st.bar_chart(formation_dist)

    st.markdown('### Distribution Oil Production by Month')
    fig, ax = plt.subplots(1,1, figsize=(20,10))
    sns.boxplot(data=df, x=df.Month_Ord, y=df.Oil)
    ax.set_xlabel('MONTH', fontsize=13)
    ax.set_ylabel('OIL PRODUCTION', fontsize=13)
    ax.set_xlim(-0.5,20.5)
    ax.set_ylim(0,60000)
    ax.tick_params(axis='y', labelsize=11)
    ax.tick_params(axis='x', labelsize=11)
    st.pyplot(fig)

    st.markdown("### All Wells Cummulative Production Month by Month")
    sum_produ = df.groupby('Month_Ord').sum()['Oil']
    st.line_chart(sum_produ)

def forecast():
    st.markdown('### Forecasting Model')
    model = pickle.load(open(r'C:\Users\USUARIO\Documents\GitHub\Oil-Gas-Projects\API Oil Production\Notebooks\Oil_pred.pkl','rb'))

    API = st.slider('Well', 0, len(data.API.unique()),1)  
    Formation_ID = st.slider('Formation', 0, len(data.Formation_ID.unique()), 1)
    #Basin_ID = st.slider('Basin',0, len(data.Basin_ID.unique()),1)
    Lateral_Length = st.slider('Lateral_Length', 0 , 16000, 2000)
    Month_Ord  = st.slider('Month_After_Peak', 0, 48, 1)

    Basin_name = st.sidebar.selectbox('Basin Name:', data.Basin_name.unique())
    if  Basin_name == 'DENVER BASIN':
        Basin_ID = 1
    elif Basin_name == 'ANADARKO BASIN':
        Basin_ID = 0
    elif Basin_name == 'PERMIAN BASIN':
        Basin_ID = 2
    elif Basin_name == 'WILLISTON BASIN':
        Basin_ID = 3
    
     
    start_month, end_month = st.sidebar.select_slider('Month Range:',options=data.Month_Ord.unique(), value=(0,36))

    df = {'Well':API, 'Formation':Formation_ID, 'Basin':Basin_ID, 'Lateral Length':Lateral_Length, 'Month':Month_Ord}
    df = pd.DataFrame(df, index=[0])

    def main():  
        if st.button('Predict'):
            makeprediction = model.predict(df)
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
    groups = st.selectbox('Grouped By:', options=data_f.columns[7:9])

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
elif options == 'Home':
    home()


