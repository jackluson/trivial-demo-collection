'''
Desc:
File: /main.py
Project: sqlalchemy-demo
File Created: Sunday, 14th August 2022 2:17:01 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
from engine import engine
from sqlalchemy import text


def pre():
    # basics-of-statement-execution

    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
        )
        conn.commit()

    #     result = conn.execute(text("SELECT * FROM  some_table"))
    #     print("result", result.all())

    # fetching-rows
    with engine.begin() as conn:
        list = [{"x": 6, "y": 8, 'z': 10}, {"x": 9, "y": 10}]
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            list
        )
        result = conn.execute(text("SELECT * FROM  some_table"))
        print("result", result.all())

    with engine.connect() as conn:
        result = conn.execute(text("SELECT x, y FROM some_table"))
        # for x, y in result:
        #     print("x, y ", x, y)

        # for row in result:
        #     print("row", type(row), row)
        #     print(f"x: {row.x}  y: {row.y}")

        for dict_row in result.mappings():
            print("dict_row", dict_row)
            x = dict_row['x']
            y = dict_row['y']
            print("y", y)

    # #sending-parameters
    with engine.connect() as conn:
        query = {"y": 2}
        result = conn.execute(
            text("SELECT x, y FROM some_table WHERE y > :y"),
            query
        )
        for row in result:
            print(f"x: {row.x}  y: {row.y}")

    # bundling-parameters-with-a-statement

    with engine.connect() as conn:
        stmt = text(
            "SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
        result = conn.execute(stmt)
        for row in result:
            print(f"x: {row.x}  y: {row.y}")


if __name__ == '__main__':
    pre()
