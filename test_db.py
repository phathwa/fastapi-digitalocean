import pymysql

# Database connection parameters
host = '127.0.0.1'
user = 'root'
password = '_Phtmer&001'  # Use '%26' if you URL-encoded the password
database = 'test_db'
port = 3306

try:
    # Establish a connection to the database
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    print("Connection to the database was successful!")

except pymysql.MySQLError as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the connection if it was successful
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Connection closed.")
