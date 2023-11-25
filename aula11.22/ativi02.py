while True:
    maior = 0
    menor = None
    saida =  input('digite "s" para sair:')
    if saida == 's' or saida == 'S':
        print('volte sempre!')
        break
    numero = int(input('innforme um numero inteiro: '))

if numero > maior:
    maior = numero

if menor ==  None or numero < menor:
    menor = numero

    print(f'a soma de {maior} + {menor} = {maior+menor}')
    print(f'o maior valor é: {maior}')
    print(f'o menor valor é: {menor}')