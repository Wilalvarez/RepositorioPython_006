#Crear menu con tres opciones
import os
def Numeros():
    #ingresar n numeros, donde n es un numero ingresado por teclado.
    #Mostrar: cantidad de numeros positivos, cantidad de negativos, cantidad de numeros iguales
    #a cero
    mayor=0
    menor=0
    igual=0

    cantidad=int(input("ingrese cantidad de números a ingresar: "))

    for i in range(cantidad):
        n=int(input(str(i)+".- Ingresa un número "))

        if (n>0):
            mayor+=1
        elif (n<0):
            menor+=1
        else:
            igual+=1
    
    print("cantidad de números positivos: "+str(mayor))
    print("cantidad de números negativos: "+str(menor))
    print("cantidad de 0: "+str(igual))
    tecla = input("Digite cualquier tecla para continuar: ")

def Personas():
    #ingresar para n personas: nombre y edad. Mostrar promedio de todas las edades ingresadas.
    nombre= ""
    edad= 0
    promedio = 0
    sumaed= 0

    personas=int(input("Ingrese la cantidad de personas: "))
    i=1
    while(i<=personas):
        nombre=str(input("Ingrese nombre de la persona: "))
        edad=int(input("Ingrese edad de la persona: "))
        sumaed = edad+sumaed
        i=i+1
    promedio=sumaed/personas
    print("El promedio de todas las edades es: " +str(promedio))    
    tecla = input("Digite cualquier tecla para continuar: ")

seguir=True 
while (seguir):
    os.system('cls')
    print("1. Numeros ")
    print("2. Datos Personales")
    print("3. Finalizar")
    op=int(input("Digite opción 1,2,3: "))
    if (op==1):
        Numeros()       #invocamos a un metodo
    if (op==2):
        Personas()
    if (op==3):
        print("Programa Finalizado")
        break