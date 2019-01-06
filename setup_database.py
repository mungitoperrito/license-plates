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


def create_trip_data_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS trip_data (
        trip_id integer PRIMARY KEY, trip_date text, trip_day int, 
        trip_start text, trip_end text, trip_distance int, 
        total_us int default 0, total_mex int default 0, 
        total_can int default 0, total_other int default 0, 
        total_plates int default 0 ); """
    execute_sql(connection, create_table_sql)

                                    
def create_plates_us_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS plates_us(
        trip_id integer PRIMARY KEY, trip_total integer default 0,
        al integer default 0, ak integer default 0, az integer default 0,
        ar integer default 0, ca integer default 0, co integer default 0,
        ct integer default 0, dc integer default 0, de integer default 0,
        fl integer default 0, ga integer default 0, hi integer default 0,
        id integer default 0, il integer default 0, na integer default 0,
        ia integer default 0, ks integer default 0, ky integer default 0,
        la integer default 0, me integer default 0, md integer default 0,
        ma integer default 0, mi integer default 0, mn integer default 0,
        ms integer default 0, mo integer default 0, mt integer default 0,
        ne integer default 0, nv integer default 0, nh integer default 0,
        nj integer default 0, nm integer default 0, ny integer default 0,
        nc integer default 0, nd integer default 0, oh integer default 0,
        ok integer default 0, ro integer default 0, pa integer default 0,
        ri integer default 0, sc integer default 0, sd integer default 0,
        tn integer default 0, tx integer default 0, ut integer default 0,
        vt integer default 0, va integer default 0, wa integer default 0,
        wv integer default 0, wi integer default 0, wy integer default 0,
        di integer default 0, gv integer default 0, gu integer default 0,
        it integer default 0, ml integer default 0, pr integer default 0,
        vi integer default 0 ); """
    execute_sql(connection, create_table_sql)
    
    
def create_plates_mex_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS plates_mex(
        trip_id integer PRIMARY KEY, trip_total integer default 0,
        agua integer default 0, baja integer default 0, bajs integer default 0,
        chih integer default 0, coli integer default 0, camp integer default 0,
        coah integer default 0, chia integer default 0, cdmx integer default 0,
        dura integer default 0, guer integer default 0, guan integer default 0,
        hida integer default 0, jali integer default 0, edmx integer default 0,
        mich integer default 0, more integer default 0, naya integer default 0,
        nleo integer default 0, oaxa integer default 0, pueb integer default 0,
        quer integer default 0, quin integer default 0, sina integer default 0,
        slpo integer default 0, sono integer default 0, taba integer default 0,
        tlax integer default 0, tama integer default 0, vera integer default 0,
        yuca integer default 0, zaca integer default 0 ); """
    execute_sql(connection, create_table_sql)
    
    
def create_plates_can_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS plates_can(
        trip_id integer PRIMARY KEY, trip_total integer default 0,
        alb integer default 0, brc integer default 0, man integer default 0,
        nbr integer default 0, new integer default 0, nwt integer default 0,
        nsc integer default 0, nun integer default 0, ont integer default 0,
        pwi integer default 0, que integer default 0, sas integer default 0,
        yuk integer default 0 ); """
    execute_sql(connection, create_table_sql)
    
    
def create_plates_other_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS plates_other(
                                    trip_id integer PRIMARY KEY,
                                    trip_total integer default 0,
                                    other_plate integer default 0
                                    ); """
    execute_sql(connection, create_table_sql)
    
    
def create_names_us_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS names_us(
                                    id integer PRIMARY KEY,
                                    short_name text NOT NULL,
                                    long_name text NOT NULL
                                    ); """
    execute_sql(connection, create_table_sql)

    
    abreviation_key = \
      [("al", "alabama"),("ak", "alaska"),("az", "arizona"),("ar", "arkansas"),
       ("ca", "california"),("co", "colorado"),("ct", "connecticut"),
       ("dc", "dist of colombia"),("de", "delaware"),("fl", "florida"),
       ("ga", "georgia"),("hi", "hawaii"),("id", "idaho"),("il", "illinois"),
       ("na", "indiana"),("ia", "iowa"),("ks", "kansas"),("ky", "kentucky"),
       ("la", "louisiana"),("me", "maine"),("md", "maryland"),
       ("ma", "massachusetts"),("mi", "michigan"),("mn", "minnesota"),
       ("ms", "mississippi"),("mo", "missouri"),("mt", "montana"),
       ("ne", "nebraska"),("nv", "nevada"),("nh", "new hampshire"),
       ("nj", "new jersey"),("nm", "new mexico"),("ny", "new york"),
       ("nc", "north carolina"),("nd", "north dakota"),("oh", "ohio"),
       ("ok", "oklahoma"),("ro", "oregon"),("pa", "pennsylvania"),
       ("ri", "rhode island"),("sc", "south carolina"),("sd", "south dakota"),
       ("tn", "tennessee"),("tx", "texas"),("ut", "utah"),("vt", "vermont"),
       ("va", "virginia"),("wa", "washington"),("wv", "west virginia"),
       ("wi", "wisconsin"),("wy", "wyoming"),("di", "diplomat"),
       ("gv", "government"),("gu", "guam"),("it", "indian territory"),
       ("ml", "military"),("pr", "puerto rico"),("vi", "virgin islands")]

    update_sql = """INSERT INTO names_us (short_name, long_name)
                    VALUES(?, ?)"""
    
    insert_rows(connection, update_sql, abreviation_key)

    
def create_names_mex_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS names_mex(
                                    id integer PRIMARY KEY,
                                    short_name text NOT NULL,
                                    long_name text NOT NULL
                                    ); """
    execute_sql(connection, create_table_sql)
    
    abreviation_key = \
      [("agua", "Aguascalientes"),("baja", "Baja California"),
       ("bajs", "Baja California Sur"),("chih", "Chihuahua"),("coli", "Colima"),
       ("camp", "Campeche"),("coah", "Coahuila"),("chia", "Chiapas"),
       ("cdmx", "Federal District"),("dura", "Durango"),("guer", "Guerrero"),
       ("guan", "Guanajuato"),("hida", "Hidalgo"),("jali", "Jalisco"),
       ("edmx", "México State"),("mich", "Michoacán"),("more", "Morelos"),
       ("naya", "Nayarit"),("nleo", "Nuevo León"),("oaxa", "Oaxaca"),
       ("pueb", "Puebla"),("quer", "Querétaro"),("quin", "Quintana Roo"),
       ("sina", "Sinaloa"),("slpo", "San Luis Potosí"),("sono", "Sonora"),
       ("taba", "Tabasco"),("tlax", "Tlaxcala"),("tama", "Tamaulipas"),
       ("vera", "Veracruz"),("yuca", "Yucatán"),("zaca", "Zacatecas")]

    update_sql = """INSERT INTO names_mex (short_name, long_name)
                    VALUES(?, ?)"""
    
    insert_rows(connection, update_sql, abreviation_key)


def create_names_can_table(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS names_can(
                                    id integer PRIMARY KEY,
                                    short_name text NOT NULL,
                                    long_name text NOT NULL
                                    ); """
    execute_sql(connection, create_table_sql)
    
    abreviation_key = \
      [("alb", "Alberta"),("brc", "British Columbia"),("man", "Manitoba"),
       ("nbr", "New Brunswick"),("new", "Newfoundland and Labrador"),
       ("nwt", "Northwest Territories"),("nsc", "Nova Scotia"),
       ("nun", "Nunavut"),("ont", "Ontario"),("pwi", "Prince Edward Island"),
       ("que", "Quebec"),("sas", "Saskatchewan"),("yuk", "Yukon")]
    
    update_sql = """INSERT INTO names_can (short_name, long_name)
                    VALUES(?, ?)"""
    
    insert_rows(connection, update_sql, abreviation_key)
    
    
def create_day_names_(connection):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS day_names(
                                    day_number integer PRIMARY KEY,
                                    day_name text NOT NULL
                                    ); """
    execute_sql(connection, create_table_sql)
    
    abreviation_key = \
      [(1, "Monday"),(2, "Tuesday"),(3, "Wednesday"),(4, "Thursday"),
       (5, "Friday"),(6, "Saturday"),(7, "Sunday")]
    
    update_sql = """INSERT INTO day_names (day_number, day_name)
                    VALUES(?, ?)"""
    
    insert_rows(connection, update_sql, abreviation_key)


def initial_setup(dbase):
    dbase_conn = connect_to_db(dbase) 

    # Set up lists of plate types 
    create_plates_us_table(dbase_conn)
    create_plates_mex_table(dbase_conn)
    create_plates_can_table(dbase_conn)
    create_plates_other_table(dbase_conn)

    # Set up abbreviation keys
    create_names_us_table(dbase_conn)
    create_names_mex_table(dbase_conn)
    create_names_can_table(dbase_conn)
    create_day_names_(dbase_conn)

    # Set up each trip as a row
    create_trip_data_table(dbase_conn)
    
    return dbase_conn
    

if __name__ == '__main__':
    dbase_name = "license-plates.db"   
    dbase = initial_setup(dbase_name)    
    dbase.close()


 # EOF