#alguns cuidados com dados mutaveis
# mutaveis na programação - são dados que pode ter seu valor alterado na memoria do dispositivo
#imutaveis - são dados que só podem ser copiados da memoria do dispositivo

lista =['joão', 'paula']
lista[1] = 'jose'
print(lista)
nome = 'paula'
#nome = 'joão'
#print (nome)
#nome[2] = 'a'
novo_nome = nome
nome = 'joão'
print(nome)
print(novo_nome)

lista_a = ['joão','paula']
lista_b = lista_a
lista_a[1]= 'jose'
print(lista_a)
print(lista_b)