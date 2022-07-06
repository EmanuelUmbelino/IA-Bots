import numpy as np

class Map():
    def __init__(self, grid_size=(59,34)):
        self.grid_size = grid_size
        self.grid = np.zeros(self.grid_size, dtype=np.uint8)
    
    def setPos(self, pos, tile):
        self.grid[pos[0],pos[1]] = tile
    
    def get(self):
        return self.grid

    def distance(self, pos1, pos2):
        return np.linalg.norm(np.array(pos1,dtype=np.float32) - np.array(pos2,dtype=np.float32))
