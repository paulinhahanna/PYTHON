dic_acesso = {'ana': '1212', 'marcos': '1024','juca':'9870'}      # criar o loguin

usuario_senha = {}                      
usuario = input('informe seu usuario:')                            #pedir o loguin 
senha = input('informe sua senha:')

usuario_senha = [usuario] = senha
print(usuario_senha)

for chave in dic_acesso.keys():
   # print(chave)
   # print(dic_acesso[chave])
    if chave == usuario:
        print('usuario ok')
        if dic_acesso[chave] == senha:
            print('acesso liberado')
            break
else:
     print(f'o usuario{usuario} não foi encontrado')





