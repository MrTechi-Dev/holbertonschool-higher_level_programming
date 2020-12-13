#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from model_state import Base, State

    # Parameter variables
    user = argv[1]
    passw = argv[2]
    database = argv[3]

    # ᐁ Create the engine
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format(user, passw, database), pool_pre_ping=True
                    )
    # Generate database schema
    Base.metadata.create_all(engine, checkfirst=True)
    # create the session instant and bind the engine
    Session = sessionmaker(bind=engine)
    # Create the session
    session = Session()

    # Query docs
    # https://docs.sqlalchemy.org/en/13/orm/query.html
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
