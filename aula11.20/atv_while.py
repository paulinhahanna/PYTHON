while True:
    nota = float(input('digite sua nota'))
    if  nota < 0 or nota >10:
        print("nota invalida")
    if nota > 0 and nota <=10 :
        print("nota valida")
        nota = nota + 1
    break