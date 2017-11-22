#!/usr/bin/python
# -*- coding: utf-8 -*-
#Por Derick Santos

from PIL import Image
import pytesseract
import urllib.request, urllib.parse, urllib.error
import platform
import time
import os
import re

#Banner
def banner():
    if platform.system() == "Windows":
        os.system("cls")
    else:
    	os.system("clear")

    print("=======================================")
    print("==== DictPy - Dicionário em Python ====")
    print("====        Por Derick Santos      ====")
    print("====           Versão 1.0          ====")
    print("=======================================")
    print("====   https://fsocietybrasil.org/ ====")
    print("=======================================")

index = banner()

time.sleep(5)
print("\nPressione CTRL + C para cancelar!\n")
time.sleep(3)

#Programa
def programa(index):
    #Requisição
    site = "https://s.dicio.com.br/"
    termo = input("[D] - Digite uma palavra que você quer saber o significado: ")
    url = site+termo+".jpg"
    r = urllib.request.urlretrieve(url,termo+".jpg")

    #Manipulação de imagens
    imagem = termo+".jpg"
    print(pytesseract.image_to_string(Image.open(imagem)))
    print("")

while True:
    programa(banner)
