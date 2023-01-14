import os

from .world import World
from .objects import Planet, Position


class Game:
    def __init__(self):
        self.world = World()
        self.player = None
        self.inventory = None
        self.vehicle = None

        # self.world.load_from_file("world1.save")
        self.world.create("Galaxy1")


    def start(self):
        print(f"Game started on world: {self.world.get_attribute('name')}")

        self.world.put_object(Planet("Earth", 1.5, 20, Position(x = 10, y = 20, z = 30)))

        print(f"World details:")
        print(str(self.world))

        print(f"Objects: {self.world.get_attribute('objects')}")

        for obj in self.world.get_attribute('objects'):
            print(str(obj))

        self.stop()

    def stop(self):
        self.world.save_to_file("world1.save")

