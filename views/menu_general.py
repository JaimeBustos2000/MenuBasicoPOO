from views.Empleados.menu_empleados import menu_empleado
from views.Proyecto.menu_proyecto import proyecto
from views.Departamentos.menu_depto import menu_depto

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Gestion empleados")
        print("2. Gestion de proyectos")
        print("3. Gestionar departamentos")
        print("4. Salir")
        opcion = int(input("Elija una opcion: "))
        
        if opcion == 1:
            menu_empleado()
        elif opcion == 2:
            proyecto()
        elif opcion == 3:
            menu_depto()
        elif opcion == 4:
            break
        else:
            print("Opcion no valida, debe escoger un numero entre 1 y 4")