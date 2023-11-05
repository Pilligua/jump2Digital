import mysql.connector

conexion = mysql.connector.connect(user='root', password='root', host='localhost',database='pruebaPython', port=3306)
cursor = conexion.cursor()