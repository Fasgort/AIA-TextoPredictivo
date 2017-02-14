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

#Método que crea y devuelve el diccionario de unigram de letras
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

    #Se ordena el diccionario por los valores de mayor a menor. Esto de vuelve un tupla
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

# Método que crea y devuelve el diccionario de bigram de letras
def diccionario_bigramLetras():
    # Lectura y transformación de Corpus
    corpus = PlaintextCorpusReader("Corpus", '.*')
    corpus = re.sub("([^a-zA-Záéíóúñ\n ])", "", corpus.raw().lower())
    corpus = re.sub("([\n])", " ", corpus)

    # Se cuenta cuantas veces aparece en el corpus los pares de letras (incluido espacios)
    bigrams = Counter(x + y for x, y in zip(*[corpus[i:] for i in range(2)]))

    dict_bigrams = {}
    for b in bigrams:
        # A cada par de letras, mientras que no estén vacios, se le traduce su segunda letra a su correspondiente numérico
        if b[0] != " " and b[1] != " ":
            #b_tr será a clave del diccionario
            b_tr = b[0] + traducciones.traduce_numerico(b[1])
            try:
                #Si la clave existe, mira que la frecuencia que está en el diccionario sea más pequeña a la frecuencia del
                #nuevo valor, y si es así, se actualiza por este nuevo valor (Se queda con la frecuencia más alta y su traducción)
                if dict_bigrams[b_tr][1] < bigrams[b]:
                    dict_bigrams[b_tr] = [b, bigrams[b]]
            except:
                #Si no está esa clave se añade
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
    dict_unigrams = {}
    for t in list_tokens_num:
        #Se traduce cada palabra a su numerico [numerico, frecuencia]
        t_num = [traducciones.traduce_numerico(t[0]), t[1]]
        try:
            #Si el numérico ya existe en el diccionario se añade la palabra y la frecuencia
            dict_unigrams[(int(t_num[0]))] = dict_unigrams[(int(t_num[0]))] + [[t[0], t[1]]]
        except:
            #Si no existe se crea
            dict_unigrams[int(t_num[0])] = [[t[0], t[1]]]

    return dict_unigrams

def diccionario_bigramPalabras():
    # Lectura y transformación de Corpus
    corpus = PlaintextCorpusReader("Corpus", '.*')
    tokenizer = RegexpTokenizer(r'[a-zA-Záéíóúñ]+')
    tokens = tokenizer.tokenize(corpus.raw())
    
    # Generación diccionario bigram de palabras + frecuencia
    bigrams_orig = bigrams(tokens)
    fdist = FreqDist(bigrams_orig)
    dict_bigrams = {}
    for b in fdist:
        b_tr = (b[0], traducciones.traduce_numerico(b[1]))
        try:
            if dict_bigrams[b_tr][1] < fdist.get(b):
                dict_bigrams[b_tr] = [b, fdist.get(b)]
        except:
            dict_bigrams[b_tr] = [b, fdist.get(b)]

    return dict_bigrams