import math
import os
import random
import re
import sys

notas= [73 , 67 , 38 , 33]


for i in range(len(notas)):
    if notas[i]> 40:
        print("El alumno {} ha aprobado".format(i+1))
    else:
        print("El alumno {} ha suspendido".format(i+1))


for i in range (len(notas)):
    cociente= int(notas/5+1)
    multiplo= cociente * 5
    nota_final= 0
    if(multiplo-notas<3):
        nota_final += multiplo
    else:
        nota_final = notas
    return nota_final

    
    
    
    #i * 5 < 100
    #i= 0
	#i = i + 1 
	#if i-notas>=3:
        #print("La nota no se aproxima, la nota es:" , notas)
    #else:
        #notas1= i
        #print("La nota se aproxima, tu nota es: " , notas)
