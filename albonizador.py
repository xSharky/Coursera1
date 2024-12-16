# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:53:22 2021

@author: Shark
"""

song=open("canción.txt","r")
lineas=song.readlines()
cantidadlineas=len(lineas)
albo=open("formatoalbo.txt","w")
i=0
while i<cantidadlineas:
    lineaacambiar=lineas[i]
    largolinea=len(lineaacambiar)
    j=0
    lineacambiada=""
    while j<largolinea:
        if lineaacambiar[j] =="u" or lineaacambiar[j]=="U":
            lineacambiada=lineacambiada+"x"
        else:
            lineacambiada=lineacambiada+lineaacambiar[j]
        j=j+1
    albo.write(lineacambiada)
    albo.write('\n')    
    i=i+1
    print(lineacambiada)
song.close()
albo.close()
    