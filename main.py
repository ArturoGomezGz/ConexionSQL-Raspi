import mysql.connector
from mysql.connector import Error

try:
    # Establecer conexión con MySQL
    conexion = mysql.connector.connect(
        host='localhost',      # Cambia esto si te conectas a un servidor remoto
        user='arturo',     # Usuario de MySQL
        password='Pword1',  # Contraseña de MySQL
        database='SemaforoInteligente'  # Base de datos que quieres usar
    )
    
    if conexion.is_connected():
        print("Conexión exitosa a MySQL")

        # Crear un cursor para ejecutar consultas
        cursor = conexion.cursor()

        # Ejecutar una consulta simple
        consulta = "SELECT * FROM Semaforo;"  # Cambia esta consulta por la que necesites
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        print("Base de datos actual:", resultado)

except Error as e:
    print("Error al conectar a MySQL:", e)

finally:
    # Cerrar la conexión a la base de datos
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión a MySQL cerrada")
