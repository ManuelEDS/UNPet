import mysqlclient

# Configura las credenciales de la base de datos
db_host = "bmb72wbdmjin8klxpert-mysql.services.clever-cloud.com"
db_name = "bmb72wbdmjin8klxpert"
db_user = "uauvrvass9qcwgye"
db_password = "QqXd66YOtJMliLEquS2y"
db_port = 3306

try:
    # Intenta conectarse a la base de datos
    connection = mysqlclient.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        port=db_port
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
except mysqlclient.Error as error:
    # En caso de error, muestra un mensaje de error
    print(f"Error de conexión a la base de datos: {error}")
