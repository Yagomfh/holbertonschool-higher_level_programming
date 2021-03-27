#!/usr/bin/python3
"""SQLalchemy"""
import sys
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    db = {'drivername': 'mysql+mysqldb',
          'host': 'localhost',
          'port': '3306',
          'username': sys.argv[1],
          'password': sys.argv[2],
          'database': sys.argv[3]}
    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    city = City(name='San Francisco')
    state = State(name='California', cities=[city])
    
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
