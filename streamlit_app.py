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
py_file_location = "Hate Speech Demo/"
sys.path.append(os.path.abspath(py_file_location))
import preprocess_sentence
import offensive
import hate,rel,eth,nat,offensive

# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def classify(sent):
  sent=preprocess_sentence.build_data(sent)
  sent=[sent]

  offensive_label=" "
  hate_label=" "
  hate_level=" "
      
  offensive_label=offensive.predict_label(sent)
  if offensive_label=="Offensive":
      hate_label = hate.predict_label(sent)
    
      if hate_label=="Religion":
              hate_level=rel.predict_label(sent)
          elif hate_label=="Ethnicity":
              hate_level=eth.predict_label(sent)
          elif hate_label=="National Origin":
              hate_level=nat.predict_label(sent)
          elif hate_label=="Not Hate Speech":
              hate_label="Not-Hate-Speech"
              hate_level="Not-Hate-Speech"

          if hate_level=="Symbolization":
            hate_level = "Less Intense"
          elif hate_level == "Attribution":
            hate_level = "Moderately Intense"
          elif hate_level == "Insult":
            hate_level = "Highly Intense"
            
  else:
      hate_label = "Not Hate Speech"
      hate_lavel = "Not Hate Speech"
          
   
  return offensive_label, hate_label, hate_level

def main():
    st.title("Toxicity Detection Urdu")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Toxicity Detection Urdu</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    urdu_text = st.text_input("Urdu Text","Type Here")
    
    
    off_label, hate_label = classify(urdu_text)

        
    if st.button("Predict"):
        # result=predict_note_authentication(variance,skewness,curtosis,entropy)
        st.success('The sentence is {}'.format(off_label))
        st.success('The sentence is {}'.format(hate_label))

if __name__=='__main__':
    main()   
