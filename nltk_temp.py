# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from nltk.corpus import PlaintextCorpusReader
import nltk
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer
import re

import unicodedata
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def traduce_numerico(translate_str):
    translate_str = elimina_tildes(translate_str)
    translate_str = re.sub(r'[^\w]', ' ', translate_str)
    translate_str = re.sub('[!@#$ºª]', ' ', translate_str)
    translate_str = tokenizer.tokenize(translate_str)
    translate_str = [t.lower().replace('a', '2').replace('b','2').replace('c','2')
    .replace('d','3').replace('e','3').replace('f','3').replace('g','4')
    .replace('h','4').replace('i','4').replace('j','5').replace('k','5')
    .replace('l','5').replace('m','6').replace('n','6').replace('ñ','6')
    .replace('o','6').replace('p','7').replace('q','7').replace('r','7')
    .replace('s','7').replace('t','8').replace('u','8').replace('v','8')
    .replace('w','9').replace('x','9').replace('y','9').replace('z','9') for t in translate_str]
    return translate_str

# Lectura y transformación de Corpus
wordlists = PlaintextCorpusReader("F:\\MII-TextoPredictivo\\Corpus\\", '.*')
wordlists.words('')
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(wordlists.raw())
tokens = [t.lower() for t in tokens]
tokens = [elimina_tildes(t) for t in tokens]
tokens = [re.sub(r'[^\w]', ' ', t) for t in tokens]
tokens = [re.sub('[!@#$ºª]', '', t) for t in tokens]
tokens_num = [t.replace('a', '2').replace('b','2').replace('c','2')
.replace('d','3').replace('e','3').replace('f','3').replace('g','4')
.replace('h','4').replace('i','4').replace('j','5').replace('k','5')
.replace('l','5').replace('m','6').replace('n','6').replace('ñ','6')
.replace('o','6').replace('p','7').replace('q','7').replace('r','7')
.replace('s','7').replace('t','8').replace('u','8').replace('v','8')
.replace('w','9').replace('x','9').replace('y','9').replace('z','9') for t in tokens]

# Código para traducir un input a teclado númerico
translate_str = "Esto es un ejemplo"
translate_str = traduce_numerico(translate_str)
for t in translate_str:
   print(t)
print("\n");
      
# Generación diccionario de palabras + frecuencia
fdist = FreqDist(tokens) # Estudio de frecuencia
print(fdist.most_common(50)) # Las 50 palabras más frecuentes
list_tokens_num = fdist.most_common()
dict_tokens_freq = {}
for t in list_tokens_num:
    t_num = [t[0].lower().replace('a', '2').replace('b','2').replace('c','2').replace('d','3').replace('e','3').replace('f','3').replace('g','4').replace('h','4').replace('i','4').replace('j','5').replace('k','5').replace('l','5').replace('m','6').replace('n','6').replace('ñ','6').replace('o','6').replace('p','7').replace('q','7').replace('r','7').replace('s','7').replace('t','8').replace('u','8').replace('v','8').replace('w','9').replace('x','9').replace('y','9').replace('z','9'),t[1]]
    try:
        length = len(dict_tokens_freq[int(t_num[0])])
        dict_tokens_freq[(int(t_num[0]))]  = dict_tokens_freq[(int(t_num[0]))] + [[t[0],t[1]]]
    except:
        dict_tokens_freq[int(t_num[0])] = [[t[0],t[1]]]

print("\n")     
print("Search for 7436: ")
print(dict_tokens_freq.get(7436))
print("\n")
print("Search for 7276: ")
print(dict_tokens_freq[7276])
print("\n")
print("Search for 72727: ")
print(dict_tokens_freq[72727])
print("\n")
