#!/usr/bin/python3
"""Contains DBStorage class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """MySQL database engine for project"""

    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate DBStorage object """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        adjClassDict = {'State': State, 'User': User, 'Place': Place,
                        'City': City,
                        'Amenity': Amenity, 'Review': Review
                        }
        if cls is None:
            for key, value in adjClassDict.items():
                try:
                    dbObjects = self.__session.query(value).all()
                except Exception as e:
                    print("skipping")
                    print("********\n{}\n********".format(e))
                    continue
                for obj in dbObjects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
            return new_dict
        else:
            if cls in classes:
                dbObjects = self.__session.query(classes[cls]).all()
                for obj in dbObjects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def get(self, cls, id):
        """Method that retrives a single object from the __0bjects dict"""
        if (id == None and cls == None):
            return None
        for key, val in self.all(cls).items():
            # Class.id
            gotcha = str(cls) + '.' + str(id)
            print(gotcha)
            if key == gotcha:
                return (val)

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if (cls == None):
            return (None)
        else:
            count = len(self.all(cls))
            return count

    def new(self, obj):
        """Adds new object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create current database session from the engine
        using a sessionmaker"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Removes session"""
        self.__session.remove()
