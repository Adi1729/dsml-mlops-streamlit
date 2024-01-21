import streamlit as st
import pandas as pd 
import yfinance as yf 

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title(" Stock Market App")

st.write("This project is a demo to understand streamlit")
sym = st.text_input("stock symbol")

start_date = st.date_input("Start Date")
ticket_data = yf.Ticker(sym)
end_date  = st.date_input("End Date")
hist = ticket_data.history(start = start_date , end = end_date)

st.write(hist)
col1,col2 = st.columns(2)

with col1:
    st.header("Volume chart")  
    st.line_chart(hist.Volume)
with col2:
    st.header("Close chart")
    st.line_chart(hist.Close)


st.text("Check")

