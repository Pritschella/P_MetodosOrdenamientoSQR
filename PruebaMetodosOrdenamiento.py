'''
Created on 22/11/2018

@author: acer
'''
import random


def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote =  lista[0]
    for i in lista:
        if i < pivote:
            izquierda.append(i)
        elif i == pivote:
            centro.append(i)
        elif i > pivote:
            derecha.append(i)
            return izquierda + centro + derecha
        else: 
            return lista
        
#a = list(range(0, 100000))
#a = random.sample(a, 10000)
a = [1, 5, 10, 20, 90, 3, 2, 25]
print(a)
sorted=sort(a)
print(sorted)
#print(a[0:10])
#print(a[99990:])