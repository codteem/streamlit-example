# -*- coding: utf-8 -*-


# Create your views here.


#outputdir=str(prev_dir)+"/Implementation/"


import os
from Implementation import datasets, save_results
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

testing_file = "Implementation/Data/Test/eth_test" 
outputdir="hello.xlsx"
X_test, text_test,  vocab_test, sentences_test=loaddata(testing_file)
#predicted=eth.predict_label(text_test)
#results(modelname, outputdir, sentences_test, predicted)

hate_label=" "
hate_level=" "
hate_label = hate.predict_label(text_test)

text_hate=dict(zip(text_test,hate_label))

rel_text=[]
eth_text=[]
nat_text=[]
none=[]
for i in text_test:
    if text_hate[i]==2:
        rel_text.append(i)
    elif text_hate[i]==0:
        eth_text.append(i)
    elif text_hate[i]==1:
        nat_text.append(i)
    else:
        none.append(i)
        
    


"""for i in text_test:
    if text_hate[i]=="Ethnicity":
        eth_text.append(i)
        

for i in text_test:
    if text_hate[i]=="Nationality":
        nat_text.append(i)"""

rel_level=rel.predict_label(rel_text)
reltext_level=dict(zip(rel_text,rel_level))

eth_level=eth.predict_label(eth_text)
ethtext_level=dict(zip(eth_text,eth_level))

nat_level=eth.predict_label(nat_text)
nattext_level=dict(zip(nat_text,nat_level))



    
        
labels={0:"Attribution", 1:"Insult", 2: "Symbolization", 3:"Not Hate Speech" }
rlabels={0:"Not Hate Speech", 1:"Attribution", 2:"Insult", 3: "Symbolization" }

hlabels={0:"Ethnicity", 1:"National Origin", 2: "Symbolization", 3:"Not Hate Speech" }

rows=[]
hate_labels=[]
hate_levels=[]
for t in text_test:
    hate_labels.append(labels[hate_label])
    if text_hate[t]==2:
        level=reltext_level[t]
        hate_levels.append(rlabels[level])
    elif text_hate[t]==0:
        level=ethtext_level[t]
        hate_levels.append(labels[level])
    elif text_hate[t]==1:
        level=nattext_level[t]
        hate_levels.append(labels[level])
    else:
        level='not hate speech'
        hate_levels.append(level)
    

        
        
    



"""if "Religion" in hate_label:
    hate_level=rel.predict_label(text_test)
elif "Ethnicity" in hate_label:
    hate_level=eth.predict_label(text_test)
elif "National Origin" in hate_label:
    hate_level=nat.predict_label(text_test)
elif "Not Hate Speech" in hate_label:
    hate_label="Not-Hate-Speech"
    hate_level="Not-Hate-Speech"""
    
def results(outputdir, sentences_test, hate_label,hate_level ):
    
    if not os.path.exists(outputdir):
        print ("Output dir ",outputdir, " doesn't exist")
        
    data=[]
    for i in range(len(sentences_test)):

        #labels={0:"Attribution", 1:"Insult", 2: "Symbolization", 3:"Not Hate Speech" }
        predicted_hate_label = hate_labels[i]
        predicted_hate_level = hate_levels[i]
        
        
        original_sentence = sentences_test[i]["orig_sentence"]
        data.append([predicted_hate_label,predicted_hate_level,original_sentence])
        
    save_results.evaluate(data,outputdir,testing_file)
    
results(outputdir, sentences_test, hate_labels,hate_levels )
