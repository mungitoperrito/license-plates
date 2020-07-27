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


def add_new_data(database, lplates_file):
    #print(f"LPF: {lplates_file}")
    # Process lines one by one b/c a given date may have multiple entries
    print("HOLA")
    with open(lplates_file) as input_file:
        for line in input_file.readline():
            print(line)
        # Read file contents
    # Split entries
    # Update tables
    
    
def main(database, lplates_file):
    dbase = initialize(database)
    #lph.check_contents(dbase, "names_can")
    add_new_data(dbase, lplates_file)
    dbase.close()    




if __name__ == '__main__':
    database_name = "license_plates.db"
    license_plates_file = "license-plates-input.txt"
    main(database_name, license_plates_file)
    
    


 # EOF