import config, random, os, csv
comunas = ["Concepción","Chihuayante","Talcahuano","Hualpén","San Pedro"]
def Generar_ID():
    return random.randint(100000,999999)
def menu():
    valor = 1
    print("*********************")
    for i in config.opciones:
        print(f"{valor}. {i}")
        valor += 1
    print("*********************")
    op = input("Opción: ")
    return op
def generar_pedido(lista):
    os.system("cls")
    ID = Generar_ID()
    while True:
        nombre = input("Nombre: ")
        if len(nombre) > 0 and nombre.isalpha() == True:
            break
        else:
            print("Nombre no valido")
    while True:
        apellido = input("Apellido: ")
        if len(apellido) > 0 and apellido.isalpha() == True:
            break
        else:
            print("Apellido no valido")
    while True:
        calle = input("Calle: ")
        if len(calle) > 0:
            break
        else:
            print("Calle no valida")
    while True:
        try:
            num_casa = int(input("Número de casa: "))
            if num_casa > 0:
                break
            else:
                print("Número debe ser positivo")
        except:
                print(num_casa)
                print("Debe ingresar un número")
    while True:
        comuna = input("Comuna: ")
        if len(comuna) > 0 and comuna.isalpha() == True:
            break
        else:
            print("Dato no valido")
    while True:
        try:
            l6 = int(input("Cantidad dispensadores (6lts): "))
            l10 = int(input("Cantidad dispensadores (10lts): "))
            l20 = int(input("Cantidad dispensadores (20lts): "))
            if (l6 + l10 + l20) > 0:
                break
            else:
                print("Debe de pedir por lo menos un dispensador")
        except:
            print("Debe ingresar un número")
    lista.append([ID,nombre,apellido,calle,num_casa,comuna,l6,l10,l20])
    os.system("cls")
def listar_pedidos(lista):
    os.system("cls")
    print("ID Pedido\tCliente\tDirección\tSector\tDisp.6lts\tDisp.10lts\tDisp.20lts")
    for i in lista:
        print(f"\n{i[0]}\t{i[1]} {i[2]}\t{i[3]} {i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}")
def imprimir(lista):
    os.system("cls")
    while True:
        buscar_comuna = input("¿En que comúna realizar el envio?: ")
        if len(buscar_comuna) > 0:
            break
        else:
            print("No valido")
    try:
            with open("Planilla.csv","w",newline='') as archivo:
             escritor = csv.writer(archivo)
             escritor.writerow("ID Pedido\tCliente\tDireccion\tSector\tDisp.6lts\tDisp.10lts\tDisp.20lts")
             for i in comunas:
                    if i == buscar_comuna:
                        for e in lista:
                            if e[5] == buscar_comuna:
                                escritor.writerow(f"{e[0]}\t{e[1]} {e[2]}\t{e[3]} {e[4]}\t{e[5]}\t{e[6]}\t{e[7]}\t{e[8]}")
                    else:
                        continue

    except:
            print("Error al imprimir la planilla")
def imprimir_ID(lista):
    while True:
        try:
            buscar_ID = (input("¿ID del envio?: "))
            if len(buscar_ID) == 6 and buscar_ID.isalnum() == True:
                break
            else:
                print("Debe ingresar un codigo de 6 digitos")
                
        except:
            print("Dato no valido")
    try:
            with open("Planilla.csv","w",newline='') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow("ID Pedido\tCliente\tDireccion\tSector\tDisp.6lts\tDisp.10lts\tDisp.20lts\n")
                for e in lista:
                    if e[0] == int(buscar_ID):
                        escritor.writerow(f"{e[0]}\t{e[1]} {e[2]}\t{e[3]} {e[4]}\t{e[5]}\t{e[6]}\t{e[7]}\t{e[8]}")
    except:
            print("Error al imprimir la planilla")
    os.system("cls")