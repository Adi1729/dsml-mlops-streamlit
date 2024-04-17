import streamlit as st
import pandas as pd 
import yfinance as yf 


st.title(" Stock Market App")
st.write("This project is a demo to understand streamlit")
sym = st.text_input("stock symbol")

start_date = st.date_input("Start Date")
ticker_data = yf.Ticker(sym)
end_date  = st.date_input("End Date")
hist = ticker_data.history(start = start_date , end = end_date)
st.write("I am going to show")
st.write(hist)
# col1,col2 = st.columns(2)
# with col1:
#     st.header("Volume chart")  
#     st.line_chart(hist.Volume)
# with col2:
#     st.header("Close chart")
#     st.line_chart(hist.Close)


# st.text("Check")
st.write("Plot")
st.line_chart(hist.Volume)

# st.text("Check")
st.write("Plot")
st.line_chart(hist.Close)


