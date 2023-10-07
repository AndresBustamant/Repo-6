a:float
b:float
c:float
d:float
e:float

from punto7reto6 import promedio_total
from punto7reto6 import mediana_numerica
from punto7reto6 import promedio_multiplicativo
from punto7reto6 import orden_ascendente
from punto7reto6 import orden_descendente
from punto7reto6 import potencia
from punto7reto6 import Raiz_cubica

if __name__ == "__main__":
    a=int(input("ingresa un valor numerico: "))
    b=int(input("ingresa un valor numerico: "))
    c=int(input("ingresa un valor numerico: "))
    d=int(input("ingresa un valor numerico: "))
    e=int(input("ingresa un valor numerico: "))
    
    promedio = promedio_total(a,b,c,d,e)
    print("el promedio de los 5 numeros es igual a = " + str(promedio))
    mediana = mediana_numerica(a,b,c,d,e)
    print("la mediana de los 5 numeros es igual a = " + str(mediana))
    promedio_multipli = promedio_multiplicativo (a,b,c,d,e)
    print("el promedio multiplicativo de los 5 numeros es igual a = " + str(promedio_multipli))
    orden_ascen = orden_ascendente (a,b,c,d,e)
    print("el orden ascendente de los 5 numeros es = " + str(orden_ascen))
    orden_descen = orden_descendente (a,b,c,d,e)
    print("el orden descendente de los 5 numeros es = " + str(orden_descen))
    poten = potencia (a,b,c,d,e)
    print("el numero mayor elevado a el numero menor es igual a = " + str(poten))
    raiz = Raiz_cubica (a,b,c,d,e)
    print("la raiz cubica del menor numero es = " + str(raiz))