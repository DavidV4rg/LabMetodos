import numpy as np
import time
import matplotlib.pylab as plt

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

#1) primero se delcara la función que se va a estudiar en este caso

def funcion(y,t):
    return 2 - np.exp(-4*t)-2*y
    
    

    
    
    
    
    
    
    
    
    
    