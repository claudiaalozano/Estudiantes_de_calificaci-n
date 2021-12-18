import math
import os
import random
import re
import sys

notas1= ["73" , " "]
notas2 = ["67" , " "]
notas3 = ["38" , " "]
notas4 = ["33" , " "]

if notas1> 40:
    print("Aprobado")
else:
    print("Suspenso")

i=0 
while i * 5 < 100:
	i = i + 1 
	if i-notas1>=3:
        print("La nota no se aproxima, la nota es:" , notas1)
    else:
        notas1= i
        print("La nota se aproxima, tu nota es: " , notas1)
