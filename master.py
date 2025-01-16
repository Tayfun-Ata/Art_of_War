from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3
from units import Unit
from map import draw_obstacles
from hud import draw_hud
from enemy_ai import move_enemy_units

class GeneralsOfWar3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model
        self.environ = self.loader.loadModel("models/environment.egg")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Create units
        self.player_units = [Unit(self.loader, self.render, Point3(5, 5, 0), "models/unit.egg", num_men=5)]
        self.enemy_units = [Unit(self.loader, self.render, Point3(10, 10, 0), "models/enemy_unit.egg", num_men=5)]

        # Create obstacles
        self.obstacles = [(7, 7), (8, 8), (9, 9)]
        draw_obstacles(self.loader, self.render, self.obstacles)

        # Set up keyboard controls
        self.accept("arrow_left", self.move_units, [-1, 0])
        self.accept("arrow_right", self.move_units, [1, 0])
        self.accept("arrow_up", self.move_units, [0, 1])
        self.accept("arrow_down", self.move_units, [0, -1])
        self.accept("space", self.attack)

    def move_units(self, dx, dy):
        for unit in self.player_units:
            unit.move(dx, dy)

    def attack(self):
        for unit in self.player_units:
            for enemy in self.enemy_units:
                unit.attack(enemy)

    def update(self, task):
        move_enemy_units(self.enemy_units, self.player_units)
        return task.cont

game = GeneralsOfWar3D()
game.taskMgr.add(game.update, "update")
game.run()
