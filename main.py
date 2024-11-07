import pyodbc

# Conectar a SQL Server
conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=pruebas;UID=arturo;PWD=Pword1'
)

# Ejecutar una consulta
cursor = conexion.cursor()
cursor.execute("SELECT * FROM tu_tabla")
for fila in cursor.fetchall():
    print(fila)

# Cerrar la conexión
conexion.close()
