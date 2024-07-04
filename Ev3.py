import Funciones as func
Lista = []
while True:
    op = func.menu()
    if op == "1":
        func.generar_pedido(Lista)
    elif op == "2":
        func.listar_pedidos(Lista)
    elif op == "3":
        func.imprimir(Lista)
    elif op == "4":
        func.imprimir_ID(Lista)
    elif op == "5":
        print("Saliendo del sistema...")
        break