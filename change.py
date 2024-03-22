def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    vuelto = money - expense
    print("")
    print("Pesos:")
    pesos = int(vuelto)
    print (pesos)
    print("Centavos:")
    centavos = (vuelto - pesos)*100
    print(int (centavos))

change()
