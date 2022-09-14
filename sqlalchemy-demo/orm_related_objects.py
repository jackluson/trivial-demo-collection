'''
Desc:
File: /orm_related_objects.py
Project: sqlalchemy-demo
File Created: Monday, 22nd August 2022 9:55:43 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
from sqlalchemy.orm import Session, registry, relationship, aliased, selectinload
from sqlalchemy import Column, Integer, String, ForeignKey, select
from engine import engine


def main():
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
    user = {
        'name': 'pkrabs2',
        'fullname': 'Pearl Krabs2',
    }
    # --insert--
    u1 = User(**user)

    a1 = Address(email_address="pearl.krabs@gmail.com2")
    u1.addresses.append(a1)
    print("a1", a1.user_id, a1.user)
    a2 = Address(email_address="pearl@aol.com2", user=u1)
    print("a2", a2)
    print("u1", u1.addresses)
    # with Session(engine) as session:
    #     # session.add(u1)
    #     session.add(a1)
    #     # print(u1 in session)
    #     # print(a1 in session)
    #     session.commit()
    #     print(u1.addresses)
    #     print(a1.user)
    #     print(a2.user)

    # --select--
    with Session(engine) as session:
        address_alias_1 = aliased(Address)
        address_alias_2 = aliased(Address)
        session.add(a1)
        # print(u1 in session)
        # print(a1 in session)
        session.commit()
        print(
            select(User).
            join(User.addresses.of_type(address_alias_1)).
            where(address_alias_1.email_address == 'patrick@aol.com').
            join(User.addresses.of_type(address_alias_2)).
            where(address_alias_2.email_address == 'patrick@gmail.com')
        )
        stmt = select(Address, User).join_from(User, Address)
        stmt2 = select(User).join(User.addresses.of_type(address_alias_1)).where(address_alias_1.email_address == 'pearl.krabs@gmail.com').join(
            User.addresses.of_type(address_alias_2)).where(address_alias_2.email_address == 'pearl@aol.com')
        user_alias_1 = aliased(User)
        stmt3 = select(User.name).join(User.addresses)
        stmt4 = (
            select(User.fullname).
            join(User.addresses.and_(
                Address.email_address == 'pearl.krabs@gmail.com'))
        )

        # res = session.execute(stmt4).all()
        stmt5 = (
            select(User.fullname).
            where(User.addresses.any(
                Address.email_address == 'pearl.krabs@gmail.com'))
        )
        stmt6 = (
            select(User.fullname).
            where(~User.addresses.any())
        )

        stmt7 = (
            select(Address.email_address).
            where(Address.user.has(User.name == "pkrabs"))
        )

        # stmt8 = select(Address).where(Address.user == u1)
        stmt8 = select(Address).where(Address.user != u1)
        # print(select(User).where(User.addresses.contains(a1)))

        res = session.execute(stmt8).all()

        print("res", res)
        for row in res:
            print("row", row, row[0])
            print("row", row[0].email_address)
        for user_obj in session.execute(
            select(User).options(selectinload(User.addresses))
        ).scalars():
            user_obj.addresses  # access addresses collection already loaded


if __name__ == '__main__':
    main()
