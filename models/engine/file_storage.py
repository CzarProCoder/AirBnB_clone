#!/usr/bin/env python3
''' Module that serializes and deserializes '''

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return(FileStorage.__objects)

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id
        '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file
        (path: __file_path)
        '''
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects if file exists
        otherwise, do nothing
        '''
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
