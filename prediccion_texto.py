#!/usr/bin/env python
# -*- coding: utf-8

import traducciones
import modelos_probabilisticos

#Este método se utiliza para la creación de un menú que hace más accesibles las pruebas de
#predicción de texto.
def prediccion_texto():
    print("\nCaso Práctico 1. Predicción de texto\n")
    print(".....................MENÚ.......................")
    print("1. Predicción de texto por unigram de letras")
    print("2. Predicción de texto por bigram de letras")
    print("3. Predicción de texto por unigram de palabras")
    print("4. Predicción de texto por bigram de palabras")
    print("5. Traducir de texto a numérico")
    print("6. Salir")

    opcion = input("\nSeleccione la opción que desea realizar: ")

    if (opcion == '1'):
        texto = input("\nIntroduzca la frase que deseea predecir: ")
        traduccion = traducciones.traduce_numerico(texto)
        diccionarioUnigramLetras = modelos_probabilisticos.diccionario_unigramLetras()
        prediccion = traducciones.traduce_unigramLetras(diccionarioUnigramLetras, traduccion)
        print ("\nLa predicción realizada por el unigram de letras es: ")
        print (prediccion)
        print("\n___________________________________________________")
        prediccion_texto()

    elif (opcion == '2'):
        texto = input("\nIntroduzca la frase que deseea predecir: ")
        traduccion = traducciones.traduce_numerico(texto)
        diccionarioBigramLetras = modelos_probabilisticos.diccionario_bigramLetras()
        prediccion = traducciones.traduce_bigramLetras(diccionarioBigramLetras, traduccion)
        print("\nLa predicción realizada por el bigram de letras es: ")
        print(prediccion)
        print("\n___________________________________________________")
        prediccion_texto()

    elif (opcion == '3'):
        texto = input("\nIntroduzca la frase que deseea predecir: ")
        traduccion = traducciones.traduce_numerico(texto)
        diccionarioUnigramPalabras = modelos_probabilisticos.diccionario_unigramPalabras()
        prediccion = traducciones.traduce_unigramPalabras(diccionarioUnigramPalabras, traduccion)
        print("\nLa predicción realizada por el unigram de palabras es: ")
        print(prediccion)
        print("\n___________________________________________________")
        prediccion_texto()

    elif (opcion == '4'):
        texto = input("\nIntroduzca la frase que deseea predecir: ")
        traduccion = traducciones.traduce_numerico(texto)
        diccionarioBigramPalabras = modelos_probabilisticos.diccionario_bigramPalabras()
        prediccion = traducciones.traduce_bigramPalabras(diccionarioBigramPalabras, traduccion)
        print("\nLa predicción realizada por el bigram de palabras es: ")
        print(prediccion)
        print("\n___________________________________________________")
        prediccion_texto()

    elif (opcion == '5'):
        texto = input("\nIntroduzca la frase que deseea traducir a numérico: ")
        traduccion = traducciones.traduce_numerico(texto)
        print ("\nLa traducción a numérico es: ")
        print(traduccion)
        print("\n___________________________________________________")
        prediccion_texto()

    elif (opcion == '6'):
        exit()

    else:
        print ("\nSeleccione una opción del menú válida")
        prediccion_texto()

prediccion_texto()