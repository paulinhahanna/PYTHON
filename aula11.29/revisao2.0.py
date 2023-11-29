#estruturas condicionais
# condicoes validam condições, puxando sempre para a  verdade

variavel = 20
if variavel <20 :
    print('menor que 20')
elif variavel == 20:
    print('igual a 20')
elif variavel > 20 and variavel < 50:
    print('esta no intervalo entre 21 e 49')
else:
    print(' qualquer outra coisa')
    

    # estrutura de repetições: FOR e WHILE
# quando vc souber quantas vezes for repetir use FOR. 
# for ele sempre quer interaveis
for i in range(10):
    print( f'print o numero{i}')

# WHILE
#contador =  5
#while contador >0:
 #   print('esse é o print do numero {contador}')
  #  contador -=1

    #join - unir strings
lista =['joão','paulo','II']
nome = '-'.join(lista)
print(nome)