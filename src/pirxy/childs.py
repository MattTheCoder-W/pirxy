import json


class Position:
    def __init__(self, x = None, y = None, z = None):
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
            ["position", str(self.position)]
        ]
        if values is not None:
            for item in values:
                json_values.append(item)
        json_data = {}
        for item in json_values:
            json_data[item[0]] = item[1]
        return json_data 

class Planet(Object):
    def __init__(self, name = "Planet", position = Position(), radius: int = 5):
        super().__init__(name=name, position=position, tag="planet")
        self.radius = radius

    def get_json(self, values: list = None):
        return super().get_json([["radius", self.radius]])


if __name__ == "__main__":
    planet = Planet()
    json_data = planet.get_json()
    print(json.dumps(json_data, indent=4))
