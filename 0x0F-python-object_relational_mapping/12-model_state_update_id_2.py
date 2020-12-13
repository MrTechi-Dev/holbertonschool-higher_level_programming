#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
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

    # Create the engine
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format(user, passw, database), pool_pre_ping=True
                    )
    # create the session instant and bind the engine
    Session = sessionmaker(bind=engine)
    # Create the session
    session = Session()
    # Query
    result = session.query(State).filter(State.id == 2).first()
    result.name = 'New Mexico'
    session.commit()
    session.close()
