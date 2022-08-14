'''
Desc:
File: /02-.py
Project: sqlalchemy-demo
File Created: Sunday, 14th August 2022 4:46:45 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
from sqlalchemy import text
from sqlalchemy.orm import Session
from engine import engine

from basics_of_statement_execution import pre

# The Session doesn’t actually hold onto the Connection object after it ends the transaction. It gets a new Connection from the Engine when executing SQL against the database is next needed.


def main():
    stmt = text(
        "SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)

    with Session(engine) as session:
        result = session.execute(stmt)
        for row in result:
            print(f"x: {row.x}  y: {row.y}")

    with Session(engine) as session:
        result = session.execute(
            text("UPDATE some_table SET y=:y WHERE x=:x"),
            [{"x": 9, "y": 11}, {"x": 13, "y": 15}]
        )
        list = [{"x": 16, "y": 18, 'z': 10}, {"x": 19, "y": 100}]
        session.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            list
        )
        session.commit()
    with Session(engine) as session:
        stmt = text(
            "SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
        result = session.execute(stmt)
        for row in result:
            print(f"x: {row.x}  y: {row.y}")


if __name__ == '__main__':
    pre()
    main()
