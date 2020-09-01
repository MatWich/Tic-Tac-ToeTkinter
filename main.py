from game import *
from config import *

game = Game(O)      # game = Game(X) if X should go first
game.setUp()        # Creates window and all buttons
game.mainLoop()     # refreshing screen