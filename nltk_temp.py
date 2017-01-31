# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from nltk.corpus import PlaintextCorpusReader
import nltk
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer

wordlists = PlaintextCorpusReader("F:\\MII-TextoPredictivo\\Corpus\\", '.*')
wordlists.words('')
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(wordlists.raw())
tokens_num = [t.lower().replace('a', '2').replace('b','2').replace('c','2')
.replace('d','3').replace('e','3').replace('f','3').replace('g','4')
.replace('h','4').replace('i','4').replace('j','5').replace('k','5')
.replace('l','5').replace('m','6').replace('n','6').replace('ñ','6')
.replace('o','6').replace('p','7').replace('q','7').replace('r','7')
.replace('s','7').replace('t','8').replace('u','8').replace('v','8')
.replace('w','9').replace('x','9').replace('y','9').replace('z','9') for t in tokens]

tokens_and_num = []
tokens_and_num = tokens.copy()
tokens_and_num.append(tokens_num)

print(tokens_and_num)

wordToNumDict = {}
a = 0
while a <= len(tokens_and_num)/2:
    tokens_and_num[a] = tokens_and_num[(len(tokens_and_num))/2 + a]
    a = a+1


#print(type(wordToNumDict))

print(wordToNumDict.get("de"))

print("\n");
                           
#print(len(tokens)) # Número de palabras

fdist1 = FreqDist(tokens) # Estudio de frecuencia
print(fdist1.most_common(50)) # Las 50 palabras más frecuentes

print("\n");

fdist2 = FreqDist(tokens_num) # Estudio de frecuencia
print(fdist2.most_common(50)) # Las 50 palabras más frecuentes