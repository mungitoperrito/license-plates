import sqlite3
from sqlite3 import Error
import setup_database as setup
import helpers as lph
import os 

# TODO -- convert 'in' as input to 'na' for indiana
# TODO -- convert 'or' as input to 'ro' for oregon
# TODO -- read a file as input

def initialize(database):
    if os.path.exists(database):
        dbase = lph.connect_to_db(database)
    else:
        dbase = setup.initial_setup(database)    
        
    return dbase


def add_new_data(database):
    pass
    # Read file contents
    # Split entries
    # Update tables
    
    
def main(database):
    dbase = initialize(database)
    lph.check_contents(dbase, "names_mex")
    add_new_data(dbase)
    dbase.close()    

if __name__ == '__main__':
    database_name = "license_plates.db"   
    main(database_name)    
    
    


 # EOF