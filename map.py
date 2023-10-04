#função map
#pega uma função e aplica para todos elementos de uma lista

def dobro(x):
    return x*2
valor = [1, 2, 3, 4, 5]
n=0
dob = map(dobro, valor)
List= []
for i in dob:
    List.append(i)

print(List) 

