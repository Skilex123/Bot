from datetime import datetime, timezone

import psycopg2


class Conn:

    @property
    def conn(self):
        return psycopg2.connect(
            dbname= 'bot_db',
            user='postgress',
            password = 'postgress',
            port='5432',
            host = 'localhost',
        )

    def get_conn_and_cursor(self):
        conn = self.conn
        return conn, conn.cursor()

    def create_table(self, query):
        conn, cursor = self.get_conn_and_cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def insert(self, query):
        conn, cursor = self.get_conn_and_cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def select(self, query):
        conn, cursor = self.get_conn_and_cursor()
        cursor.execute(query)
        resp = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return resp


if __name__ == '__main__':
#   #  just_rsp = create_order_table(cur)
#    # just_rsp
#     create_order(cur)
    pass
