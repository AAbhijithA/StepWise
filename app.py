import streamlit as st
import pandas as pd
from datetime import date
import datetime as dt
st.set_page_config(
    page_title="StepWise",
    page_icon="👣"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>StepWise</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Historical Performance</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Footfall</h4>", unsafe_allow_html=True)
data = pd.read_csv("data.csv")
data['date'] = pd.to_datetime(data['date'])
grouped_df = data.groupby('date').sum()
grouped_df = grouped_df.reset_index()
data = pd.concat([data, grouped_df], ignore_index=True)
data = data.drop_duplicates(subset=['date'], keep='last')
data['date'] = data['date'].map(dt.datetime.toordinal)
data['date'] = data['date'] - min(data['date'])
st.line_chart(data,x='date',y='people')
money = pd.read_csv("money.csv")
money['date'] = pd.to_datetime(money['date'])
grouped_df = money.groupby('date').sum()
grouped_df = grouped_df.reset_index()
money = pd.concat([money, grouped_df], ignore_index=True)
money = money.drop_duplicates(subset=['date'], keep='last')
money['date'] = money['date'].map(dt.datetime.toordinal)
money['date'] = money['date'] - min(money['date'])
st.markdown("<h4 style='text-align: center; color: white;'>Profits</h4>", unsafe_allow_html=True)
st.line_chart(money,x='date',y='amount')
perf = pd.DataFrame()
perf['Performance'] = ((money['people'])/(data['people']))*100
perf['date'] = data['date']
st.markdown("<h4 style='text-align: center; color: white;'>Performance of attracting customers</h4>", unsafe_allow_html=True)
st.line_chart(perf,x='date',y='Performance')
un_p = pd.DataFrame()
un_p['Potential'] = ((data['people'] - money['people'])/(data['people']))*100
un_p['date'] = data['date']
st.markdown("<h4 style='text-align: center; color: white;'>Potential for more customers</h4>", unsafe_allow_html=True)
st.line_chart(un_p,x='date',y='Potential')
st.markdown("<h2 style='text-align: center; color: white;'>Todays Performance</h2>", unsafe_allow_html=True)
t1df = data[data['date'] == max(data['date'])]
t2df = money[money['date'] == max(money['date'])]
c1, c2, c3 = st.columns(3)
with c1:
    st.write("Footfall Today:")
    st.write(sum(t1df['people']))
with c2:
    st.write("People Purchased:")
    st.write(sum(t2df['people']))
with c3:
    st.write("Profit Generated Today:")
    st.write(sum(t2df['amount']))
with st.expander("Enter values into the money data"):
    n = st.number_input('Enter the number of people purchased:',value=0)
    m = st.number_input('Enter the total amount they purchased with:',value=0)
    d = st.text_input('Enter the date',value='yyyy-mm-dd')
    if n > 0 and d != 'yyyy-mm-dd' and m > 0:
        df = pd.read_csv('money.csv')
        ldf = pd.DataFrame([[n,m,d]],columns=['people','amount','date'])
        df = pd.concat([df,ldf],axis=0)
        df.to_csv('money.csv',index=False)
