#!/usr/bin/env python3

import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        cn = obj.__class__.__name__
        id =  obj.id
        key = f"{cn}.{id}"
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            print(f"value = {value}")
            print(f"type(value) = {type(value)}")
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, 'r') as f:
                collected = json.load(f)
                for key, value in collected.items():
                    FileStorage.__objects[key] = BaseModel(value)
                # FileStorage.__objects = json.load(f)
                # print(f"FileStorage.__objects = {FileStorage.__objects}")
                # print(f"type(FileStorage.__objects) = {type(FileStorage.__objects)}")
        except FileNotFoundError:
            pass

