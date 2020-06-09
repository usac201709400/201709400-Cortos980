def collatz(number):                        #funcion para sacar los valores
    lista=[]
    while number != 1:                      #Se inicia la cuenta
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
