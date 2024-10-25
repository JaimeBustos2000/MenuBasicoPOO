from mysql.connector import connect

# AQUI DEBERIAN IR LOS METODOS GENERALES PARA MANIPULAR LA BASE DE DATOS

# Ejemplo aplicado a una clase de vehiculos
""" 
# Encapsulamiento y abstraccion

Transformamos elementos o comportamientos de la vida real en clases y objetos (abstraccion)
Solo permitimos ver o editar atributos atravez de metodos(encapsulamiento)(getters y setters)


La clase vehiculo es una clase padre, las clases padre son utiles como moldes para las clases hijas
estas clases hijas heredan los atributos y metodos de la clase padre, pero tambien pueden tener sus propios atributos y metodos



class Vehiculo:
    def __init__(self,color, marca):
        self.color = color
        self.marca = marca
        
    def obtener_datos(self):
        return f"Detalles del vehiculo: {self.color} -- {self.marca}"
        
        
Las clases pueden obtener atributos y metodos de otras clases (herencia)
La clase Automovil hereda de la clase Vehiculo, por tanto tiene los atributos y metodos de la clase Vehiculo
pero tambien tiene sus propios atributos y metodos

Una clase puede tener metodos que se llamen igual que los metodos de la clase padre, 
pero que tengan un comportamiento diferente (poliformismo)

# Herencia y poliformismo
class Automovil(Vehiculo):
    def __init__(self, color, marca,velocidad,cant_pasajeros):
        super().__init__(color, marca)
        self.velocidad = velocidad
        self.cantpasajeros = cant_pasajeros

    def detalles(self):
        return f''' Detalles: 
    color : {self.color}
    marca : {self.marca}
    velocidad : {self.velocidad}
    cantidad_pasejeros : {self.cantpasajeros}'''
    

auto = Automovil("blanco","Mazda","240km",10)

print(auto.detalles())

################################


SELECT *
FROM TABLA;

def consultar(self,nombre_tabla=""):
    cursor = self.conexion.cursor()

    if nombre_tabla="":
        return print("NO SE SELECCIONO NINGUNA TABLA")
    else:
        cursor.execute(f"SELECT * FROM {tabla}")
    pass

"""

class ConexionMySQL:
    def __init__(self):
        self.nombre = "basedeDatos"
        self.usuario = "root"
        self.contrasena = "1234"
        self.host = "localhost"
        self.puerto = "3306"
        self.conexion = self.conectar()
        
    def conectar(self):
        try:
            conexion = connect(
                host=self.host,
                user=self.usuario,
                passwd=self.contrasena,
                database=self.nombre
            )
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos")
    
    def obtener_conexion(self):
        return self.conexion
    
    def desconectar(self, conexion):
        conexion.close()
        
    def buscar_datos(self,tabla=""):

        cursor = self.conexion.cursor()
        if tabla == "":
            return print("ERROR")
        else:
            cursor.execute(f"SELECT * FROM {tabla}")
            return cursor.fetchall()

    def insertar_datos(self, conexion, tabla, datos):
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO {tabla} VALUES {datos}")
        conexion.commit()
        
    def eliminar_datos(self, conexion, tabla, condicion):
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM {tabla} WHERE id = {condicion}")
        conexion.commit()
        
    def actualizar_datos(self, conexion, tabla, datos, condicion):
        cursor = conexion.cursor()
        cursor.execute(f"UPDATE {tabla} SET {datos} WHERE id = {condicion}")
        conexion.commit()

conexion = ConexionMySQL()

print(conexion.buscar_datos())

# Archivo para empleados        
class Empleados(ConexionMySQL):
    def __init__(self):
        super().__init__()
        self.tabla = "empleados"
        
    def seleccionar_empleados(self):
        conexion = self.conectar()
        empleados = self.buscar_datos(conexion, self.tabla)
        self.desconectar(conexion)
        return empleados
    
    def insertar_empleado(self, datos):
        conexion = self.conectar()
        self.insertar_datos(conexion, self.tabla, datos)
        self.desconectar(conexion)

    def eliminar_empleado(self, condicion):
        conexion = self.conectar()
        self.eliminar_datos(conexion, self.tabla, condicion)
        self.desconectar(conexion)
    
    def actualizar_empleado(self, datos, condicion):
        conexion = self.conectar()
        self.actualizar_datos(conexion, self.tabla, datos, condicion)
        self.desconectar(conexion)


"""
Aqui se reutiliza la clase ConexionMySQL para departamentos
la que tiene los diferentes metodos para operar con la base de datos
aqui no se deberia generar una conexion nueva, sino que se deberia reutilizar la conexion
de la clase principal por tanto usar la clase principal y guardar el objeto en una variable
para pasarlo atravez de los menus


1) Definir que operaciones se pueden hacer con los departamentos
2) Crear un menu para departamentos
3) Realizar pruebas de insercion, eliminacion y actualizacion de datos

"""
# archivo para departamentos
class Departamentos(ConexionMySQL):
    def __init__(self):
        super().__init__()
        self.tabla = "departamentos"
        
    def lista_deptartamentos(self):
        conexion = self.conectar()
        departamentos = self.buscar_datos(conexion, self.tabla)
        self.desconectar(conexion)
        return departamentos
    
    def insertar_departamento(self, datos):
        conexion = self.conectar()
        self.insertar_datos(conexion, self.tabla, datos)
        self.desconectar(conexion)
        
    def eliminar_departamento(self, condicion):
        conexion = self.conectar()
        self.eliminar_datos(conexion, self.tabla, condicion)
        self.desconectar(conexion)
        
    def actualizar_departamento(self, datos, condicion):
        conexion = self.conectar()
        self.actualizar_datos(conexion, self.tabla, datos, condicion)
        self.desconectar(conexion)
