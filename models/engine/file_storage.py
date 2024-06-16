#!/usr/bin/python3
"""module of class file storange"""
import json
from os import path

class FileStorage:
    """ class filestorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serialize __object to __file_path """
        serialized_object = {}
        for key, obj in self.__objects.items():
            serialized_object[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_object, file)

    def reload(self):
        """deserializing json file to obj only if __file_path exist|"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    loaded_objects = json.load(file)
                    for key, value in loaded_objects.items():
                        class_name = value["__class__"]
                        cls = eval(class_name)
                        self.__objects[key] = cls(**value)
                except json.JSONDecoderError:
                    pass
