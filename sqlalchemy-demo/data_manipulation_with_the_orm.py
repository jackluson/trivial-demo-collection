'''
Desc:
File: /data_manipulation_with_the_orm.py
Project: sqlalchemy-demo
File Created: Sunday, 21st August 2022 12:02:53 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from working_with_database_metadata import createWithORM
from engine import engine


def Add():
    res = createWithORM()
    User = res[0]
    Address = res[1]
    squidward = User(name="squidward", fullname="Squidward Tentacles")
    krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")
    # Insert
    with Session(engine) as session:
        session.add(squidward)
        session.add(krabs)
        print('new', session.new)
        session.flush()
        session.commit()
    # Update-1
    with Session(engine) as session:
        sandy = session.execute(
            select(User).filter_by(name="sandy")).scalar_one()
        print("sandy", sandy)
        sandy.fullname = "Sandy Squirrel"
        print('is_dirty', sandy in session.dirty)
        sandy_fullname = session.execute(
            select(User.fullname).where(User.id == 2)
        ).scalar_one()

        print(sandy_fullname)
        print('is_dirty', sandy in session.dirty)
        session.commit()
    # Update-2
    with Session(engine) as session:
        session.execute(
            update(User).
            where(User.name == "sandy").
            values(fullname="Sandy Squirrel Extraordinaire")
        )
        session.rollback()
        session.commit()

    # with Session(engine) as session:
    #     patrick = session.get(User, 6)
    #     session.delete(patrick)
    #     session.commit()


def main():
    Add()


if __name__ == '__main__':
    main()
