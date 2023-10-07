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