#!/usr/bin/python3
"""SQLalchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (func, create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL

db = {'drivername': 'mysql+mysqldb',
      'host': 'localhost',
      'port': '3306',
      'username': sys.argv[1],
      'password': sys.argv[2],
      'database': sys.argv[3]}

if __name__ == "__main__":
    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    row = State(name="Louisiana")
    session.add(row)
    session.commit()
    row = session.query(State).filter(State.name == "Louisiana").first()
    print(row.id)
    session.close()
