contador_par = 0
contador_impar = 0
for i in range(1,11):
    numero = int(input(f'informe o numero {i} : '))
    if numero % 2 == 0:
        contador_par +=1
    else:
        contador_impar +=1
        print(f'a quantidade de numeros pares é: {contador_par}')
        print(f'a quantidade de numeros impar é: {contador_impar}')