def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto: ")
    print(expense)
    print("Dinero recibido: ")
    print(money)
    print("\n")
    print("Vuelto")
    vuelto = money - expense
    print("\n")
    print("Pesos: ")
    pesos = int(vuelto)
    print (pesos)
    print("Centavos: ")
    centavos = (pesos - vuelto)*-100
    print(int (centavos))

change()
