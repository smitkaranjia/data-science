import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import pickle

def app():

    def main():
        # file = open('C:/Users/Smit Karanjia/OneDrive/Desktop/model.pkl','r')
        lreg = pickle.load(open('C:/Users/Smit Karanjia/OneDrive/Desktop/model.pkl', 'rb'))
        st.title('Salary Prediction app')
        exp = st.number_input('Input Experience')
        age = st.number_input('Input age')
        val = np.array([exp,age])
        val = val.reshape(1,-1)
        if st.button('Submit'):
            if val[0][1] < 21:
                st.error('Age should be more than 21')
            else:
                st.success(f'The expected salary is: {lreg.predict(val)[0]}')
    
    main()

app()