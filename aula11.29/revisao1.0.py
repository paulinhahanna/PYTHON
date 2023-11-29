variavel = 1
print(variavel)
variavel = 'paula'
print(variavel)

#regra do fatiamento [inicio,fim,step]

print(variavel[2:4])
tamanho = 6

#ultilizando fatiamento e repetição imprima uma lista de "a" ate "e" removendo uma letra de cada vez
# primeiro colcoar a quantidade total de indice da lista no range, variavel 
for i in range (6):
    lista = ['a','b','c','d','e']
    print (lista[0:tamanho])
    tamanho -= 1

