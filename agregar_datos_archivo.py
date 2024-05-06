# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:24:22 2024

@author: Dell
"""

archivo = open("noticia.txt","at")
# \n es para agregar el contenido en una línea al final
contenido="\nFuente: RPP"

archivo.write(contenido)

archivo.close()
