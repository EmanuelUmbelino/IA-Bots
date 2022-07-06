import numpy as np
from Map.Position import Position

class Map():
    def __init__(self, grid_size=(59,34)):
        self.grid_size = grid_size
        self.grid = np.zeros(self.grid_size, dtype=np.uint8)
    
    def setPos(self, pos = Position(), tile = int(0)):
        if (self.grid[pos.x,pos.y] == 0):
            self.grid[pos.x,pos.y] = tile
    
    def get(self):
        return self.grid

    def distance(self, pos1 = Position(), pos2 = Position()):
        return np.linalg.norm(np.array((pos1.x, pos1.y),dtype=np.float32) - np.array((pos2.x, pos2.y),dtype=np.float32))
