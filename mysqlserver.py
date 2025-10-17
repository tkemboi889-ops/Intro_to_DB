# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    
    try:
        # Step 1: Connect to MySQL Server (not a specific database yet)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Kenboi3482&'  # 🔒 Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Step 2: Create the database (safe if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("✅ Database 'alx_book_store' created successfully!")

    except Error as e:
        # Step 3: Handle errors gracefully
        print(f"❌ Error while connecting to MySQL: {e}")

    finally:
        # Step 4: Close the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 MySQL connection is closed.")

# Run the function when script is executed
if __name__ == "__main__":
    create_database()
