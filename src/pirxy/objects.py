import json


class Position:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def get_json(self):
        data = {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }
        return data

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z {self.z}"


class Planet:
    def __init__(self, name: str = None,
                 radius: float = None,
                 mass: float = None,
                 position = None):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.position = position

    def get_json(self):
        name = self.name if self.name is not None else ""
        radius = self.radius if self.radius is not None else 0
        mass = self.mass if self.mass is not None else 0
        position = self.position.get_json() if self.position is not None else 0 
        data = {
            "type": "planet",
            "name": name,
            "radius": radius,
            "mass": mass,
            "position": position,
        }
        return data

    def from_json(self, data):
        self.name = data['name']
        self.radius = data['radius']
        self.mass = data['mass']
        self.position = data['position']

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
