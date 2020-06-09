'''
def Coll(num):
    all_seq = []
        while (n > 1):
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            all_seq.append(n)
            print(all_seq)
    return lista


for n in range(2,400):
    all_seq = []
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    all_seq.append(n)
    print(all_seq)


 while numero != 1:
        if numero % 2 == 0:
        print("%d," % (numero), end = "")
        numero = numero / 2
    else:
        print("%d," % (numero), end = "")
        numero = (numero * 3) + 1

    if numero == 1:
        print("1")

for i in range(2,400):
    total=[]
    numero=i
    while numero != 1:
        lista=[]
        if numero % 2 == 0:
            numero = numero / 2
            lista.append(numero)
        else:
            numero = (numero * 3) + 1
            lista.append(numero)
        if numero == 1:
            lista.append(numero)
        total.append(lista)
        '''


def sist(num):
    lista=[]     
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    lista.append(n) 
    return lista

for i in range(2,400):
    n=i
    while(n>1):
        sist(n)
    total.append(lista)
