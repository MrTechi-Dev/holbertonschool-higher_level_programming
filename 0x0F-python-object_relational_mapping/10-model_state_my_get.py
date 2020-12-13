#!/usr/bin/python3
"""
    prints the State object with the name passed '
    as argument from the database hbtn_0e_6_usa
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
    word_to_match = argv[4]

    # ᐁ Create the engine
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format(user, passw, database), pool_pre_ping=True
                    )
    # create the session instant and bind the engine
    Session = sessionmaker(bind=engine)
    # Create the session
    session = Session()

    # Query docs
    # https://docs.sqlalchemy.org/en/13/orm/query.html
    result_query = session.query(State)\
        .filter(State.name == word_to_match).first()
    print(result_query.id if result_query else "Not found")
    # Close session
    session.close()
