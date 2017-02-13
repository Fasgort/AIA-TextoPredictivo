#!/usr/bin/env python
# -*- coding: utf-8

import re
import modelos_probabilisticos

#Método que traduce una frase a su equivalente numérico
def traduce_numerico(str):
    translate_str = re.sub("([^a-zA-Záéíóúñ\n ])", "", str.lower())
    translate_str = re.sub("([\n])", " ", translate_str)
    translate_str = re.sub("([aábc])", "2", translate_str)
    translate_str = re.sub("([deéf])", "3", translate_str)
    translate_str = re.sub("([ghií])", "4", translate_str)
    translate_str = re.sub("([jkl])", "5", translate_str)
    translate_str = re.sub("([mnñoó])", "6", translate_str)
    translate_str = re.sub("([pqrs])", "7", translate_str)
    translate_str = re.sub("([tuúv])", "8", translate_str)
    translate_str = re.sub("([wxyz])", "9", translate_str)
    return translate_str

#Método que traduce la frase pasada según el diccionario de unigram de letras
def traduce_unigramLetras(diccionario, translate_num):
    translate_num = translate_num.split(" ")
    translated_str = []

    for num in translate_num:
        palabra = []
        for n in num:
            try:
                #Si la letra está en el diccionario se coge la primera que corresponda (la que más frecuencia tiene)
                palabra.append(diccionario.get(int(n))[0][0])
            except:
                #Si no está se pone una ? indicando que no sabe que letra es
                palabra.append("?")
        translated_str.append(''.join(palabra))

    return ' '.join(translated_str)

def traduce_bigramLetras(diccionario, translate_num):
    translate_num = translate_num.split(" ")
    translated_str = []

    for num in translate_num:
        palabra = []
        for n in range(len(num)):
            if (n-1) >= 0:
                try:
                    key = palabra[n-1] + str(num[n])
                    # Si la letra está en el diccionario se coge la primera que corresponda (la que más frecuencia tiene)
                    palabra.append(diccionario.get(key)[0][1])
                except:
                    # Si no está se llama al unigram de letras para intentar averiguarlo
                    diccionarioUnigramLetras = modelos_probabilisticos.diccionario_unigramLetras()
                    p = traduce_unigramLetras(diccionarioUnigramLetras, num[n])
                    palabra.append(p)
            else:
                # Si es la primera letra, resolvemos con el modelo unigram
                diccionarioUnigramLetras = modelos_probabilisticos.diccionario_unigramLetras()
                p = traduce_unigramLetras(diccionarioUnigramLetras, num[n])
                palabra.append(p)
        translated_str.append(''.join(palabra))

    return ' '.join(translated_str)

def traduce_unigramPalabras(diccionario, translate_num):
    translate_num = translate_num.split(" ")
    translated_str = []
    for t in translate_num:
        try:
            # Si la palabra está en el diccionario se coge la primera que corresponda (la que más frecuencia tiene)
            translated_str.append(diccionario.get(int(t))[0][0])
        except:
            # Si no está se llama al bigram de letras para intentar averiguarlo
            diccionarioBigramLetras = modelos_probabilisticos.diccionario_bigramLetras()
            palabra = traduce_bigramLetras(diccionarioBigramLetras, t)
            translated_str.append(palabra)

    return ' '.join(translated_str)

def traduce_bigramPalabras(diccionario, translate_num):
    translate_num = translate_num.split(" ")
    translated_str = []
    for t in range(len(translate_num)):
        if (t-1) >= 0:
            try:
                key = translated_str[t-1] + str(translate_num[t])
                # Si la palabra está en el diccionario se coge la primera que corresponda (la que más frecuencia tiene)
                translated_str.append(diccionario.get(key)[0][1])
            except:
                # Si no está se llama al unigram de palabras para intentar averiguarlo
                diccionarioUnigramPalabras = modelos_probabilisticos.diccionario_unigramPalabras()
                palabra = traduce_unigramPalabras(diccionarioUnigramPalabras, translate_num[t])
                translated_str.append(palabra)
        else:
            # Si es la primera palabra, resolvemos con el modelo unigram
            diccionarioUnigramPalabras = modelos_probabilisticos.diccionario_unigramPalabras()
            palabra = traduce_unigramPalabras(diccionarioUnigramPalabras, translate_num[t])
            translated_str.append(palabra)

    return ' '.join(translated_str)