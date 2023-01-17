import os
import json
from datetime import datetime

from .utils import yes_no_input
from .objects import OBJECT_TYPE


class World:
    def __init__(self):
        self.data = {
            "name": None,
            "created": None,
            "objects": [],
        }

    def create(self, name: str):
        print(f"[world] creating new world with name: {name}")
        self.data['name'] = name
        self.data['created'] = datetime.now().strftime("%d/%m/%Y")
        self.data['objects'] = []
        print(f"[world] blank world created")

    def load_from_file(self, fpath: str):
        if not os.path.exists(fpath):
            raise FileNotFoundError(f"Specified world file does not exists! -> {fpath}")
        if not os.path.isfile(fpath):
            raise TypeError("Specified world path is not file!")
        print(f"[world] loading world from file: {fpath}")

        with open(fpath, "r") as world_file:
            load_data = world_file.read()
            load_data = json.loads(load_data)

        raw_objects = []
        for obj_id in load_data['objects']:
            obj = load_data['objects'][obj_id]
            if obj['tag'].lower() not in OBJECT_TYPE:
                print(f"Tag `{obj['tag']} is not recognized!`")
                continue
            raw_obj = OBJECT_TYPE[obj['tag'].lower()]()
            raw_obj.from_json(obj)
            print(f"[world_load] Converted object from json")
            raw_objects.append(raw_obj)
        self.data = load_data
        self.data['objects'] = raw_objects
        print(f"[world_load] loaded world data from file")

    # returns save success status
    def save_to_file(self, fpath: str) -> bool:
        if os.path.exists(fpath):
            override = yes_no_input("[warning] Specified world save file already exists! Do you want to override it? [N/y]: ", default = False)
            if not override:
                return False

        objects = self.data['objects'].copy()
        save_data = self.data.copy()
        save_data['objects'] = {}
        for i, obj in enumerate(objects):
            print(f"[world_save] Converting object no. {i} to json")
            print(type(obj))
            try:
                save_data['objects'][str(i)] = obj.get_json()
            except:
                print("Object does not provide json conversion and will not be included in save!")
                continue

        with open(fpath, "w") as save_file:
            save_file.write(json.dumps(save_data, indent=4))
        print(f"[world] data saved to file")
        return True

    def get_attribute(self, attr_name: str):
        if attr_name not in list(self.data.keys()):
            raise KeyError(f"World data doesn't have specified attribute -> {attr_name}")
        return self.data[attr_name]

    def put_object(self, obj):
        self.data['objects'].append(obj)
        print(self.data)

    def __str__(self):
        return f"[{self.data['name']}] - {self.data['created']}\n--> Object count: {len(self.data['objects'])}"


class WorldGenerator:
    def __init__(self):
        pass

