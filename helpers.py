''' Sets up the database tables if needed. '''

import sqlite3
from sqlite3 import Error

 
def connect_to_db(db_file):
    # sqlite will create a new dbase if none exists 
    try:      
        db_conn = sqlite3.connect(db_file)
        return db_conn
    except Error as e:
        print(e)


def execute_sql(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

        
def insert_rows(connection, sql, values):
    dbase_cursor = connection.cursor()   
    try:
        dbase_cursor.executemany(sql, values)
    except Error as e:
        print(e)
    
    connection.commit()



if __name__ == '__main__':
    # Connect to / create dbase
    test_dbase_name = "test_dbase.db"   
    test_dbase = connect_to_db(test_dbase_name)    
    
    # Add a table
    create_table_sql = """CREATE TABLE IF NOT EXISTS table1 (
        id integer PRIMARY KEY, col1 text, col2 int); """
    execute_sql(test_dbase, create_table_sql)

    # Update rows
    test_values = [("val1", 1), ("val2", 2), ("val3", 3)]    
    test_sql = """INSERT INTO table1 (col1, col2) VALUES(?,?); """
    insert_rows(test_dbase, test_sql, test_values)    
    
    # Check results
    results = test_dbase.execute("SELECT * FROM table1;")
    for r in results:
        print(r)
    
    # Close connections    
    test_dbase.close()


 # EOF