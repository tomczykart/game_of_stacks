from app.models import User, UserCube
from app import app, db


class StackTower():
    MAX_FLOOR_CUBES = 4  #cubes in positions 1, 2, 3, 4
    floors = 0  #4 cubes each floor
    floor_cubes = 0
   
   
    def __init__(self):
        self.cubes = ""
        self.generate_tower()
        pass
    
    def generate_tower(self):
        self.cubes = UserCube.query.all()
        StackTower.floors = len(self.cubes)//4
        StackTower.floor_cubes = len(self.cubes)%4
        return StackTower.floor_cubes
        
        
    def return_cube(self, floor, position):
        index = (int(floor)-1)*4 + int(position)-1
        try:
            cube = self.cubes[index]
            return cube
        except IndexError:
            raise IndexError
        
 
    
    def find_your_cube(self, cube_owner_id):
        pass
    
    
    def find_your_neighbours(self):
        pass
    
 
    def add_cube(self,cube):
        pass