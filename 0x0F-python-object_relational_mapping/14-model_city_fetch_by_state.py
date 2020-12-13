#!/usr/bin/python3
"""
    deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from model_state import State
    from model_city import Base, City

    # Parameter variables
    user = argv[1]
    passw = argv[2]
    database = argv[3]

    # ᐁ Create the engine
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format(user, passw, database), pool_pre_ping=True
                    )
    # create the session instant and bind the engine
    Session = sessionmaker(bind=engine)
    # Create the session
    session = Session()
    # Query instant
    _query = session.query(City, State).filter(City.state_id == State.id)
    # Going through each object in _query
    for cities, states in _query:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
