#!/usr/bin/env python
# -*- coding: utf-8

import re
import modelos_probabilisticos

#Este método devuelve el equivalente númerico de la frase pasada por parámetro
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

#Método que, dado un diccionario de unigam de letras y una frase numérica, devuelve la predicción de esa frase
#según el diccionario de unigram de letras
def traduce_unigramLetras(diccionario, translate_num):
    #Se separa la frase númerica por los espacios, obteniéndose una lista de las palabras numéricas.
    #Posteriormente por cada palabra se van recorriendo las letras y formando la palabra predictiva
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
        #Cuando ya ha recorriendo todas las letras de la palabra numérica se unen para formar la palabra y se guarda
        translated_str.append(''.join(palabra))

    #Se forma la frase predictiva a devolver
    return ' '.join(translated_str)

#Método que, dado un diccionario de bigram de letras y una frase numérica, devuelve la predicción de esa frase
#según el diccionario de bigram de letras. En caso de no poder resolver algún numérico se le aplica el unigram de letras
def traduce_bigramLetras(diccionario, translate_num):
    translate_num = translate_num.split(" ")
    translated_str = []

    for num in translate_num:
        palabra = []
        for n in range(len(num)):
            #Si no es la primera letra se intenta hacer el bigram de letras.
            if (n-1) >= 0:
                try:
                    #Se forma la clave del diccionario (letra anterior conocida y el numérico a buscar)
                    key = palabra[n-1] + str(num[n])
                    # Si la clave está en el diccionario se coge la primera que corresponda (la que más frecuencia tiene)
                    palabra.append(diccionario.get(key)[0][1])
                except:
                    # Si no está se llama al unigram de letras para intentar averiguarlo
                    diccionarioUnigramLetras = modelos_probabilisticos.diccionario_unigramLetras()
                    p = traduce_unigramLetras(diccionarioUnigramLetras, num[n])
                    palabra.append(p)
            # Si es la primera letra, se resuelve con el modelo unigram de letras ya que no hay letra anterior conocida.
            else:
                diccionarioUnigramLetras = modelos_probabilisticos.diccionario_unigramLetras()
                p = traduce_unigramLetras(diccionarioUnigramLetras, num[n])
                palabra.append(p)

        translated_str.append(''.join(palabra))

    return ' '.join(translated_str)

#Método que, dado un diccionario de unigram de palabras y una frase numérica, devuelve la predicción de esa frase
#según el diccionario de unigram de palabras. En caso de no poder resolver algún numérico se le aplica el bigram de letras
def traduce_unigramPalabras(diccionario, translate_num):
    # Se separa la frase númerica por los espacios, obteniéndose una lista de las palabras numéricas.
    # Posteriormente se va recoriendo cada palabra y se obtiene su correspondiente palabra predictiva
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

#Método que, dado un diccionario de bigram de palabras y una frase numérica, devuelve la predicción de esa frase
#según el diccionario de bigram de palabras. En caso de no poder resolver algún numérico se le aplica el unigram de palabras
def traduce_bigramPalabras(diccionario, translate_num):
    translate_num = translate_num.split(" ")
    translated_str = []
    for t in range(len(translate_num)):
        # Si no es la primera palabra se intenta hacer el bigram de palabras.
        if (t-1) >= 0:
            try:
                # Se forma la clave del diccionario (palabra anterior conocida y el numérico a buscar)
                key = translated_str[t-1] + str(translate_num[t])
                # Si la palabra está en el diccionario se coge la primera que corresponda (la que más frecuencia tiene)
                translated_str.append(diccionario.get(key)[0][1])
            except:
                # Si no está se llama al unigram de palabras para intentar averiguarlo
                diccionarioUnigramPalabras = modelos_probabilisticos.diccionario_unigramPalabras()
                palabra = traduce_unigramPalabras(diccionarioUnigramPalabras, translate_num[t])
                translated_str.append(palabra)
        # Si es la primera palabra, se resuelve con el modelo unigram de palabras ya que no hay palabra anterior conocida.
        else:
            diccionarioUnigramPalabras = modelos_probabilisticos.diccionario_unigramPalabras()
            palabra = traduce_unigramPalabras(diccionarioUnigramPalabras, translate_num[t])
            translated_str.append(palabra)

    return ' '.join(translated_str)