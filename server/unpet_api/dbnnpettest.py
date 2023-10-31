import mysql.connector

try:
    # Intenta conectarse a la base de datos
    connection = mysql.connector.connect(
        host="bmb72wbdmjin8klxpert-mysql.services.clever-cloud.com",
        user="uauvrvass9qcwgye",
        password="Zx80kAeYM8J6lEiuh64W",
        database="bmb72wbdmjin8klxpert",
        port=3306
    )

    # Si la conexión tiene éxito, muestra un mensaje
    print("Conexión exitosa a la base de datos MySQL en Clever Cloud")

    # Obtiene el cursor para ejecutar consultas
    cursor = connection.cursor()

    # Ejecuta la consulta para obtener todas las tablas de la base de datos
    cursor.execute("SHOW TABLES")

    # Obtiene los resultados de la consulta
    tables = cursor.fetchall()

    # Imprime las tablas de la base de datos
    print("Tablas de la base de datos:")
    for table in tables:
        print(table[0])
    # Cierra la conexión a la base de datos
    connection.close()
except mysql.connector.Error as error:
    # En caso de error, muestra un mensaje de error
    print(f"Error de conexión a la base de datos: {error}")
