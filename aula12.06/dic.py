#CRUD - created, readed, updated e deleted

dic = {'nome':'paulo'}             #creaded- criei o dicionario
dic2 = dict(idade=23)              #  outra forma de fazer creaded
dic['nome']
reading = dic2.get('idade')        #readed

dic.update(sobrenome = 'junior')   #updated
dic.update({'idade':23})           #outra forma de fazer updated
tupla =('peso',72.12),             #ao adicionar uma tupla no dicionario vc tem que colocar uma vigula apos o parenteses
dic.update(tupla)                

lista= [ 'data','13/04/1996'],['numeros,',[1,2,3,4,5,6]]     #colocando lista no dicionario e colocando duas lista uma detro da outra  #updated
dic.update(lista)
print(dic)
print(dic2)
dic.clear()                       #deleted
print(f'o dic foi deletado:{dic}')

