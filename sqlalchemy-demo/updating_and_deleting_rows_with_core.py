'''
Desc:
File: /updating_and_deleting_rows_with_core.py
Project: sqlalchemy-demo
File Created: Saturday, 20th August 2022 6:05:38 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
from sqlalchemy import update, delete, select, bindparam

from engine import engine
from working_with_database_metadata import createWithMetadata, createWithORM
from working_with_data import insert_data


def main():
    insert_data()
    res = createWithMetadata()
    metadata_obj = res[0]
    user_table = res[1]
    address_table = res[2]
    with engine.connect() as conn:
        stmt = select(user_table)
        result = conn.execute(stmt)
        for row in result:
            print("row", row)

        update_stmt = (
            update(user_table).where(user_table.c.name == 'patrick').
            values(fullname='Patrick the Star').
            returning(user_table.c.id, user_table.c.name)
        )
        conn.execute(update_stmt)
        result = conn.commit()
        print("result", result)
        print(update_stmt)
    with engine.connect() as conn:
        stmt = select(user_table)
        result = conn.execute(stmt)
        for row in result:
            print("row", row)

    # delete_stmt = (
    #     delete(user_table).where(user_table.c.name == 'patrick').
    #     returning(user_table.c.id, user_table.c.name)
    # )
    # print(delete_stmt)


if __name__ == '__main__':
    main()
