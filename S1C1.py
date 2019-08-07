import numpy as np

lista = [5,3,2,8,1,4]
print (lista)
for i in range (len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]: 
            if lista[i]%2 != 0 and lista[j]%2 !=0:
                var = lista[i]
                lista[i] = lista[j]
                lista[j] = var
print(lista)

                
          