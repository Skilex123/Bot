from datetime import datetime, timezone

import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname= 'bot_db', user='postgress', 
password = 'postgress', port='5432', host = 'localhost')

# Open a cursor to perform database operations
cur = conn.cursor()


def create_order_table(db_cursor):
    query = "CREATE TABLE IF NOT EXISTS 'order' (ID int,OrdeID TEXT,CreatedAt date)"
    rsp = db_cursor.execute(query)
    conn.commit()
    return rsp


def create_order(db_cursor):
    query = "INSERT INTO 'order' (OrderId, CreatedAt) VALUES (%s, %s);"
    order_id = 'just test text1'
    created_at = datetime.now(tz = timezone.utc)
    db_cursor.execute(query,(order_id, created_at))
    conn.commit() 


if __name__ == '__main__':
  #  just_rsp = create_order_table(cur)
   # just_rsp
    create_order(cur)