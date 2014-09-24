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

w = '~'
hit = '*'


grid = [
    [' ',0,1,2,3,4,5,6,7,8,9],
    ['A',w,w,w,w,w,w,w,w,w,w],
    ['B',w,w,w,w,w,w,w,w,w,w],
    ['C',w,w,w,w,w,w,w,w,w,w],
    ['D',w,w,w,w,w,w,w,w,w,w],
    ['E',w,w,w,w,w,w,w,w,w,w],
    ['F',w,w,w,w,w,w,w,w,w,w],
    ['G',w,w,w,w,w,w,w,w,w,w],
    ['H',w,w,w,w,w,w,w,w,w,w],
    ['I',w,w,w,w,w,w,w,w,w,w],
    ['J',w,w,w,w,w,w,w,w,w,w]
]


for row in grid:
    for col in row:
        print(col,end=' ')
    print("")
