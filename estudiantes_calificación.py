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
    if notas[i]>40:
        cociente= int(notas[0]/5+1)
        multiplo= cociente * 5
        if (multiplo - notas[i])<3:
            print("La nota del alumno {}".format(i+1) ,"se aproxima, la nota final es {}".format(multiplo))
        if (multiplo - notas[i])>=3:
            print("La nota del alumno {}".format(i+1) ," no se aproxima, la nota final es {}".format(notas[i]))
    elif notas[i]< 40:
        print("El alumno {} se queda con su nota".format(i+1, notas[i]))
    

    
    
    
    
