from panda3d.core import Point3

def draw_grid(loader, render, width, height, grid_size):
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            line = loader.loadModel("models/line.egg")
            line.reparentTo(render)
            line.setPos(Point3(x, y, 0))
