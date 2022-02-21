# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:32:04 2022

@author: Toyin
"""

# importing libraries used
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

# loading the pretrained model
model = pickle.load(open('model.sav', 'rb'))

# function to carry out the prediction
def prediction(data):
    data = np.array(data).reshape(1, -1)
    predicted_price = model.predict(data)
    return(predicted_price)

def main():
    st.title("Apple Stock Price Prediction")
    open_price = st.number_input('Open Price')
    high = st.number_input('High Price')
    low = st.number_input('Low Price')
    price = ''
    if st.button("Predict"):
        price = prediction([open_price, high, low])
    
    st.success(price)
    
    
    
    
if __name__ == '__main__':
    main()
