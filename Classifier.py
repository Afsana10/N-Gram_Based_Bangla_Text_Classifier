# -*- coding: utf-8 -*-

'''

this is final implementation


'''

import codecs


import unicodedata
import re
import nltk 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy import sparse

from sklearn import svm

from sklearn.feature_extraction.text import CountVectorizer

import PreProcessing


OneGram=[]
OneGram=PreProcessing.stp3gram
CL=PreProcessing.ClassLebel
#print(OneGram)
vec = CountVectorizer(analyzer='word', ngram_range=(1,1), min_df=1,lowercase=False, token_pattern=u'[\S]+',tokenizer=None,vocabulary=OneGram)
global rate
datalst=[]
vul=[]
predictCls=[]
resultCls=[]
def Training():
    #.......read preprocessed data first..............
   
    al=[]
    lst=[]
    
    
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\FinalPreProcessedData.txt', encoding='utf-8') as f:
        for line in f:
            lst.append(line)
            sentence1 = vec.transform(lst)
            lst=[]
            al=[]
            #print('s')
            s=sentence1.toarray()
            #print(s)
            al = np.squeeze(np.asarray(s))
            #print('al')
            #print(al)
            datalst.append(al)
            
            
    #print(al)
    #print('ssadf')

            


def Predict():
  
     with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\TestSet.txt', encoding='utf-8') as f:
        temp=' '
        finalSent=' '
        spacedSent=' '
        rate=0
        tp=0
        tn=0
        fp=0
        fn=0
        pol=''
        idx=0
        
        for line in f:
            idx+=1
            testData=[]
            ald=[]
            var=10
            pol='d'
            line=line.split()
            temp=(line[1:])
            k=line[:1]
            if len(k)!=0:
                pol=k[0]
            

            if pol=='pos':
                var=1
                predictCls.append(1)
            elif pol=='neg':
                var=0
                predictCls.append(0)
            for tkn in temp:
                spacedSent=spacedSent+' '+tkn
            spacedSent=PreProcessing.Emoticons(spacedSent)
            spacedSent=PreProcessing.SpaceBeforePunc(spacedSent)
            spacedSent=PreProcessing.RemovePunctuation(spacedSent)
            
            spacedSent=PreProcessing.SpaceBeforeNa(spacedSent)
            spacedSent=spacedSent.split()
            for wrd in spacedSent:
                if wrd=='নেই':
                    wrd='না'
                elif wrd=='নি':
                    wrd='না'
                elif wrd=='নাকচ':
                    wrd='না'
                elif wrd=='নেই':
                    wrd='না'
                elif wrd=='নন':
                    wrd='না'    
                    
                    
                    
                if wrd in PreProcessing.Adverb:
                    finalSent=finalSent+' '+wrd
                elif wrd in PreProcessing.Adjective:
                    finalSent=finalSent+' '+wrd
                elif wrd in PreProcessing.ImpPunc:
                    finalSent=finalSent+' '+wrd
                elif wrd in PreProcessing.AbstractNoun:
                    finalSent=finalSent+' '+wrd
                elif wrd in PreProcessing.NounSelected:
                    finalSent=finalSent+' '+wrd
                elif (len(wrd)>2):
                    proRes=PreProcessing.ProkitiProttoy(wrd)
                    if proRes!="nothing":
                        finalSent=finalSent+' '+proRes 
            finalSent=finalSent.strip()
            testData.append(finalSent)
            
            sentence1 = vec.transform(testData)
            s=sentence1.toarray()
            ald = np.squeeze(np.asarray(s))
            
            #print(k)
            p=clf.predict([ald])
            
            #print('prediction')
            #print(p)
            kg=[]
            kg=p.tolist()
            resultCls.append(kg[0])
            h=kg[0]
            if h==var:
                rate=rate+1
                if h==0:
                    tn+=1
                elif h==1:
                    tp+=1
            else:
                if h==1:
                    fp+=1
                elif h==0:
                    fn+=1
                vul.append(testData)
                #print(testData)
                #print (idx)
                #print('else')
                #print('v=')
                #print(var)
                
            var=10
            ald=[]
            testData=[]
            spacedSent=' '
            finalSent=' '
        
     print('tp+tn:')
     print(rate)
     print('accuracy:')
     print((rate*100)/len(resultCls))
     print('tp:')
     print(tp)
     print('tn:')
     print(tn)
     print('fp:')
     print(fp)
     print('fn:')
     print(fn)
     
     
            
        
        
        
Training()
 

      
X = np.array(datalst)
sA = sparse.csr_matrix(X) 
#X=X.reshape(-1,1) 
#clf = svm.SVC(kernel='linear', C = 1.0) 
clf = svm.NuSVC(kernel='rbf') 
#clf = svm.LinearSVC(C = 1.0)
clf.fit(sA,CL)

#vectorizer_sent = CountVectorizer(analyzer='word', ngram_range=(2,2 ), min_df=1,lowercase=False, token_pattern=u'[\S]+',tokenizer=None,vocabulary=OneGram)

Predict()















 
''' 
 
sentence1 = vec.transform(['বিলাসিতার ব্যাপার'])      
sentence2 = vec.transform(['বান্দরবান শহরে খাবার এর দাম খুব বেশি না'])
sentence3 = vec.transform(['  তাই আজ হারতে বসেছে  '])   
sentence4 = vec.transform(['এটা নিশ্চয় রেফারীর দোষ']) 
sentence5 = vec.transform(['চেলসি হ্যাজার্ডকে সেল করবে কিনা সেটা নিয়ে যথেষ্ট সন্দেহ আছে।কন্তের মনে হয় সেল করার কোন ইচ্ছে নাই।'])  
#print(sentence1)

     
al=[]
bl=[]
cl=[]
dl=[]
el=[]
s=sentence1.toarray()
al = np.squeeze(np.asarray(s)) 
#print(al)
s=sentence2.toarray()
bl = np.squeeze(np.asarray(s))
s=sentence3.toarray()
cl = np.squeeze(np.asarray(s))
s=sentence4.toarray()
dl = np.squeeze(np.asarray(s))
s=sentence5.toarray()
el = np.squeeze(np.asarray(s))
print(clf.predict(al)) 
print(clf.predict(bl)) 
print(clf.predict(cl)) 
print(clf.predict(dl)) 
print(clf.predict(el))        
        
        
'''        
#print(resultCls)
#print(predictCls)
print(len(resultCls))
#print(len(predictCls) )       
        
        
        
        
        
        
        