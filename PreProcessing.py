# -*- coding: utf-8 -*-



'''
this is final implementation
'''

import codecs
from sklearn.feature_extraction.text import CountVectorizer 

import unicodedata
import re
ClassLebel=[]
Data=[]
uniqeWord=[]
wordList=[]
PunctuationList = ['।','.', ',', '@','!','?','-','_','[',']','{','}'];
Adverb={}
Adjective={}
VerbFull={}
VerbSelected={}
NounSelected={}
ImpPunc=['?','!']
listna=['না','নি','নাই','কে','টা','টি','নাহ']
adj='adj'
adv='adv'
vv='verb'
nouns='noun'
left='<'
right='>'
FinalDataForVector=[]
Vocabulary={} 
Adverb.update({'না':1})
Adjective.update({'অসাধারন':1})  
AbstractNoun={}


Emolist1= [ '-_-',':v',':D',':/',':-/','<3','♥',':p', ':)',':(','😈',':v','(y)','(Y)','>_<',':\'( ']

Emolist2=['বিরক্ত','মজা','অট্টহাসি','বিরক্ত','বিরক্ত','ভালবাসি','ভালবাসি','মজা','খুশি','দুঃখ','দুষ্টামি','ব্যঙ্গ','পছন্দ','পছন্দ','অসহ্য','কষ্ট']
naList=['নেই','নাই','নি','নাকচ', 'নন','নেতিবাচক']
RmvList=['আপনি','আপনা']
def Emoticons(text):
   for i in range (len(Emolist1)):
       if Emolist1[i] in text:
           p=text.find(Emolist1[i])
           text=text[:p]+' '+Emolist2[i]+' '+text[p:]
           
   return text
   

def VerbFullCollection():
    sentpos=''
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\Verb.txt', encoding='utf-8') as f:
       for line in f:
           if vv in line:
               for index, c  in enumerate(line):
                
                   if c==right:
                      index+=1
                      while index < len(line):
                          sentpos=sentpos+line[index]
                          index+=1
                          if(line[index]==left):
                           #print("sentttt\n\n")
                              #print(sentpos)
                              VerbFull.update({sentpos:1})
                              sentpos=''
                              break
                       
                      break


def VerbSelectedCollection():
    sentpos=''
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\SelectedVerb.txt', encoding='utf-8') as f:
       for line in f:
           if vv in line:
               
               for index, c  in enumerate(line):
                
                   if c==right:
                      index+=1
                      while index < len(line):
                          
                          sentpos=sentpos+line[index]
                          index+=1
                          if(line[index]==left):
                              #print("sentttt\n\n")
                              #print(sentpos)
                              VerbSelected.update({sentpos:1})
                              sentpos=''
                              break
                       
                      break


def NounSelectedCollection():
    sentpos=''
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\SelectedNoun.txt', encoding='utf-8') as f:
       for line in f:
           if nouns in line:
               
               for index, c  in enumerate(line):
                
                   if c==right:
                      index+=1
                      while index < len(line):
                          
                          sentpos=sentpos+line[index]
                          index+=1
                          if(line[index]==left):
                              #print("sentttt\n\n")
                              #print(sentpos)
                              NounSelected.update({sentpos:1})
                              sentpos=''
                              break
                       
                      break


   
def AbsCollection():
    sent=''
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\AbstractNoun.txt', encoding='utf-8') as f:
       for line in f:
           sent=line
           sent=sent.strip()
           AbstractNoun.update({sent:1})



def CreateVocab():
    sentpos=''
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\FullTxtFile.txt', encoding='utf-8') as f:
        for line in f:
            for index, c  in enumerate(line):
                if c==left:
                    index+=1
                    while index < len(line):
                        sentpos=sentpos+line[index]
                        index+=1
                        if(line[index]==right):
                            Vocabulary.update({sentpos:1})
                            sentpos=''
                            break
                    break
                        


RepeatedWord = ['মনন']


def SpaceBeforeNa(text):
    query = text.split()
    for k in range(len(query)):
        if query[k] in Vocabulary:
            query[k]=query[k]
        elif query[k] in AbstractNoun:
            query[k]=query[k]
        else:
            #print(query[k])
            for i in range(len(listna)):
                index=0
                while index < len(query[k]):
                    index = query[k].find(listna[i], index)
                    if index == -1:
                        break
                    if query[k].endswith(listna[i]):
                        query[k]=query[k][:index]+' '+query[k][index:]
                    index+=3
    
    sentence=' '
    i=0
    while(i<len(query)):
        sentence=sentence+query[i]+' '
        i=i+1
    sentence=sentence.strip()
    return sentence


def ProkitiProttoy(word):
    no='nothing'
    w=word
    w2=word
    
    l=len(w)
    k=1
    flg=0
    if word in VerbFull:
        while(l>=2):
            l=l-1
            foo = ''.join(word.split())[:-k]
            if foo in VerbSelected:
                flg=100
                
                break
            else:
                k+=1
                flg=0
        if flg==0:
            return no
        elif flg==100:
            return foo
    else:
        #print(w2)
        
        l=len(w2)
        k=1
        flg=0
        while(l>=2):
            l-=1
            foo = ''.join(w2.split())[:-k]
            #print(foo)
            if foo in Adjective:
                flg=100
                break
            elif foo in Adverb:
                flg=100
                break
            elif foo in AbstractNoun:
                flg=100
                break
            elif foo in NounSelected:
                flg=100
                break
             
            elif foo in Vocabulary:
                flg=0;
                break
            elif foo in RmvList:
                flg=0
                break
            
            k+=1
        if flg==100:
            return foo
        elif flg==0:
            return no
        
        
        
        
        
            
        
        
    


    


   
class RepeatReplacer(object):
  def __init__(self):
    self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
    self.repl = r'\1\2\3'
  def replace(self, word):
    if word in RepeatedWord:
       
       return word
    elif word in ImpPunc:
        return word
    elif word in Adverb:
        return word
    elif word in Adjective:
        return word
    elif word in Vocabulary:
        return word
    repl_word = self.repeat_regexp.sub(self.repl, word)
    if repl_word != word:
       return self.replace(repl_word) 
    else:
       return repl_word




def ReplaceRepeatedChar(sentence):
    replacer = RepeatReplacer()
    sentence=sentence.strip()
    
    sentTOwords=sentence.split();
    FinalSentence=''
    for word in sentTOwords:
       s=replacer.replace(word)
       FinalSentence=FinalSentence+s+' '
    FinalSentence.strip()
    return FinalSentence
    
    

def AdjCollection():
    sentpos=''
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\Full.txt', encoding='utf-8') as f:
       for line in f:
           if adj in line:
               for index, c  in enumerate(line):
                
                   if c==left:
                      index+=1
                      while index < len(line):
                          sentpos=sentpos+line[index]
                          index+=1
                          if(line[index]==right):
                           #print("sentttt\n\n")
                              #print(sentpos)
                              Adjective.update({sentpos:1})
                              sentpos=''
                              break
                       
                      break




def AdvCollection():
    sentpos=''
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\FullTxtFile.txt', encoding='utf-8') as f:
       for line in f:
           if adv in line:
               for index, c  in enumerate(line):
                
                   if c==left:
                      index+=1
                      while index < len(line):
                          sentpos=sentpos+line[index]
                          index+=1
                          if(line[index]==right):
                           #print("sentttt\n\n")
                              #print(sentpos)
                              Adverb.update({sentpos:1})
                              sentpos=''
                              break
                       
                      break




 
def RemovePunctuation(str1):
    str1 = re.sub('[।;,@#$><A-Za-z0+-9=./''""_০-৯]', '', str1)
    str1=re.sub(r'(\W)(?=\1)', '', str1)     #Remove Repeated punctuation.............
    return str1


def SpaceBeforePunc(str1):
    str1=str1.strip()

    i=0
    j=0
    l=len(str1)
    while(i<l+j):
        if str1[i] in PunctuationList:
            str1=str1[:i]+' '+str1[i:]
            i=i+2
            j=j+1
        else:
            i=i+1
    return str1



def Read_File():
    
    with open('E:\\cse\\4 2\\thesis\\code\\newBeg\\FinalTrainingData.txt', encoding='utf-8') as f:
        spacedSent=' '
        finalSent=' '
        temp=' '
        for line in f:
        #data=f.read()
        #print(data)
            line=line.split()
            temp=(line[1:])
            for tkn in temp:
                spacedSent=spacedSent+' '+tkn
                
              
            
            
            spacedSent=Emoticons(spacedSent)
            spacedSent=SpaceBeforePunc(spacedSent)
            spacedSent=RemovePunctuation(spacedSent)
            
           
            spacedSent=SpaceBeforeNa(spacedSent)
            #tokenization
            spacedSent=spacedSent.split()
            for wrd in spacedSent:
                if wrd in naList:
                    wrd='না'
              
                #elif wrd=='নি' #নাকচ নেই নন   
                
                if wrd in Adverb:
                    #print(wrd)
                    finalSent=finalSent+' '+wrd
                elif wrd in Adjective:
                    finalSent=finalSent+' '+wrd
                elif wrd in ImpPunc:
                    finalSent=finalSent+' '+wrd
                elif wrd in AbstractNoun:
                    finalSent=finalSent+' '+wrd
                elif wrd in NounSelected:
                    finalSent=finalSent+' '+wrd
                  
                elif (len(wrd)>1):
                    
                    if wrd not in RmvList:
                        proRes=ProkitiProttoy(wrd)
                        if proRes!="nothing":
                            finalSent=finalSent+' '+proRes 
                        
                                          
            #print('final')
            #
            #print(finalSent)
            finalSent=finalSent.strip()
            if len(finalSent)==0:
                k=line[:1]
                #print(k)
                #if len(k)==0:
                    #print('zero')
            else:
                FinalDataForVector.append(finalSent)
                finalSent=finalSent.split()
                temp=finalSent
                k=line[:1]
                if k[0]=='pos':
                    ClassLebel.append(1)
                elif k[0]=='neg':
                    ClassLebel.append(0)
                    
                Data.append(temp)
            spacedSent=' '
            finalSent=' '
               
#print("new\n\n")


def Write_File():
    sentence=' '
    with codecs.open("E:\\cse\\4 2\\thesis\\code\\newBeg\\FinalPreProcessedData.txt", "w", encoding="utf-8") as ff:
        for inner_l in Data:
            for item in inner_l:
                sentence=sentence+' '+item
            sentence=sentence.strip()
            if len(sentence)==0:
                sentence='dkdsfkds ffdgfd gfdgf fgdgfd fgdgfd gfdgdfg fgdgfd gfdgfd'
            ff.write(sentence+'\n')
            sentence=''
        


CreateVocab()
NounSelectedCollection()
VerbSelectedCollection()
VerbFullCollection()
AdjCollection()
AdvCollection()
AbsCollection()
Read_File()
Write_File()



word_vectorizer3gram = CountVectorizer(analyzer='word', ngram_range=(1,1), min_df=1,lowercase=False, token_pattern=u'[\S]+',tokenizer=None)
word_vectorizer3gram.fit_transform(FinalDataForVector)
stp3gram=word_vectorizer3gram.get_feature_names()



#print(word_vectorizer3gram.get_feature_names())
print('number of vector:')
print(len(stp3gram)) 


