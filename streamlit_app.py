from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
import pickle
import sklearn
from PIL import Image

import os
import sys
py_file_location = "/Hate Speech Demo/"
sys.path.append(os.path.abspath(py_file_location))
from HateSpeechDemo import fileprocessing

# import offensive
# import hate,rel,eth,nat,offensive

# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Toxicity Detection Urdu")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Toxicity Detection Urdu</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    urdu_text = st.text_input("Urdu Text","Type Here")

    result=""
    
    if st.button("Predict"):
        # result=predict_note_authentication(variance,skewness,curtosis,entropy)
        st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()   
