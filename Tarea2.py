import numpy as np
import time
import matplotlib.pylab as plt
import random
#####Primer punto

#1) Funcion de Fibonacci usando recursividad, se tienen las condiciones iniciales que son las primeras dos condicones, es decir que el primer valor de la serie será igual a cero y el segundo valor será 1. En caso de que n sea un numero mayor a estos dos se usa entonces la formula de fibonacci.

def fib_recursion(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)

#2) Se crean dos listas vacias donde se van a almacenar los n (que irán de 1 a 40) y el tiempo que tarda en correr el código para cada uno de los n. Después de esto se crea el ciclo donde se da la orden que corra el codigo de fibonacci en el valor n y calcula la diferencia de tiempo en correr el código por cada iteracion. Para cada iteración se agregan los n y las diferencias de tiempo. Finalmente se plotea estas dos listas la cual resulta en una curva con comportamiento exponencial

list_n = []
list_time = []
for i in range(1,41):
    init= time.time()
    fib_recursion(i)
    difference = time.time()-init
    list_n.append(i)
    list_time.append(difference)

    
plt.figure(figsize=(10,6))
plt.plot(list_n, list_time, color = "red", marker = "2")
plt.xlabel("$N$")
plt.ylabel("$Difference$ $of$ $Time$")
plt.grid()
plt.savefig("Fibonacci")

#3) Se hace el mismo método de Fibonacci pero si usar recursivada para comparar el tiempo que tarda en correr el código para valores n mayores a 30, se repite el mismo proceso para mirar el tiempo que tarda en correr el codigo ahora sin recursividad y se plotea


def fibonacci(n):
    a = 1
    b = 0
    for i in range(1,n):
        b = a+b
        a = b
    return a

lista_n = []
lista_tiempo = []

for i in range(1,101):
    inicial = time.time()
    fibonacci(i)
    diferencia = time.time()-inicial
    lista_n.append(i)
    lista_tiempo.append(diferencia)
    
plt.figure(figsize=(10,6))
plt.plot(lista_n, lista_tiempo, color = "blue", marker = "o")
plt.xlabel("$N$")
plt.ylabel("$Difference$ $of$ $Time$")
plt.grid()
plt.savefig("Fibonacci_1")


#4) para este punto se crean dos listas donde se van a almacenar el valor de Fn+1/Fn y los n, según la grafica el unico valor difrerente es el primero el resto de valores converge a 2 lo cual quiere decir que hay un leve desfase en el calculo del n-ésimo valor de la serie de fibonacci.
list_rate=[]
l_n=[]
for i in range(1,101):
    rate = fibonacci(i+1)/fibonacci(i)
    list_rate.append(rate)
    l_n.append(i)
    
plt.figure()
plt.scatter(l_n, list_rate, color="green", alpha = 0.8)
plt.xlabel("$N$")
plt.ylabel("$Diferencia$  $Fn+1/Fn$")
plt.grid()
plt.savefig("Rate")


    
###ODEs

#1) primero se delcara la derivada que se va a estudiar en este caso, esta va a retornar la expresión dada en el enunciado

def funcion(y1,t1):
    return 2 - np.exp(-4*t1)-2*y1

#Acá declaro las condiciones iniciales y los arreglos necesarios para poder resolver la ecuacion diferencial
ini = 0
final = 1
puntos = 100
dy = (final-ini)/puntos
y= np.zeros(puntos)
t= np.zeros(puntos)


y[0]=1
t[0]=0

#FInalmente se crea el bucle que va a llenar los arreglos con la solución a la ecuacin diferencial, para esto se debe tomar el metodo de Euler el cual me actualiza la solución de un punto tomando el valor de la derivada en el punto anterior multiplicado por un delta.
for i in range(1,puntos):
    t[i]=t[i-1]+dy
    y[i]=y[i-1]+(dy*funcion(y[i-1],t[i-1]))

plt.figure()
plt.plot(t,y, color = "green", marker = "o")
plt.xlabel("$t$")
plt.ylabel("$y(t)$")
plt.grid()
plt.savefig("SolucionODE")

#solución matemática de la ecuacion diferencial, se usa para hallar el error del método de Euler.
def fun(y1,t1):
    return 1+0.5*np.exp(-4*t1)-0.5*np.exp(-2*t1)

plt.figure()
plt.plot(t,np.abs(fun(t,y)-y)/fun(t,y), marker="o")
plt.xlabel("$t$", size = 15)
plt.ylabel("$|y_{\\mathrm{true}}-y_{\\mathrm{ODE}}|$", size = 15)
plt.grid()
plt.savefig("Errores_ODE")

Ak = np.abs(fun(t,y)-y)/fun(t,y)
mean = np.sum(Ak)/(puntos+1)

print("El promedio de los errores es", mean)

#h más pequeño
inic = 0
final_ = 1
puntos_ = 250
d_y = (final_-inic)/puntos_
y_= np.zeros(puntos_)
t_= np.zeros(puntos_)

y_[0]=1
t_[0]=0

for i in range(1,puntos_):
    t_[i]=t_[i-1]+d_y
    y_[i]=y_[i-1]+(d_y*funcion(y_[i-1],t_[i-1]))

plt.figure()
plt.plot(t_,y_, color = "blue", marker = "o")
plt.xlabel("$t$")
plt.ylabel("$y(t)$")
plt.grid()
plt.savefig("SolucionODE_hmenor")

plt.figure()
plt.plot(t_,np.abs(fun(t,y_)-y_)/fun(t_,y_), marker="o")
plt.xlabel("$t$", size =15)
plt.ylabel("$|y_{\\mathrm{true}}-y_{\\mathrm{ODE}}|$", size = 15)
plt.grid()
plt.savefig("Errores_ODE_hmenor")

A_k = np.abs(fun(t,y_)-y_)/fun(t_,y_)
mean_1 = np.sum(A_k)/(puntos_+1)

print("El promedio de los errores con un h menor es", mean_1)

#El valor del error es un poco menor, lo que quiere decir que si se disminute el h a un valor muy muy pequeño, cercano a cero, el error también va a converger a cero.

#4) Lista de listas
lista1 = []
for i in range(4):
    lista1.append(random.randint(1,6))
print(lista1)
lista1 = np.sort(lista1)
print(lista1)
lista2 = []
for i in range(len(lista1)):
    lista2.append(np.zeros(lista1[i]))

for i in range(len(lista2[0])):
    lista2[0][i] = lista1[0]
for i in range(len(lista2[1])):
    lista2[1][i] = lista1[1]
for i in range(len(lista2[2])):
    lista2[2][i] = lista1[2]
for i in range(len(lista2[3])):
    lista2[3][i] = lista1[3]
print(lista2)





