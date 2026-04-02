from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print("\n" + "=" * 40)
    print("   SISTEMA AVANZADO DE INVENTARIO")
    print("=" * 40)
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad/precio")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todo el inventario")
    print("6. Salir")
    return input("\nSeleccione una opción: ")


def ejecutar():
    inv = Inventario()

    while True:
        op = mostrar_menu()

        if op == "1":
            id_p = input("ID: ")
            nom = input("Nombre: ")
            try:
                can = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                inv.añadir_producto(Producto(id_p, nom, can, pre))
                print("¡Producto añadido!")
            except ValueError:
                print("Error: Cantidad y Precio deben ser números.")

        elif op == "2":
            id_p = input("ID del producto a eliminar: ")
            inv.eliminar_producto(id_p)
            print("Proceso terminado.")

        elif op == "3":
            id_p = input("ID del producto: ")
            try:
                c_str = input("Nueva Cantidad (vacío para omitir): ")
                p_str = input("Nuevo Precio (vacío para omitir): ")
                can = int(c_str) if c_str else None
                pre = float(p_str) if p_str else None
                inv.actualizar_producto(id_p, can, pre)
                print("Datos actualizados.")
            except ValueError:
                print("Error: Datos inválidos.")

        elif op == "4":
            nom = input("Nombre a buscar: ")
            resultados = inv.buscar_nombre(nom)
            if resultados:
                for p in resultados: print(p)
            else:
                print("No se encontraron coincidencias.")

        elif op == "5":
            print("\n--- LISTADO DE INVENTARIO ---")
            productos = inv.obtener_todos()
            if productos:
                for p in productos: print(p)
            else:
                print("El inventario está vacío.")

        elif op == "6":
            print("Cerrando sistema... ¡Adiós!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    ejecutar()