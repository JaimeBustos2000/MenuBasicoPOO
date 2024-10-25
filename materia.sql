-- Crear la base de datos
CREATE DATABASE sistema_empleados;

-- Usar la base de datos
USE sistema_empleados;

-- Tabla para los empleados
CREATE TABLE empleados (
    empleado_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_inicio DATE,
    salario DECIMAL(10, 2),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(departamento_id)
);

-- Tabla para los departamentos
CREATE TABLE departamentos (
    departamento_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    gerente VARCHAR(100)
);

-- Tabla para los proyectos
CREATE TABLE proyectos (
    proyecto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE
);

-- Tabla para asignar empleados a proyectos
CREATE TABLE empleado_proyecto (
    empleado_id INT,
    proyecto_id INT,
    PRIMARY KEY (empleado_id, proyecto_id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(empleado_id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(proyecto_id)
);

-- Tabla para registrar horas trabajadas
CREATE TABLE registro_tiempo (
    registro_id INT AUTO_INCREMENT PRIMARY KEY,
    empleado_id INT,
    fecha DATE,
    horas_trabajadas DECIMAL(5, 2),
    descripcion TEXT,
    FOREIGN KEY (empleado_id) REFERENCES empleados(empleado_id)
);

INSERT INTO departamentos (nombre, gerente) VALUES 
('Desarrollo Sostenible', 'Carlos Pérez'),
('Investigación y Desarrollo', 'María López'),
('Ventas', 'Juan Martínez'),
('Recursos Humanos', 'Ana Gómez');


INSERT INTO empleados (nombre, direccion, telefono, email, fecha_inicio, salario, departamento_id) VALUES 
('Laura Torres', 'Calle Falsa 123', '555-1234', 'laura@ejemplo.com', '2023-01-15', 3500.00, 1),
('Pedro Sánchez', 'Avenida Siempre Viva 456', '555-5678', 'pedro@ejemplo.com', '2023-02-20', 4200.00, 2),
('Lucía Fernández', 'Boulevard de los Sueños 789', '555-8765', 'lucia@ejemplo.com', '2023-03-10', 3800.00, 3),
('Javier Ramírez', 'Plaza Mayor 12', '555-4321', 'javier@ejemplo.com', '2023-04-25', 3000.00, 4);


INSERT INTO proyectos (nombre, descripcion, fecha_inicio) VALUES 
('Proyecto Alpha', 'Desarrollo de nuevas funcionalidades.', '2023-05-01'),
('Proyecto Beta', 'Investigación de mercado.', '2023-06-15'),
('Proyecto Gamma', 'Lanzamiento de campaña de ventas.', '2023-07-10');

INSERT INTO empleado_proyecto (empleado_id, proyecto_id) VALUES 
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(1, 3);


INSERT INTO registro_tiempo (empleado_id, fecha, horas_trabajadas, descripcion) VALUES 
(1, '2023-05-10', 8.0, 'Desarrollo de funcionalidades del Proyecto Alpha.'),
(2, '2023-05-10', 7.5, 'Investigación de mercado para Proyecto Beta.'),
(3, '2023-05-10', 6.0, 'Revisión de ventas del Proyecto Gamma.'),
(4, '2023-05-10', 5.5, 'Análisis de recursos humanos para el nuevo proyecto.');
