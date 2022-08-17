'''
Desc:
File: /working_with_data.py
Project: sqlalchemy-demo
File Created: Monday, 15th August 2022 9:09:34 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
from sqlalchemy import text, insert, select, bindparam
from sqlalchemy.orm import Session
from engine import engine
from working_with_database_metadata import createWithMetadata, createWithORM


def insert_data():
    res = createWithMetadata()
    metadata_obj = res[0]
    user_table = res[1]
    address_table = res[2]
    stmt = insert(user_table).values(
        name='spongebob', fullname="Spongebob Squarepants")
    compiled = stmt.compile()
    print(stmt, compiled.params)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        print('result.inserted_primary_key', result.inserted_primary_key)
        conn.commit()
    with engine.connect() as conn:
        result = conn.execute(
            insert(user_table),
            [
                {"name": "sandy", "fullname": "Sandy Cheeks"},
                {"name": "patrick", "fullname": "Patrick Star"}
            ]
        )
        conn.commit()
        scalar_subq = (
            select(user_table.c.id).
            where(user_table.c.name == bindparam('username')).
            scalar_subquery()
        )

        with engine.connect() as conn:
            result = conn.execute(
                insert(address_table).values(user_id=scalar_subq),
                [
                    {"username": 'spongebob',
                        "email_address": "spongebob@sqlalchemy.org"},
                    {"username": 'sandy', "email_address": "sandy@sqlalchemy.org"},
                    {"username": 'sandy', "email_address": "sandy@squirrelpower.org"},
                ]
            )
            conn.commit()
    with engine.connect() as conn:
        select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
        insert_stmt = insert(address_table).from_select(
            ["user_id", "email_address"], select_stmt
        )
        result = conn.execute(insert_stmt)
        # print(insert_stmt)
        print(insert_stmt.returning(
            address_table.c.id, address_table.c.email_address))
        conn.commit()


def selectWithCore():
    res = createWithMetadata()
    metadata_obj = res[0]
    user_table = res[1]
    address_table = res[2]

    # stmt = select(user_table).where(user_table.c.name == 'spongebob')

    with engine.connect() as session:
        # print(select(user_table.c.name, user_table.c.fullname))
        stmt = select(address_table.c.email_address).where(
            address_table.c.email_address == 'sandy@aol.com')

        result = session.execute(stmt)
        for row in result:
            print("row", row)


def main():
    # selectWithCore()
    res = createWithORM()
    insert_data()
    User = res[0]
    Address = res[1]
    # stmt = select(User).where(User.name == 'spongebob')
    # stmt = select(User)
    with Session(engine) as session:
        #     for row in session.execute(stmt):
        #         print(row)
        # user = session.execute(select(User)).first()
        # user = session.execute(select(User.name, User.fullname)).first()
        # user = session.scalars(select(User.name, User.fullname)).first()
        # print("user", user, user.name, user.fullname)
        alls = session.execute(
            select(User.name, Address).
            where(User.id == Address.user_id).
            order_by(Address.id)
        ).all()
        for row in alls:
            print(row)
    stmt = (
        select(
            ("Username: " + User.__table__.c.name).label("username"),
        ).order_by(User.__table__.c.name)
    )
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(f"{row.username}")


if __name__ == '__main__':
    main()
