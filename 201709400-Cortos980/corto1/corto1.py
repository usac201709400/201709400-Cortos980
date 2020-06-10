def collatz(number):                        #funcion para sacar los valores
    lista=[]# no realiza nada en todo el codigo
    while number != 1:                      #Se inicia la cuenta, cuenta?
        if number % 2 == 0:                 #se especifica las condiciones
            number = number // 2
            print(number)
            lista.append(number)

        elif number % 2 == 1:
            number = number * 3 + 1
            print(number)
            lista.append(number)

try:
    num = int(input("Please pick any whole number to see the Collatz Sequence in action.n"))
    collatz(num)                                #Se implementa la funcion
except ValueError:
    print("Please use whole numbers only.")

#que casualidad se ve muy parecido al codigo dentro de esta pagina
#https://living-sun.com/es/python/686209-collatz-sequence-python-sequence-collatz.html

#Funcionamiento:        0/40
#Uso de Funciones       0/20
#Manejo de archivos     0/10
#Manejo de Listas       0/10
#Uso de git             20/20
#*****************************
#Total                  20/100

