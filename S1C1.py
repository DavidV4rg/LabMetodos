import numpy as np

lista = [5,3,2,8,1,4]
print (lista)

#Primer punto
for i in range (len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]: 
            if lista[i]%2 != 0 and lista[j]%2 !=0:
                var = lista[i]
                lista[i] = lista[j]
                lista[j] = var
print(lista)

#Segundo punto
print ("")
l= [5,3,2,8,1,4]
print (l)

for i in range (len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]: 
            if l[i]%2 != 0 and l[j]%2 !=0:
                variable = l[i]
                l[i] = l[j]
                l[j] = variable
        else:
            if l[i]%2==0 and l[j]%2 ==0:
                variable = l[j]
                l[j] = l[i]
                l[i] = variable                            
                             
print(l)
        