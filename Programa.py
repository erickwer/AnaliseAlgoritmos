import time
import timeit
import psutil
from memory_profiler import memory_usage
import os

#---------------------------------------------------------------#
#------------------------- BUBLE SORT 1 ------------------------#
#---------------------------------------------------------------#
lista = [456,567,3,78,467,57,5,76435,45,34,746,4]
inicioBublesort1 = timeit.default_timer()
def bublesort1(lista):
    qt_comp=0
    qt_troca=0
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            qt_comp+=1
            if lista[i] > lista[i+1]:
                qt_troca+=1
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    print("Quantidade de comparações: ",qt_comp)
    print("Quantidade de trocas: ",qt_troca)
    return lista
print("BUBLE SORT 1")
bublesort1(lista)
fimBublesort1 = timeit.default_timer()
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  #Uso de memória em GB

print('memory use:', memoryUse)
print("Tempo de execução Bublesort 1: %f "%(fimBublesort1 - inicioBublesort1))
print("Uso de CPU: ",psutil.cpu_percent(),"\n\n")

#---------------------------------------------------------------#
#------------------------- BUBLE SORT 2 ------------------------#
#---------------------------------------------------------------#

lista = [456,567,3,78,68,2,1,445786]
inicioBublesort2 = timeit.default_timer()
def bublesort2(lista):
    qt_comp=0
    qt_troca=0
    for j in range(len(lista)):
        for i in range(len(lista)-1,j, -1):
            qt_comp+=1
            if lista[i]<lista[i-1]:
                qt_troca+=1
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1]=aux
    print("Quantidade de comparações: ",qt_comp)
    print("Quantidade de trocas: ",qt_troca)          
    return lista
print("BUBLE SORT 2")
bublesort2(lista)
fimBublesort2 = timeit.default_timer()
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  #Uso de memória em GB
print('memory use:', memoryUse)
print("Tempo de execução Bublesort 1: %f "%(fimBublesort2 - inicioBublesort2))
print("Uso de CPU: ",psutil.cpu_percent(),"\n\n")

#---------------------------------------------------------------#
#------------------------- BUBLE SORT 3 ------------------------#
#---------------------------------------------------------------#

lista = [456,567,3,78,68,2,1,445786]
inicioBublesort3 = timeit.default_timer()
def bublesort3(lista):
    qt_comp=0
    qt_troca=0
    j=1
    troca = True
    while j<=len(lista) and troca:
        troca = False
        for i in range(len(lista)-1,0,-1):
            qt_comp+=1
            if (lista[i] < lista[i-1]):
                qt_troca+=1
                troca=True
                aux=lista[i]
                lista[i] = lista[i-1]
                lista[i-1]=aux
        j=j+1
    print("Quantidade de comparações: ",qt_comp)
    print("Quantidade de trocas: ",qt_troca)
    return lista
print("BUBLE SORT 3")
bublesort3(lista)
fimBublesort3 = timeit.default_timer()

pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  #Uso de memória em GB
print('memory use:', memoryUse)
print("Tempo de execução Bublesort 1: %f "%(fimBublesort3 - inicioBublesort3))
print("Uso de CPU: ",psutil.cpu_percent(),"\n\n")

#---------------------------------------------------------------#
#------------------------- INSERTION SORT ----------------------#
#---------------------------------------------------------------#

lista4 = [556,567,3,78,68,2,1,446]
inicioInsertionsort = timeit.default_timer()
def insertionSort(lista):
    qt_comp=0
    qt_troca=0
    for i in range(1, len(lista)):
        eleito = lista[i]
        j=i
        qt_comp+=1
        while(j>0)and(lista[j-1]>eleito):
            qt_troca+=1
            lista[j]=lista[j-1]
            j-=1
        lista[j] = eleito
    print("Quantidade de comparações: ",qt_comp)
    print("Quantidade de trocas: ",qt_troca)
    return lista
print("INSERTION SORT ")
insertionSort(lista4)
fimInsertionsort = timeit.default_timer()
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  #Uso de memória em GB
print('memory use:', memoryUse)
print("Tempo de execução Bublesort 1: %f "%(fimInsertionsort - inicioInsertionsort))
print("Uso de CPU: ",psutil.cpu_percent(),"\n\n")

#---------------------------------------------------------------#
#------------------------- SELECTION SORT ----------------------#
#---------------------------------------------------------------#

lista = [456,567,3,78,68,2,10,354,234326,445786]
inicioSelectionsort = timeit.default_timer()
def selectionSort(lista):
    qt_comp=0
    qt_troca=0
    for i in range(len(lista)-1):
        eleito=lista[i]
        menor=lista[i+1]
        pos=i+1
        for j in range(i+1,len(lista)):
            qt_comp=qt_comp+1
            if lista[j]<menor:
                qt_troca=qt_troca+1
                menor=lista[j]
                pos=j
        qt_comp=qt_comp+1
        if menor<eleito:
            qt_troca=qt_troca+1
            lista[i]=lista[pos]
            lista[pos]=eleito
    print("Quantidade de comparações: ",qt_comp)
    print("Quantidade de trocas: ",qt_troca)
    return lista
print("SELECTION SORT ")
selectionSort(lista)
fimSelectionsort = timeit.default_timer()
pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  #Uso de memória em GB
print('Uso de RAM:', memoryUse)
print("Tempo de execução Bublesort 1: %f4 "%(fimSelectionsort - inicioSelectionsort))
print("Uso de CPU: ",psutil.cpu_percent())




