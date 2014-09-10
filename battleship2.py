import random

class Ship():
    size = None

class PatrolBoat(Ship):
    size = 2
    
class Destroyer(ship):
    size = 3

class Submarine(Ship):
    size = 3

class Battleship(Ship):
    size = 4

class AircraftCarrier(ship):
    size = 5

#---------------------------------------------



def init_grid(grid):
    grid = [] 
    for row in range(10):
         grid[row] = [] 
        for col in range(10):
        grid[row][col] = '~'
   
       
def print_grid(grid):
    for row in range(10):
        for col in range(10):
            print(grid[row][col], end' ') 

