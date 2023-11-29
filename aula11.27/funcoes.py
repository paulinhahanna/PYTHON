#funçôes são blocos de códigos que são execultados somente quando são chamados 
#paramentro def
#as funções devem ter prioridade no código

def media(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3 ) / 3
    return media 
nota1 = int(input('informe a primeira  nota:'))
nota2 = int(input('informe a segunda nota:'))
nota3 = int(input('informe a terceira nota:'))

print(media(nota1,nota2,nota3))

def calculo_horas_extras(quantidade_horas, valor_hora):
    horas = float(quantidade_horas)
    taxa = float(valor_hora)

    if horas >=40:
        valor_receber =(horas - 40) * taxa
    return valor_receber
quantidade_horas = float(input('informe o total de horas trabalhadas:'))
valor_da_hora = float(input('informe o valor da taxa do colaborador:'))
salario = 1400.00
print(calculo_horas_extras(quantidade_horas,valor_da_hora))