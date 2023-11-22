# ser - conjuntos

set01 = set('paulo')
set02 = {'paulo','junior','lara','kaynan','felipe'}
print(set01)
print(set02)

lista = [1,2,3,4,5,5,5,5,5,5]
print(lista)
set03 = set(lista)
print(set03)
print(5 in set03)
print(7 in set03)
print(7 not in set03)
print( 5 not in set03)

for i in set03:
    print(i)

set03.add('joão')
set03.add('6')
set03.update('paulo')
set03.discard('paulo')
set03.clear()
print(set03)

set04 = {1,2,3,4,5}
set05 = {4,5,6,7,8}

set06 = set04|set05   # união de conjuntos
print(set06)
set06 = set04 & set05  # inter de conjuntos
print(set06)
set06 = set04 - set05  #  diferença de conjuntos
print(set06)
