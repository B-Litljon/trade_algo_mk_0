import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def make_connection():
    # Set up MySQL connection credentials
    host = os.getenv('MYSQL_HOST')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    database = os.getenv('MYSQL_DATABASE')

    # Connect to MySQL server
    try:
        cnx = mysql.connector.connect(user=user, password=password,
                                      host=host, database=database)
        print(f"connection to: {database} was successful")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error connecting to mysql server: {err}")
        return None
