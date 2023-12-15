#dicionarios possuim "CHAVE":"VALOR" (keys,values)
#parametro:{} ou dicit()
# pode criar a mesma chave com o mesmo nome, mas a estrudura  não sera mesma ao imprimir ,quando repetir o memsmo valor
# ele so pega pela chave
#ele não pega o primeiro valor, pegar sempre o ultimo repetido
#


pessoa = {'nome':'paulo', 'sobrenome':'junior'}

print(len(pessoa))
print("="*20)

#imprimir valor
for valor in pessoa.values():
    print(valor)
print("="*20)

#imprimir chave
for chave in pessoa:
    print(chave) 
print("="*20)

#imprimir chave e valor
for chave, valor in pessoa.items():
    print(chave, valor)
print("="*20)

#imprimir so uma chave
print(pessoa['sobrenome'])
print("="*20)

d1 = {'valor1':'100','valor2':'200','valor3':'300'}
d2 = d1.copy()
print(d1)
d2['valor2']= 2000
print(d1)
print(d2.get('valor2'))
print("="*20)


#pop deleta pelo nome no dicionario
d3 = d1.pop('valor3')
print(d1)
print("="*20)

#so atualiza se tiver outro dicionario
outro_nome = {'valor5','valor6'}
d1.update(outro_nome)
print(d1)
print(d1.has_key('valor5'))
