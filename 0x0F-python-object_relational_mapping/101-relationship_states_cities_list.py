!/usr/bin/python3
""" ℹ️
    lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
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
    # Query instant
    _query = session.query(State).order_by(State.id)
    # Going through each object in _query ✅
    for obj_states in _query:
        print("{}: {}".format(obj_states.id, obj_states.name))
        for city in obj_states.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
