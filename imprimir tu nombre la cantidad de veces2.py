#created by pradelson francois on 29/3/2021
from time import sleep

nombre = input("Escribe tu nombre por favor:")

vecesPorPantalla = int(input("cuantas veces quieres que se imprima tu nombre por pantalla?:"))

for i in range(vecesPorPantalla):
  if i==1:
    print("imprimiendo " + nombre + " en pantalla......\n")
    sleep(2)  
    print(nombre + " se ha imprimido " + str(i) + " vez!")
  elif i>=2:
    print(nombre + " se ha imprimido " + str(i) + " veces!")  

else:
  print("Tu nombre se ha imprimido " +
  str(i) + " veces " + nombre)
