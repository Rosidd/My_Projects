import mysql.connector
from mysql.connector import Error
 
def get_db_connection():
     try:
         connection = mysql.connector.connect(
             host='localhost',
             database='new_schema',
             user='root',
             password='password'
         )
         return connection
     except Error as e:
         raise RuntimeError(f"Error connecting to MySQL: {e}")
         