#soma dos valores dos elementos de uma lista
from functools import reduce
def soma(x, y):
    return x+y 
lista = [1, 2, 53, 5, 534]

soma = reduce(soma, lista) #primeiro vem a função, depois a lista desejada a se fazer a função
print(soma)
 
