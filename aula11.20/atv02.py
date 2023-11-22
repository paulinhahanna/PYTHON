tentativas = 0
while tentativas <=3:
    tentativas = tentativas + 1
    usuario= str(input('digite seu nome:'))
    senha = str(input('digite sua senha:'))
    if senha == usuario :
        print(f'erro! :essa foi sua tentativa:{tentativas}')
    if tentativas == 3:
            print(f'suas tentativas acabaram. Tente amanha')
            break
    
