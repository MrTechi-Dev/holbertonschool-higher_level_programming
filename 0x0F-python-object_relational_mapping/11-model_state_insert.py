#!/usr/bin/python3
"""
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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
    # create the session instant and bind the engine
    Session = sessionmaker(bind=engine)
    # Create the session
    session = Session()
    # Create new state
    new_row = State(name='Louisiana')
    # Add new state to table
    session.add(new_row)
    # Query
    result = session.query(State).filter(State.name == 'Louisiana').first()
    print(result.id)
    session.commit()
