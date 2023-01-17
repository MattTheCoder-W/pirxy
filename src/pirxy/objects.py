import json

class Position:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def set_coordinate(self, coord_name: str, coord_value: int):
        coord_name = coord_name.lower()
        if coord_name == "x":
            self.x = coord_value
        elif coord_name == "y":
            self.y = coord_value
        elif coord_name == "z":
            self.z = coord_value
        else:
            raise ValueError("Specified coordinate is not present ->", coord_name)

    def get_json(self):
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z
        }

    def from_json(self, json_data: dict):
        self.x = json_data['x']
        self.y = json_data['y']
        self.z = json_data['z']

    def __str__(self):
        return f"x={self.x},y={self.y},z={self.z}"

class Object:
    def __init__(self, name = "", position = Position(), tag = "object", object_id = 0):
        self.name = name
        self.position = position
        self.tag = tag
        self.object_id = object_id

    # values - List in format [ [key, value], ..., [key, value] ]
    def get_json(self, values: list = None):
        json_values = [
            ["tag", self.tag],
            ["id", self.object_id],
            ["name", self.name],
            ["position", self.position.get_json()]
        ]
        if values is not None:
            for item in values:
                json_values.append(item)
        json_data = {}
        for item in json_values:
            json_data[item[0]] = item[1]
        return json_data 

    def from_json(self, json_data: dict):
        self.name = json_data['name']
        self.object_id = json_data['id']
        pos = Position()
        pos.from_json(json_data['position'])
        self.position = pos
        self.tag = json_data['tag']


class Planet(Object):
    def __init__(self, name: str = "Planet",
                 radius: int = 5,
                 mass: int = 1,
                 position = Position()):
        super().__init__(name, position, "planet")
        self.radius = radius
        self.mass = mass

    def get_json(self):
        return super().get_json([["radius", self.radius], ["mass", self.mass]])

    def from_json(self, data):
        super().from_json(data)
        self.radius = data['radius']
        self.mass = data['mass']

    def __str__(self):
        text = f"[Planet]\nName: {self.name}\n"
        if self.radius:
            text += f"Radius: {self.radius}\n"
        if self.mass:
            text += f"Mass: {self.mass}\n"
        if self.position:
            text += f"Position: {self.position}\n"
        return text


OBJECT_TYPE = {
    "planet": Planet,
}
