from views.Departamentos.asignar_depto import depto

def menu_empleado():
    while True:
        print("""
1. Añadir empleado
2. Editar empleado
3. Asignar proyecto
4. Registrar hora
5. Vincular depto
              """)
        opcion =int(input("Elija una opcion: "))
        
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            depto()
            pass