import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # put your MySQL password here
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    cursor.close()
    connection.close()

except mysql.connector.Error as error:
    print("Error while connecting to MySQL:", error)
