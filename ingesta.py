import boto3
import csv
import mysql.connect

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="54.152.40.39",      # Dirección del servidor MySQL
    user=3307,   # Tu usuario de MySQL
    password=1234,  # Tu contraseña de MySQL
    database="empresa"  # Tu base de datos
)

# Crear un cursor
cursor = conexion.cursor()

# Consultar todos los registros de la tabla
cursor.execute("SELECT * FROM personas")

# Obtener todos los registros
registros = cursor.fetchall()

# Guardar los registros en un archivo CSV
ficheroUpload = "data.csv"
with open(ficheroUpload, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Escribir los nombres de las columnas (si es necesario)
    writer.writerow([i[0] for i in cursor.description])  
    # Escribir los registros
    writer.writerows(registros)

# Subir el archivo CSV a un bucket S3
nombreBucket = "jos-output-1"
s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada")
