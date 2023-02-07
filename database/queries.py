from connection import Conn

CREATE_FLOWERS_TABLE = """
    CREATE TABLE flowers(
        ID int NOT NULL PRIMARY KEY,
        price DECIMAL(3,2) NOT NULL,
        amount  int NOT NULL,
        name varchar(250) NOT NULL UNIQUE,
        color varchar(250) NOT NULL,
    );
"""

fix_flowers_table = """ALTER TABLE "flowers" ALTER COLUMN "price" TYPE DECIMAL(7,2)"""

create_squence = 'CREATE SEQUENCE flower_id_seq;'

modify_id_mechanism = """ALTER TABLE "flowers" ALTER COLUMN "id" SET DEFAULT nextval('flower_id_seq');"""


if __name__ == "__main__":
    db_instance = Conn()
    #db_instance.execute_query_without_response(CREATE_FLOWERS_TABLE)
    #db_instance.execute_query_without_response(fix_flowers_table)
   # db_instance.execute_query_without_response(create_squence)
    db_instance.execute_query_without_response(modify_id_mechanism)

