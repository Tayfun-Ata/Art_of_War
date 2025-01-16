from panda3d.core import Point3

class Unit:
    def __init__(self, loader, render, position, model_path, hp=100, attack_power=10, num_men=5):
        self.loader = loader
        self.render = render
        self.position = position
        self.model_path = model_path
        self.hp = hp
        self.attack_power = attack_power
        self.num_men = num_men
        self.models = []

        self.create_men()

    def create_men(self):
        for i in range(self.num_men):
            model = self.loader.loadModel(self.model_path)
            model.reparentTo(self.render)
            offset = i * 0.5  # Adjust the offset as needed
            model.setPos(self.position + Point3(offset, 0, 0))
            self.models.append(model)

    def update_men(self):
        # Remove models if the number of men decreases
        while len(self.models) > self.num_men:
            model = self.models.pop()
            model.removeNode()

        # Update positions of remaining models
        for i, model in enumerate(self.models):
            offset = i * 0.5  # Adjust the offset as needed
            model.setPos(self.position + Point3(offset, 0, 0))

    def move(self, dx, dy):
        self.position += Point3(dx, dy, 0)
        self.update_men()

    def attack(self, other):
        if self.models and self.models[0].getDistance(other.models[0]) <= 1:
            other.hp -= self.attack_power
            other.num_men = max(0, other.num_men - 1)
            other.update_men()
