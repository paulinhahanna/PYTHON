# count - a função é contar quantas vezes um daterminado caractere aparece em uma string 
#upper e a lower - dois metodos que deixam a string toda em maiuscula ou a string toda minuscula 
#find - busca por uma esprssão dentro da frase
#repleace - é ultilizado para realizar alterações dentro das strings
#capitaluze - deixa a primeira letra da frase  maiuscula
# split - tranforma a frase em uma lista

frase = "a banana é amarela e o abacate é verde.".lower()
letra = 'a'
print(f'a letra "{letra}" aparece {frase.count(letra)} vezes na frase "{frase}"')

#saida = input('digite "s" para sair:').upper
#if saida == 'S':
 #   print(saida)

achei = frase.find('roxo')
if achei >= 0:
    print(f'a expressão foi encontrada no indice {achei} ')
else:
    print(f'a expressão não foi encontrada na frase')
nova_frase = frase.replace('banana', 'maracuja')
print(nova_frase)
print(frase.split())