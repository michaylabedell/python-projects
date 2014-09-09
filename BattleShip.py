class Ship():
    size = None


class Carrier(Ship) :
    size = 5

class Battleship(Ship) :
    size = 4

class Submarine(Ship) :
    size = 3

class Destroyer(Ship) :
    size = 2

class PatrolBoat(Ship) :
    size = 2
    

print(Carrier.size)
print(Battleship.size)
print(Submarine.size)
print(Destroyer.size)
print(PatrolBoat.size) 
