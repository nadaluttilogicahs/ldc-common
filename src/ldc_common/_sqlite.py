import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def total_rows(cursor, table_name, print_out=False):
    """ Returns the total number of rows in the database """
    cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = cursor.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]

#http://www.cdotson.com/2014/06/generating-json-documents-from-sqlite-databases-in-python/
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def select_tables_name (db):

    # create a database connection
    conn = sqlite3.connect(db)
    with conn:
        cur = conn.cursor()
        
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        rows = cur.fetchall()
        
    # print(rows)
    # convert list of tuples to list
    out = [item for t in rows for item in t]
    return out

def select_all_tasks(db, table):
    
    # create a database connection
    conn = sqlite3.connect(db)
    with conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM "+table)
        rows = cur.fetchall()
        
    #print(rows)
    return rows

def select_task_by_id(db, table, id):
    
    # create a database connection
    conn = sqlite3.connect(db)
    with conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute("SELECT * FROM "+table+" WHERE ID=?", (id,))
        rows = cur.fetchall()
         
    #print(rows)
    return rows

def select_task_by_field(db, table, id, field):
    
    # create a database connection
    conn = sqlite3.connect(db)
    with conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        
        cur.execute("SELECT ID, "+field+" FROM "+table+" WHERE ID=?", (id,))
        rows = cur.fetchall()
            
    #print(rows)
    return rows

def select_task_by_query(db, query):
    
    #20221125: tolto perchè se tabella non ha colonna ID da errore!!
    #Comunque ID o viene richiesto o con WHERE (quindi risaputo). Eventualmente se serve richiederlo nella query
    #!! Vedere se funziona con i sorgenti del cloud !!
    #query = query[:6]+" ID, "+query[6:]
    
    # create a database connection
    conn = sqlite3.connect(db)
    with conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        
        cur.execute(query)
        rows = cur.fetchall()
            
    #print(rows)
    return rows

def select_column_by_query(db, query):
    
    # create a database connection
    conn = sqlite3.connect(db)
    with conn:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        
        cur.execute(query)
        rows = cur.fetchall()
        # rows += [d[0] for d in cur.description]
            
    #print(rows)
    return rows

def update_task_by_field(db, table, id, field, value):
    
    # create a database connection
    conn = sqlite3.connect(db)
    with conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()

        sql = "UPDATE "+table+" SET "+field+"=? WHERE ID=?", (value, id)
        cur.execute("UPDATE "+table+" SET "+field+"=? WHERE ID=?", (value, id))
        rows = cur.fetchall()
            
    #print(rows)
    return rows

def update_task_by_query(db, query):
    
    # create a database connection
    try:
        conn = sqlite3.connect(db)
        with conn:
            conn.row_factory = dict_factory
            cur = conn.cursor()
            
            cur.execute(query)
            rows = cur.fetchall()
            # print(rows)
            return rows
    except Error as e:
        print(e) 
        #return bytes(str(e), 'utf-8')
        return str(e)
    
    #print(rows)
    #return rows

