#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "Review": Review,
    "City": City,
    "Amenity": Amenity
}


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """displaying all objects"""
        return self.__objects

    def new(self, obj):

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj

    def save(self):

        obj_dict = {}

        for key, ob in self.__objects.items():
            obj_dict[key] = ob.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):

        if os.path.exists(self.__file_path):
            try:

                with open(self.__file_path, 'r') as f:
                    data = json.load(f)

                    for ke, obj_dic in data.items():
                        classname = obj_dic.get('__class__')
                        if classname:
                            if classname in classes:
                                actualclass = classes[classname]
                                self.__objects[ke] = actualclass(**obj_dic)
                            else:
                                print("the class does exit")
                        else:
                            print(
                                f"objectwith {ke} classattributedon'texist")

            except FileNotFoundError:
                return
