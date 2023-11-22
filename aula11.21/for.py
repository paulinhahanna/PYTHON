# for - trabalha com interaveis
# tem que possui uma variavel de controle
#iter()
#next()
 
#nome = 'paulo'
#texto(iter(peulo))

#print(next(letra))

#for letra in nome:
 #   print(letra)


#enumerate

lista_nomes =[ 'joão','pedro','mateus','judas','tiago']
lista_enumerada =enumerate(lista_nomes)
print(lista_nomes)
print(lista_enumerada)

for item in lista_enumerada:
    print(item)

for indice_lista,item_lista in enumerate(lista_nomes):
    print(f'{item_lista} é o {indice_lista} da lista')