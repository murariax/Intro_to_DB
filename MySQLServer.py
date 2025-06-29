# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update with your credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Use CREATE DATABASE IF NOT EXISTS to avoid failure if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
