
class Grid():

    def __init__(self,rows=10,cols=10,char='~'):
        self.cols = []
        for row in range(cols):
            self.cols.append(char)
        
class Player():
    pass

class ComputerPlayer(Player):
    pass

class HumanPlayer(Player):
    pass

class ShellController():

    def run(self):
        print('Welcome to ConnectFour!') 
    
    
if __name__=='__main__':

    #game = ShellController()
    #game.run()
    grid = Grid(12,12)
    print(grid.cols) 
    
