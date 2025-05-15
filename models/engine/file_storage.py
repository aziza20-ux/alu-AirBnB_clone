#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel


classes = {
         "BaseModel":BaseModel 
         }
class FileStorage(self):

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """displaying all objects"""
        return self.__objects
    def new(self, obj):

        obj_key = f"{self.obj.__class__.name}.{self.id}"
        for k, v in obj.items():
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
                    obj_dict = {}

                    for ke, obj_dic in data:
                        classname = obj_dic.get('__class__')
                        if classname:
                            if classname in classes:
                                actualclass = classes[classname]
                                self.obj_dict[ke] = actualclass(**obj_dic)
                            else:
                                print("the class does exit")
                        else:
                            print(f"object with {ke} doesn't have a class attribute")

            except FileNotFoundError:
                return
                            
