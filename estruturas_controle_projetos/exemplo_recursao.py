#!/usr/local/bin/python3

def imprimir(maximo, atual):
  # condicão de parada
  if atual < maximo:
    print(atual)
    imprimir(maximo, atual + 1)
  

imprimir(990, 1) 
