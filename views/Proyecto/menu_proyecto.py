# Description: Contiene las vistas de la sección de proyectos
def proyecto(conexion):
    
    while True:
        print("""
1. Crear proyecto
2. Editar proyecto
3. Eliminar proyecto
4. Listar proyectos
5. Volver
""")
        opcion = int(input("Elija una opcion: "))
        
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            break
        else:
            print("Opcion no valida, debe escoger un numero entre 1 y 5")