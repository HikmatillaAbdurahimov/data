import os
import psycopg2
from dotenv import load_dotenv
import multiprocessing
import time

load_dotenv()
with psycopg2.connect(
    database=os.getenv('database'),
    password=os.getenv('password'),
    user=os.getenv('user'),
    host=os.getenv('host'),
    port=os.getenv('port')
) as conn:
    with conn.cursor() as cur:
        def create_table():
            create_table_query="""
            create table datas(
            id         serial primary key ,
            name       varchar(100),
            commintt   text,
            userId     int
            ); """
            cur.execute(create_table_query)
            conn.commit()
            time.sleep(2)

        def insert_into():
            insert_into_query="""
            insert into datas(name,commintt,userId)
            values ('vali','student',4),
                   ('ali','oshpaz',7),
                   ('temur','domla',8),
                   ('saman','shoir',1)
            """
            cur.execute(insert_into_query)
            conn.commit()
            time.sleep(2)

        def select():
            select_query="""
            select *  from datas;"""
            cur.execute(select_query)
            print(cur.fetchall())
            time.sleep(3)

        create_table()

        process2 = multiprocessing.Process(target=insert_into())
        process3 = multiprocessing.Process(target=select())


        # Jarayonlarni boshlash
        process2.start()
        process3.start()


        # Jarayonlarning tugashini kutish
        process2.join()
        process3.join()

