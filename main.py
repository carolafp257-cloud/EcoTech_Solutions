from src.clases import Empleado, Cliente, Producto, Pedido
from src.conexion import obtener_conexion

print("=== SISTEMA DE GESTION ECOTECH SOLUTIONS ===")
print("Iniciando pruebas de POO y Persistencia...\n")

empleado1 = Empleado("Maria Perez", "maria@ecotech.cl", "Analista", 650000)
cliente1 = Cliente("Juan Soto", "juan@correo.cl", "Constructora ABC")
producto1 = Producto("P001", "Panel solar", 150000, 20)

print("--- DATOS DEL EMPLEADO (OBJETO) ---")
empleado1.mostrar_datos()

print("\n--- CONECTANDO A ORACLE DATABASE ---")
conexion = obtener_conexion()

if conexion:
    print("Conexion exitosa con el usuario C##ECOTECH_SOLUTIONS!")
    try:
        with conexion.cursor() as cursor:
            
            print("\n[BD] Consultando tabla productos:")
            cursor.execute("SELECT codigo, nombre, precio, stock FROM productos")
            productos_bd = cursor.fetchall()
            for prod in productos_bd:
                print(f"Codigo: {prod[0]} | Producto: {prod[1]} | Precio: ${prod[2]} | Stock: {prod[3]}")
            
            print("\n[BD] Consultando tabla personas:")
            cursor.execute("SELECT nombre, correo, tipo_persona FROM personas")
            personas_bd = cursor.fetchall()
            for p in personas_bd:
                print(f"Tipo: {p[2]} | Nombre: {p[0]} | Correo: {p[1]}")
                
    except Exception as e:
        print("Error al ejecutar las consultas en la base de datos:", e)
    finally:
        conexion.close()
        print("\nConexion cerrada de forma segura.")
else:
    print("No se pudo establecer la conexion con la base de datos.")