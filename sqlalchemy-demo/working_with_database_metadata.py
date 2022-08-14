'''
Desc:
File: /working_with_database_metadata.py
Project: sqlalchemy-demo
File Created: Sunday, 14th August 2022 6:23:34 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''

from sqlalchemy.orm import Session, registry, declarative_base, relationship
from sqlalchemy import text, MetaData, Table, Column, Integer, String, ForeignKey
from engine import engine


def createTableSchemaWithMetatdata():
    metadata_obj = MetaData()
    user_table = Table(
        "user_account",
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('name', String(30)),
        Column('fullname', String)
    )
    # print("metadata_obj", metadata_obj, user_table.primary_key)
    address_table = Table(
        "address",
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_id', ForeignKey('user_account.id'), nullable=False),
        Column('email_address', String, nullable=False)
    )
    return metadata_obj, user_table, address_table


def createWithMetadata():
    res = createTableSchemaWithMetatdata()
    metadata_obj = res[0]
    user_table = res[1]
    address_table = res[2]
    metadata_obj.create_all(engine)
    return metadata_obj, user_table, address_table


def createWithORM():
    mapper_registry = registry()
    Base = mapper_registry.generate_base()

    class User(Base):
        __tablename__ = 'user_account'
        id = Column(Integer, primary_key=True)
        name = Column(String(30))
        fullname = Column(String)
        addresses = relationship("Address", back_populates="user")

        def __repr__(self):
            return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

    class Address(Base):
        __tablename__ = 'address'
        id = Column(Integer, primary_key=True)
        email_address = Column(String, nullable=False)
        user_id = Column(Integer, ForeignKey('user_account.id'))
        user = relationship("User", back_populates="addresses")

        def __repr__(self):
            return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    # user_table = User.__table__
    # print(user_table)
    # createWithMetadata()
    # emit CREATE statements given ORM registry
    # mapper_registry.metadata.create_all(engine)

    # the identical MetaData object is also present on the
    # declarative base
    Base.metadata.create_all(engine)


def createWithHybird():
    res = createTableSchemaWithMetatdata()
    metadata_obj = res[0]
    user_table = res[1]
    address_table = res[2]
    # Base = declarative_base()
    mapper_registry = registry()
    Base = mapper_registry.generate_base()

    class User(Base):
        __table__ = user_table

        addresses = relationship("Address", back_populates="user")

        def __repr__(self):
            return f"User({self.name!r}, {self.fullname!r})"

    class Address(Base):
        __table__ = address_table

        user = relationship("User", back_populates="addresses")

        def __repr__(self):
            return f"Address({self.email_address!r})"

    # Base.metadata.create_all(engine)
    # mapper_registry.metadata.create_all(engine)

    metadata_obj.create_all(engine)


def reflection_table():
    metadata_obj = MetaData()
    some_table = Table("user_account", metadata_obj, autoload_with=engine)
    print("some_table", some_table)


def main():
    # createWithMetadata()
    # createWithORM()
    createWithHybird()
    reflection_table()

    # with Session(engine) as session:
    #     stmt = text(
    #         "SELECT * FROM user_account")
    #     result = session.execute(stmt)
    #     for row in result:
    #         print("row", row)
    # print(f"x: {row.x}  y: {row.y}")


if __name__ == '__main__':
    main()
