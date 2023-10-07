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
```
    area= area_total(r1,r2,h)
    print("el voluen superficial de la figura es " +str(volumen))
    print("el area superficial de la figura es " +str(area))
