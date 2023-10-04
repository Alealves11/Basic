# -*- coding: utf -8 -*- #comentario funcional, pra acentuação

x = "Alexandre"
y = "Alves"
j = "o pai ta trabalhando hoje, em pleno sabado"
s = x + " "+ y 
"""com aspas, ele transforma o que ta dentro em texto, 
e com essa soma, apenas faz a junção"""

print (s)
tamanho = len(s)
print (tamanho)

print (x[0:3]) #mostra qual dado esta na posição de 0 à 5 da minha Sting x
print (y[3]) #mostra o que está inscrito na posição 3 da string y

print(x.lower())#transforma a string x em lestras minusculas
print(y.upper())#transforma a string y em letras maiusculas
print(j.find(""))#busca a posição da palavra desejada na sua strig
print(j.replace("o pai","a mãe"))