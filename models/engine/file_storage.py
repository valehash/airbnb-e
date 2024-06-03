#!/usr/bin/env python3

import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        # for key, value in FileStorage.__objects.items():
        # Do NOT trust the key in FileStorage.__objects.keys()
        # Hence the reason for changing the logic in the
        # above for loop to the one below.
        # WIERD ERROR INDEED.
        for value in FileStorage.__objects.values():
            key = f"{value.__class__.__name__}.{value.id}"
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        to_be_serialized = {}

        try:
            with open(FileStorage.__file_path, 'r') as f:
                collected = json.load(f)
            
            for value in collected.values():
                key = f"{value['__class__']}.{value['id']}"
                to_be_serialized[key] = BaseModel(value)

            FileStorage.__objects = to_be_serialized
        except FileNotFoundError:
            pass
