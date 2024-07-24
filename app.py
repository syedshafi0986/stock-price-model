import yfinance as yf
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

start = '2015-01-01'
end ='2024-05-01'
st.title("stock-predictions")

user_input =st.text_input("enter the stock ticker","APPL")
df = yf.download("APPL", start='2010-01-01', end='2024-01-01')
df = df.drop(["Adj Close","Volume"],axis=1)


# desc
st.subheader("data from 2015 to 2024")
st.write(df.describe)