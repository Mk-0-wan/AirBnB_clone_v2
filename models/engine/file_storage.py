#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            dictOfClassMatchInObjectDict = {}
            for key, value in self.__objects.items():
                if str(cls) in str(type(value)):
                    dictOfClassMatchInObjectDict[key] = value
            return dictOfClassMatchInObjectDict

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
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        jsonObject = {}
        for key in self.__objects:
            jsonObject[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(jsonObject, f)

    def reload(self):
        """Loads storage dictionary from file"""
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
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if its inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
