import random

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 'wall'
        
    def __repr__(self):
        return f'Tile({self.x}, {self.y}, {self.type})'
        
class Dungeon:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[Tile(x, y) for y in range(height)] for x in range(width)]
        
    def generate_map(self):
        self.tiles = [[Tile(x, y) for y in range(self.height)] for x in range(self.width)]
        
        for x in range(self.width):
            for y in range(self.height):
                if random.random() < 0.4:
                    self.tiles[x][y].type = 'floor'
    
    def print_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles[x][y].type == 'wall':
                    print('#', end='')
                else:
                    print('.', end='')
            print()
                
if __name__ == '__main__':
    dungeon = Dungeon(50, 50)
    dungeon.generate_map()
    dungeon.print_map()