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
well = data.groupby(['API']).count()
wells = well.index[well.Oil > 40]
data = data[data.API.isin(wells)]

st.title('DECAY WELL PRODUCTION PREDICTED BY MACHINE LEARNING (XGBOOST)')

def home():
    st.text('Data was gather from Kaggle Datasets: https://www.kaggle.com/c/datascienceatraisa')
    st.markdown('#### This is a web app to make predictions of well-production using Machine Learning instead of Curve Decay Formula')
    st.write('Oil Production forecasting is one of the most important problems in the Oil and Gas industry. Accurately estimating the amount of liquid that could be produced by a certain well along its lifetime is very crucial especially from the economical and business side. There are several factors that contribute into it, starting from the well location, geological factors, drilling technologies used by the operator drilling, neighboring wells and their effect on each others.')

st.sidebar.title('Analytics')
options = st.sidebar.radio('SHEETS',options=['Home','Tables','Plots','Interactive Plot','Forecasting'])

def describe(df):
    st.markdown('### Data')
    st.write(data.sort_values(by='Lateral_Length', ascending=False).head()[['API','Oil','Formation_name', 'Basin_name', 'Lateral_Length', 'Month_Ord', 'Basin_ID']])

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

    st.markdown("### All Wells Cummulative Decay Production Month by Month")
    sum_produ = df.groupby('Month_Ord').sum()['Oil']
    st.line_chart(sum_produ)

def forecast():
    st.markdown('### Forecasting Model')
    model = pickle.load(open(r'C:\Users\USUARIO\Documents\GitHub\Oil-Gas-Projects\API Oil Production\Notebooks\Oil_pred.pkl','rb'))

    API = st.slider('Well', 0, len(data.API.unique()),3500)  
    Formation_ID = st.slider('Formation', 0, len(data.Formation_ID.unique()), 38)
    #Basin_ID = st.slider('Basin',0, len(data.Basin_ID.unique()),1)
    Lateral_Length = st.slider('Lateral_Length', 0 , 16000, 8000)
    # Month_Ord  = st.slider('Month_After_Peak', 0, 48, 1)

    Basin_name = st.sidebar.selectbox('Basin Name:', data.Basin_name.unique())
    if  Basin_name == 'DENVER BASIN':
        Basin_ID = 1
    elif Basin_name == 'ANADARKO BASIN':
        Basin_ID = 0
    elif Basin_name == 'PERMIAN BASIN':
        Basin_ID = 2
    elif Basin_name == 'WILLISTON BASIN':
        Basin_ID = 3
    
     
    start_month, end_month = st.sidebar.select_slider('Month Range:',options=data.Month_Ord.unique()[0:40], value=(0,36))

    df = pd.DataFrame()
    for x in range(start_month,end_month+1):
         df_n = pd.DataFrame({'Well':API, 'Formation':Formation_ID, 'Basin':Basin_ID, 'Lateral Length':Lateral_Length, 'Month_Ord':x}, index=[x])
         df = pd.concat([df,df_n], axis=0)

    #df = {'Well':API, 'Formation':Formation_ID, 'Basin':Basin_ID, 'Lateral Length':Lateral_Length, 'Month':Month_Ord}
    # df = pd.DataFrame(df, index=[0])

    def main():  
        if st.button('Predict'):
            makeprediction = model.predict(df)
            output = np.array(makeprediction, dtype=int)
            st.success(f'This well is going to produce around: \n\n {output.sum()} barrels from month {start_month} to {end_month} after the peak')

    if __name__ == '__main__':  
        main()    

    predicts = model.predict(df)
    index = np.arange(start_month, end_month).tolist()
    data_preds = pd.DataFrame(zip(predicts, data.Oil[data.API == API][start_month:end_month]),columns=('Predictions', 'Oil_Production'), index=index)
    
    fig, ax = plt.subplots(1,1, figsize=(20,10))
    sns.lineplot(data=data_preds, x=data_preds.index, y=data_preds.Predictions)
    sns.lineplot(data=data_preds, x=data_preds.index, y=data_preds.Oil_Production)
    ax.set_title(f'(Well {API}) Production vs Predictions from month {start_month} to {end_month}', fontsize=18)
    ax.set_xlabel('MONTH', fontsize=13)
    ax.legend(['Predictions', 'Real'])
    ax.set_ylabel('OIL PRODUCTION', fontsize=13)
    ax.set_xlim(start_month,end_month)
    ax.set_ylim(0,20000)
    ax.tick_params(axis='y', labelsize=11)
    ax.tick_params(axis='x', labelsize=11)
    st.pyplot(fig)

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


