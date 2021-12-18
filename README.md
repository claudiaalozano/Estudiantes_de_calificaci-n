# Estudiantes_de_calificaci-n
Mi dirección de Github es:https://github.com/claudiaalozano/Estudiantes_de_calificaci-n.git

A continuación muestro un esquema de como se ejecutaría el código, para crearlo:
![FIGMA FINAL NOTAS ESTUDIANTES](https://user-images.githubusercontent.com/91722847/146642300-09f87b29-79db-46bf-8ded-4ab260d4506c.png)


El código finalmente es:
```import math
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
 ```
