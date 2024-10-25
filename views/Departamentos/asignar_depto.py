from controllers.clases import ConexionMySQL
def depto():
    conexion = ConexionMySQL()
    conn = conexion.obtener_conexion()
    
    """
    1) Obtener todos los empleados
    
    [empleado 1,empleado2, empleado3....]
    
    2) Consulta select para revisar que el empleado no tenga un departamento asignado
    
    SELECT id_empleado, id_departamento
    FROM empleado_departamento;
    """

    cursor = conn.cursor()
    
    while True:
        empleados = conexion.buscar_datos("empleados")
        departamentos = conexion.buscar_datos("departamentos")
    
        for i,empleado in enumerate(empleados):
            print(f"Empleado n°{i}: {empleado}")
            
        id_empleado = int(input("Seleccione el empleado: "))
        
        cursor.execute(f"SELECT empleado_id FROM empleado_departamento WHERE empleado_id = {id_empleado}")
        resultado = cursor.fetchone()
        
        if resultado:
            print("El empleado ya tiene depto")
        else:
            # Aqui se muestran los diferentes empleados
            for i,depto in enumerate(departamentos):
                print(f"Empleado n°{i}: {depto}")
                
            id_depto = int(input("Seleccione el departamento: "))
            
            
            """
            1) Verificar la id_depto si existe en la tabla empleado_departamento
            2) Asignar el depto al empleado con su id
            """