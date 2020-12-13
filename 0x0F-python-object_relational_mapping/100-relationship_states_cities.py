#!/usr/bin/python3
""" ℹ️
    creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa:
"""


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from relationship_state import State
    from relationship_city import Base, City

    # Parameter variables 🎟
    user = argv[1]
    passw = argv[2]
    database = argv[3]

    # ᐁ Create the engine
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost/{}'
                    .format(user, passw, database), pool_pre_ping=True
                    )
    Base.metadata.create_all(engine)
    # create the session instant and bind the engine
    Session = sessionmaker(bind=engine)
    # Create the session
    session = Session()
    # create state
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    # Add the new city
    # ✅ When add the city automatically add the state too
    session.add(new_city)
    session.commit()
    session.close()
