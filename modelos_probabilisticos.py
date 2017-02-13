#!/usr/bin/env python
# -*- coding: utf-8
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer
from nltk import bigrams
from nltk import FreqDist
from collections import Counter
import traducciones
import operator
import re

def diccionario_unigramLetras():
    # Lectura y transformación de Corpus
    corpus = PlaintextCorpusReader("Corpus", '.*')
    tokenizer = RegexpTokenizer(r'[a-zA-Záéíóúñ]+')
    tokens = tokenizer.tokenize(corpus.raw())

    frecuenciaLetras = {}
    diccionario = {}

    #Se crea un diccionario que tiene como clave la letra y como valor la frecuencia de esa letra en el corpus
    for lineas in tokens:
        for letra in lineas:
            if letra in list(frecuenciaLetras.keys()):
                count = frecuenciaLetras.get(letra)
                frecuenciaLetras[letra] = count + 1
            else:
                frecuenciaLetras[letra] = 1

    #Se ordena el diccionario por los valores, de mayor a menor. Esto de vuelve un tupla
    frecuenciaLetras = sorted(frecuenciaLetras.items(), key=operator.itemgetter(1), reverse=1)

    #Se recorre la tupla, transformando el primer elemento (la letra) a su numérico
    for letra_frec in frecuenciaLetras:
        numerico = traducciones.traduce_numerico(letra_frec[0])
        numerico = int(numerico)

        #Si el numérico ya está en el diccionario se actualiza su valor y si no está se crea
        if numerico in list(diccionario.keys()):
            diccionario.get(numerico).append([letra_frec[0], letra_frec[1]])
        else:
            diccionario[numerico] = [[letra_frec[0], letra_frec[1]]]

    return diccionario

def diccionario_bigramLetras():
    # Lectura y transformación de Corpus
    corpus = PlaintextCorpusReader("Corpus", '.*')
    corpus = re.sub("([^a-zA-Záéíóúñ\n ])", "", corpus.raw().lower())
    corpus = re.sub("([\n])", " ", corpus)
    
    bigrams = Counter(x+y for x, y in zip(*[corpus[i:] for i in range(2)]))
    bigrams_mix = Counter()
    dict_bigrams = {}
    for b in bigrams:
        if b[0] != " " and b[1] != " ":
            b_tr = b[0] + traducciones.traduce_numerico(b[1])
            bigrams_mix[b_tr] = bigrams_mix[b_tr] + bigrams[b]
            try:
                if dict_bigrams[b_tr][1] < bigrams[b]:
                    dict_bigrams[b_tr] = [b, bigrams[b]]
            except:
                dict_bigrams[b_tr] = [b, bigrams[b]]                    
    return dict_bigrams

def diccionario_unigramPalabras():
    # Lectura y transformación de Corpus
    corpus = PlaintextCorpusReader("Corpus\\", '.*')
    tokenizer = RegexpTokenizer(r'[a-zA-Záéíóúñ]+')
    tokens = tokenizer.tokenize(corpus.raw())

    # Generación diccionario unigram de palabras + frecuencia
    fdist = FreqDist(tokens)  # Estudio de frecuencia
    list_tokens_num = fdist.most_common()
    dict_tokens_freq = {}
    for t in list_tokens_num:
        t_num = [traducciones.traduce_numerico(t[0]), t[1]]
        try:
            dict_tokens_freq[(int(t_num[0]))] = dict_tokens_freq[(int(t_num[0]))] + [[t[0], t[1]]]
        except:
            dict_tokens_freq[int(t_num[0])] = [[t[0], t[1]]]

    return dict_tokens_freq

def diccionario_bigramPalabras():
    # Lectura y transformación de Corpus
    corpus = PlaintextCorpusReader("Corpus", '.*')
    tokenizer = RegexpTokenizer(r'[a-zA-Záéíóúñ]+')
    tokens = tokenizer.tokenize(corpus.raw())
    
    # Generación diccionario bigram de palabras + frecuencia
    bigrams_tokens = bigrams(tokens)
    for b in bigrams_tokens:
        b = (b[0], traducciones.traduce_numerico(b[1]))
    fdist = FreqDist(bigrams_tokens)  # Estudio de frecuencia
    list_tokens_num = fdist.most_common()
    dict_tokens_freq = {}
    for t in list_tokens_num:
        print(t)
        t_key = int(t[0][1])
        try:
            dict_tokens_freq[t_key] = dict_tokens_freq[t_key] + [[t[0][0], t[1]]]
        except:
            dict_tokens_freq[t_key] = [[t[0][0], t[1]]]
    print(dict_tokens_freq)
            
    return dict_tokens_freq
