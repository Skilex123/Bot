from connection import Conn

CREATE_FLOWERS_TABLE = """
    CREATE TABLE flowers(
        ID int NOT NULL PRIMARY KEY,
        price DECIMAL(3,2) NOT NULL,
        amount  int NOT NULL,
        name varchar(250) NOT NULL UNIQUE,
        color varchar(250) NOT NULL
    );
"""


if __name__ == "__main__":
    db_instance = Conn()
    db_instance.create_table(CREATE_FLOWERS_TABLE)
