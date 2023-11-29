# Faça um programa que peça para 10 pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 a 60 e maior que 60; e então, dizer se a turma é jovem ou adulta ou idosa, conforme a média calculada

for i in range(11):
    print = input('digite sua idade:')
    if i >0 and i<=25:
        print('turma jovem')
    if i > 26 and i < 60:
        print('turma adulta')
    if i > 60:
        print('turma idosa')