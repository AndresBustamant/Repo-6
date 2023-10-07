# Reto-6


hola buenas tardes, este repo tiene como proposito mostrar el desarrollo de el reto 6, el cual se basa en la idea de crear, utilizar e importar funciones.


-NOTA: para correr los programas esta adjunto un notebook y para los puntos 7 y 8 hay dos documentos .py con su respectivo desarrollo


link notebook: https://colab.research.google.com/drive/13ETp39LaGgsWsg8VTtE-_5IhQtPe5iwU?usp=sharing


1.Dado la figura de la imagen, desarrolle:

Una función matemática para calcular el volumen y el área superficial. Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h. Revise como utilizar el valor de pi usando import math y math.pi
![figura 1 reto 6](https://github.com/AndresBustamant/Repo-6/assets/141858005/deb0f541-dc75-4e3f-b84d-5dd3e5df225d)

para el desarrollo de este punto fue de vital importancia buscar las formulas de area y volumen indivuduales, para despues plantearlas como funciones y posteriormente sumarlas, dando asi el volumen y area superficiales de toda la figura:

```pseudocode
import math
def area_esfera(r1: float) -> float:
    areaesfe= 4* math.pi* r1**2
    return areaesfe
def area_cono(r2: float, h:float) -> float:
    areacon= math.pi*r2(r2+ (r2**2+h**2)**1/2)
    return areacon
def volumen_esfera(r1: float) -> float:
    volumenesfe= (4* math.pi*r1**3)/3
    return volumenesfe
def volumen_cono(r2: float, h:float) -> float:
    volumencon= (math.pi*r2**2*h)/3
    return volumencon

def volumen_total(r1: float,r2: float, h:float) -> float:
    return (math.pi*r2**2*h)/3 + (4* math.pi*r1**3)/3
def area_total(r1: float,r2: float, h:float) :
    return (4* math.pi* (r1**2)) + (math.pi*r2*(math.sqrt(r2+ (r2**2+h**2))))

if __name__ == "__main__":
    r1= int(input("ingresa el radio de la esfera:"))
    r2= int(input("ingresa el radio del cono:"))
    h= int(input("ingresa la altura del cono:"))
    volumen= volumen_total(r1,r2,h)

    area= area_total(r1,r2,h)
    print("el voluen superficial de la figura es " +str(volumen))
    print("el area superficial de la figura es " +str(area))
```


2. Dado la figura de la imagen, desarrolle:

Una función matemática para calcular el área y el perimetro. Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b. Revise como utilizar el valor de pi usando import math y math.pi.


![figura 2 reto 6](https://github.com/AndresBustamant/Repo-6/assets/141858005/f9b710ca-b5e3-45fd-9b4c-8de629c38740)


el desarrollo de este punto fue similar a el anterior, primero se busco las formulas que describen como obtener el area y perimetro de un cilindro, para porteriormente interpretar las formulas como funciones, dando como resultado un programa a el cual se le dan variables y calcula el area y perimetro superficial total.

```pseudocode
import math
def area_base_circular(r: float) -> float:
    area_circular= math.pi*r**2
    return area_circular
def area_cuadrada(a: float, b:float) -> float:
    area_cuadrado= 2*math.pi* a*b
    return area_cuadrado
def area_total(r: float,a: float, b:float) -> float:
    areat= 2*math.pi*a*b + 2*math.pi*r**2
    return areat
def perimetro_base_circular(r: float) -> float:
    perimetro_circular= 2*math.pi*r
    return perimetro_circular
def perimetro_cuadrada(a: float, b:float) -> float:
    perimetro_cuadrado= a*b
    return perimetro_cuadrado
def perimetro_total(r: float,a: float, b:float) -> float:
    perimetrot= 2*math.pi*r + a*b
    return perimetrot
if __name__ == "__main__":
    r= int(input("ingresa el radio de la base:"))
    b= int(input("ingresa lo que mide la base cuadrada:"))
    a= int(input("ingresa la altura de la parte cuadrada:"))
    area= area_total(r,a,b)
    perimetro= perimetro_total(r,a,b)
    print("el perimetro superficial de la figura es " +str(perimetro))
    print("el area superficial de la figura es " +str(area))
```


3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

en este punto se plantean funciones a partir de la relacion existente entre cantidad (datos de entrada) y los pesos fijos (datos contantes), onteniendo como resultado un programa que multiplica la cantidad por las proporciones fijas para dar respuesta.

```pseudocode
Gallina = 6
Gallo = 7
pollo = 1

def cantidad_de_carne (n: int, m: int, k:int) ->int:
    carne_de_gallina= n*Gallina
    carne_de_gallo= m*Gallo
    carne_de_pollo= k*pollo
    carne_total= (n*Gallina)+(m*Gallo)+(k*pollo)
    return carne_total
if __name__ == "__main__":
    n= int(input("ingresa la cantidad de gallinas:"))
    m= int(input("ingresa la cantidad de gallos:"))
    k= int(input("ingresa la cantidad de pollos:"))
    carne= cantidad_de_carne(n,m,k)
    print("la cantidade de carne en total es " +str(carne)+ "Kg")
```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.


el planteamiento de este punto es parecido a el punto anterior, se basa en la creacion de funciones que relacionen datos fijos y de entrada.

```pseudocode
panes = 300
leche = 3300
huevos = 350
B:int
def precio_a_pagar (m: int, h: int, p:int) ->int:
    precio_panes= p*panes
    precio_leche= m*leche
    precio_huevos= h*huevos
    precio_total= (p*panes)+(m*leche)+(h*huevos)
    devuelta= B - precio_total
    if devuelta<0:
        print("hace falta dinero para pagar")
    else:
        print("las devueltas son" +str(devuelta))
    return devuelta

if __name__ == "__main__":
    p= int(input("ingresa la cantidad de panes:"))
    m= int(input("ingresa la cantidad de bolsas de leche:"))
    h= int(input("ingresa la cantidad de huevos:"))
    B= int(input("ingresa la cantidad de dinero que te dieron: "))
    devueltas= precio_a_pagar(p,m,h)
    print("la cantidade de dinero restante es " +str(devueltas))
```

5.Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

para solucionar este punto me base en la formula de interes compuesto

![interes compuesto](https://github.com/AndresBustamant/Repo-6/assets/141858005/b975c5ea-959c-44d3-a67b-2c1c275d81d4)

basado en esta formula cree una funcion que solicitara ciertos valores para calcilar el interes representado en funcion de datos como un tiempo dado, la tasa de interes y un capital inicial

```pseudocode
def interes_compuesto (ci: float, i:float, n:float ) -> float:
    capital_final= ci*(1+ i)**n
    return capital_final

if __name__ == "__main__":
    ci= int(input("ingresa el capital prestado:"))
    i= int(input("ingresa el interes anual:"))
    n= int(input("ingresa los años a los que quieres proyectr el interes:"))
    capital= interes_compuesto(ci,i,n)
    print("el capital final es de " +str(capital))
```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

el resultado de este punto fue una funcion, la cual se basa en solicitar ciertos datos como la pobacion inicial y el tiempo que transcurres para asi poder calcular el aumento en contagios, resultando en el siguiente programa:

```pseudocode
def numero_de_contagios (p: int, d:int ) :
    contagios= p*(2**d)
    return contagios

if __name__ == "__main__":
    p= int(input("ingresa la poblacion inicial:"))
    d= int(input("ingresa los dias transcurridos:"))
    contag= numero_de_contagios (p,d)
    print("la poblacion contagiada es de " +str(contag))
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
   -promedio, mediana, pormedio multiplicativo, orden numerico ascendente, orden numerico descendente, La potencia del mayor número elevado al menor número, La raíz cúbica del menor número.

el programa con sus respectivas funciones fue el siguiente:

```pseudocode
import math
a:float
b:float
c:float
d:float
e:float

def promedio_total(a: float,b: float,c: float,d: float,e: float) -> float:
    promedio=(a+b+c+d+e)/5
    return promedio

def mediana_numerica(a: float,b: float,c: float,d: float,e: float) -> float:
    lista_numeros=[a,b,c,d,e]
    orden= sorted(lista_numeros)
    valor_intermedio= lista_numeros[2]
    return valor_intermedio

def promedio_multiplicativo(a: float,b: float,c: float,d: float,e: float) -> float:
    promediom=(a*b*c*d*e)**(1/5)
    return promediom

def orden_ascendente(a: float,b: float,c: float,d: float,e: float) -> float:
    lista_numeros=[a,b,c,d,e]
    ordena= sorted(lista_numeros)
    return ordena

def orden_descendente(a: float,b: float,c: float,d: float,e: float) -> float:
    lista_numeros=[a,b,c,d,e]
    lista_numeros.sort(reverse=True)
    ordend= lista_numeros
    return ordend

def potencia(a: float,b: float,c: float,d: float,e: float) -> float:
    lista_numeros=[a,b,c,d,e]
    orden= sorted(lista_numeros)
    mayor_valor= lista_numeros[4]
    menor_valor= lista_numeros[0]
    potencia= mayor_valor**menor_valor
    return potencia

def Raiz_cubica(a: float,b: float,c: float,d: float,e: float) -> float:
    lista_numeros=[a,b,c,d,e]
    orden= sorted(lista_numeros)
    menor_valor= lista_numeros[0]
    Raiz_cub= menor_valor**(1/3)
    return  Raiz_cub

if __name__ == "__main__":

    a=int(input("ingresa un valor numerico: "))
    b=int(input("ingresa un valor numerico: "))
    c=int(input("ingresa un valor numerico: "))
    d=int(input("ingresa un valor numerico: "))
    e=int(input("ingresa un valor numerico: "))

    promedio=promedio_total(a,b,c,d,e)
    mediana=mediana_numerica(a,b,c,d,e)
    promedio_multipli=promedio_multiplicativo(a,b,c,d,e)
    orden_ascen=orden_ascendente(a,b,c,d,e)
    orden_descen=orden_descendente(a,b,c,d,e)
    poten=potencia(a,b,c,d,e)
    raiz=Raiz_cubica(a,b,c,d,e)

    print("el promedio de los 5 numeros es igual a = " + str(promedio))
    print("la mediana de los 5 numeros es igual a = " + str(mediana))
    print("el promedio multiplicativo de los 5 numeros es igual a = " + str(promedio_multipli))
    print("el orden ascendente de los 5 numeros es = " + str(orden_ascen))
    print("el orden descendente de los 5 numeros es = " + str(orden_descen))
    print("el numero mayor elevado a el numero menor es igual a = " + str(poten))
    print("la raiz cubica del menor numero es = " + str(raiz))
```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```pseudocode
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
```
9.Consultar qué es y cómo funciona pip en python.

es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python y descargarlos a el computador con la finalidad de integrarlos a los desarrollos realizado en python. Muchos paquetes pueden ser encontrados en el Python Package Index (PyPI). Python 2.7.9 y posteriores (en la serie Python2), Python 3.4 y posteriores incluyen pip (pip3 para Python3) por defecto; lo cual no es necesario instalarlo en nuestra pc ya que al instalar python en la version 3.4 o superior en automaático se instala el gestor de paquetes. para su implementacion es necesario descargarlos desde paginas web y posteriormente guardandolos con la terminal get-pip.py, con el fin de despues referenciarla y ejecutar en el momento de utilizar python.

10.Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.
    1. Matplotlib (generacion de gran variedad de graficos)
    
    -escriba su nombre en el campo de búsqueda y, después, seleccione la opción Ejecutar comando: pip install matplotlib. Si ejecuta el comando, se instalará matplotlib , así como los paquetes de los que depende (en este caso, numpy ).
    
    2. TensorFlow (calculos numericos y diagramas de flujos, usasdos frecuente mente para el desarrollo de deep learning)

    -para utilizar este pip es necesario descargar con anterioridad anaconda y posteriormente descargarlo 
    
    3. PyTorch (calculos numericos y tajetas graficas para para la rapida ejecucion de codigos)

     -para utilizar este pip es necesario descargar con anterioridad anaconda y posteriormente luego de la instalación podemos verificar si la instalación se hizo de manera correcta ejecutando instrucciones en Python.
    
    4. Pandas (analisis de series de datos, así como el Data Frame para dos dimensiones)
    
    -Utiliza el comando py -m pip --version para saber si tienes instalado el manejador de paquetes PIP. Emplea el comando py -m pip install numpy para instalar NumPy y, finalmente, usa py -m pip install pandas para instalar Pandas.

    
