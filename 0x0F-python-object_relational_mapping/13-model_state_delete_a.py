#!/usr/bin/python3
"""
    script that deletes all State objects with a
    name containing the letter a from the database hbtn_0e_6_usa
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
    # Query and delete instant
    _query = session.query(State).\
        filter(State.name.contains('a')).\
        delete(synchronize_session='fetch')
    """
    Another way to do it
    result = session.query(State).all()
    # for record in result:
    #     if 'a' in record.name:
    #         session.delete(record)
    """
    session.commit()
    session.close()
