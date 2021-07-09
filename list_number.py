lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#itera sobre la lista
for num in lista_1:
    if (num % 2) == 0:  #si se puede dividir entre 2
        print("{0} es par".format(num))  
    else:  
        print("{0} es impar".format(num))
