#listas são um conjunto de elementos
#extend - para estender uma conjuncão

lista_a = [1,2,3,4,5]
lista_b =[6,7,8,9,10]

# o sinal de + ele soma numaros e concatena strings

a = 2
b = 3
print (a + b)

c = "amo"
d = "valley"
print(c + d)

lista_c = lista_a + lista_b
print(lista_c,type(lista_c))
      
lista_a.extend(lista_b)
print(lista_a)