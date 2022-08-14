'''
Desc:
File: /engine.py
Project: sqlalchemy-demo
File Created: Sunday, 14th August 2022 5:04:16 pm
Author: luxuemin2108@gmail.com
-----
Copyright (c) 2022 Camel Lu
'''
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
