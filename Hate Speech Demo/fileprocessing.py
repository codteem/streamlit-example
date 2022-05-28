# -*- coding: utf-8 -*-


# Create your views here.


#outputdir=str(prev_dir)+"/Implementation/"


import os
import datasets, save_results
"""sys.path.insert(0, "E:/Project/")

two_dir_up_path=os.path.abspath('../..')
two_dir_up_path=two_dir_up_path.replace('\\', '/')
#print (two_dir_up_path)
sys.path.insert(0, two_dir_up_path+"/")"""

#print (sys.path)

#from Implementation import preprocess_sentence,segmenter
import numpy as np
from django.shortcuts import render
from Implementation import preprocess_sentence,hate,rel,eth,nat

from django.http import HttpResponse

def loaddata(filename):
    text, sentences,vocab= datasets.build_data(filename)
    
    tokenized_text=[]

    for sent in text:
        sent=sent.split()
        tokenized_text.append(sent)
  
   
            
    X = np.array(tokenized_text)

    return X,  text, vocab,sentences

testing_file = "Data/Test/eth_test" 
outputdir="Results/hello.xlsx"
X_test, text_test,  vocab_test, sentences_test=loaddata(testing_file)
#predicted=eth.predict_label(text_test)
#results(modelname, outputdir, sentences_test, predicted)

hate_label=" "
hate_level=" "
hate_label = hate.predict_label()
if hate_label=="Religion":
    hate_level=rel.predict_label()
elif hate_label=="Ethnicity":
    hate_level=eth.predict_label()
elif hate_label=="National Origin":
    hate_level=nat.predict_label()
elif hate_label=="Not Hate Speech":
    hate_label="Not-Hate-Speech"
    hate_level="Not-Hate-Speech"
    
def results(outputdir, sentences_test, hate_label,hate_level ):
    
    if not os.path.exists(outputdir):
        print ("Output dir ",outputdir, " doesn't exist")
        
    data=[]
    for i in range(len(sentences_test)):

        #labels={0:"Attribution", 1:"Insult", 2: "Symbolization", 3:"Not Hate Speech" }
        predicted_hate_label = hate_label[i]
        predicted_hate_level = hate_level[i]
        
        
        original_sentence = sentences_test[i]["orig_sentence"]
        data.append([predicted_hate_label,predicted_hate_level,original_sentence])
        
    save_results.evaluate(data,outputdir,testing_file)
    

