# -*- coding: utf-8 -*-

from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer
import re

def traduce_to_numerico(translate_str):
    translate_str = re.sub("([^a-zA-Záéíóú ])","", translate_str.lower())
    translate_str = re.sub("([aábc])","2", translate_str)
    translate_str = re.sub("([deéf])","3", translate_str)
    translate_str = re.sub("([ghií])","4", translate_str)
    translate_str = re.sub("([jkl])","5", translate_str)
    translate_str = re.sub("([mnñoó])","6", translate_str)
    translate_str = re.sub("([pqrs])","7", translate_str)
    translate_str = re.sub("([tuúv])","8", translate_str)
    translate_str = re.sub("([wxyz])","9", translate_str)
    return translate_str

def traduce_from_numerico(diccionario, translate_num):
    translate_num = translate_num.split(" ")
    translated_str = []
    for t in translate_num:
        try:
            translated_str.append(diccionario.get(int(t))[0][0])
        except:
            translated_str.append("$NoMatchInCorpus")
    return translated_str

def crear_diccionario_palabra_unigram():
    # Lectura y transformación de Corpus
    wordlists = PlaintextCorpusReader("F:\\MII-TextoPredictivo\\Corpus\\", '.*')
    tokenizer = RegexpTokenizer(r'[a-zA-Záéíóú]+')
    tokens = tokenizer.tokenize(wordlists.raw())


    # Generación diccionario de palabras + frecuencia
    fdist = FreqDist(tokens) # Estudio de frecuencia
    list_tokens_num = fdist.most_common()
    dict_tokens_freq = {}
    for t in list_tokens_num:
        t_num = [traduce_to_numerico(t[0]),t[1]]
        try:
            dict_tokens_freq[(int(t_num[0]))]  = dict_tokens_freq[(int(t_num[0]))] + [[t[0],t[1]]] 
        except:
            dict_tokens_freq[int(t_num[0])] = [[t[0],t[1]]]
            
    return dict_tokens_freq
      
# Código ejemplo
dictionaryUnigramWord = crear_diccionario_palabra_unigram()    

# Código para consultar un input númerico a texto predictivo
print("Search for 7436: ")
print(dictionaryUnigramWord.get(7436))
print("\n")
print("Search for 7276: ")
print(dictionaryUnigramWord[7276])
print("\n")
print("Search for 72727: ")
print(dictionaryUnigramWord[72727])
print("\n")


# Código para traducir un input a teclado númerico
translate_str = "Hortensia está con Pepita y Elvira"
translated_str = traduce_to_numerico(translate_str)
print(translated_str)
print("\n");

     
# Código para traducir un input númerico a texto predictivo
translate_num = "467836742 3782 266 737482 9 358472"
translated_num = traduce_from_numerico(dictionaryUnigramWord,translate_num)
print(translated_num)
