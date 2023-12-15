#escreva uma função chamada gorjata, que recebe o valor da conta de um restaurante,calcule e exibe a gorjeta do garçom, considerando 12% do valor da conta

conta = float(input('digite o valor da sua conta:'))
gorjeta = (conta* 12 / 100)

print(f'gorjeta é {gorjeta}')