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
    states = session.query(State)
    for state in states:
        cities = session.query(City).filter(City.state_id == state.id)
        print("{}: {}".format(state.id, state.name))
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
