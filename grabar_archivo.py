# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:23:26 2024

@author: Dell
"""

archivo = open ("archivo_de_prueba.txt","wt")
contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a Ñaña."
archivo.write(contenido)
archivo.close()
