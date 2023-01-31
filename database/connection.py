import psycopg2
import os


class Conn:

    @property
    def conn(self):
        return psycopg2.connect(
            dbname=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            port=os.environ['DB_PORT'],
            host=os.environ['DB_HOST'],
        )

    def open_and_close_conn(func):
        def wrapper(*args, **kwargs):
            conn = Conn().conn
            cursor = conn.cursor()
            resp = func(*args, conn=conn, cursor=cursor, **kwargs)
            cursor.close()
            conn.close()
            return resp
        return wrapper

    def create_table(self, query: str, conn, cursor):
        cursor.execute(query)
        conn.commit()

    def insert(self, query: str, conn, cursor):
        cursor.execute(query)
        conn.commit()

    def select(self, query: str, conn, cursor):
        cursor.execute(query)
        resp = cursor.fetchall()
        return resp


if __name__ == '__main__':
#   #  just_rsp = create_order_table(cur)
#    # just_rsp
#     create_order(cur)
    conn = Conn().conn
    conn
