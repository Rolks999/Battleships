"""
Created on Fri Jun  4 15:31:51 2021

@author: rolka

Based on YouTube instructions from Robert Heaton
"""

import copy

class GameBoard(object):
    def __init__(self, battleships, width, height):
        self.battleships = battleships
        self.shots = []
        self.width = width
        self.height = height
    
    # Update Battleship with any hits
    # Save whether shot hit or miss
    def take_shot(self, shot_location):
        is_hit = False
        
        for b in self.battleships:
            idx = b.hull_index(shot_location)
            
            if idx is not None:
                is_hit = True
                b.hits[idx] = True
                break
                
        self.shots.append(Shot(shot_location, is_hit))
    
    def is_game_over(self):
        return all([b.is_destroyed() for b in self.battleships])
    
        
class Battleship(object):
    def __init__(self, hull):
        self.hull = hull
        self.hits = [False] * len(hull)
        
    @staticmethod 
    def build(bow, length, direction):
        hull = []
        for i in range(length):
            if direction == "N":
                section = (bow[0], bow[1] - i)
            elif direction == "S":
                section = (bow[0], bow[1] + i)
            elif direction == "W":
                section = (bow[0] - i, bow[1])
            elif direction == "E":
                section = (bow[0] + i, bow[1])
                
            hull.append(section)
            
        return Battleship(hull)
    
    def hull_index(self, location):
        try:
            return self.hull.index(location)
        except ValueError:
            return None
        
    def is_destroyed(self):
        return all(self.hits)

                
class Shot(object):
    def __init__(self, location, is_hit):
        self.location = location
        self.is_hit = is_hit
        

def render(game_board, show_battleships = False):
    header = "+" + "-" * game_board.width + "+"
    
    print(header)

    # Construct empty board
    board = []
    
    for x in range(game_board.width):
        row = []
        
        for y in range(game_board.height):
            row.append(" ")
        
        board.append(row)
        
    # Add the battleships to the board
    if show_battleships:
        for b in game_board.battleships:
            for x, y in b.hull:
                board[x][y] = "O"
    
    # Add the shots to the board
    for sh in game_board.shots:
        x, y = sh.location
        
        if sh.is_hit:
            p = "X"
        else:
            p = "."
        board[x][y] = p
    
    # Render full board 
    for y in range(game_board.height):
        row = []
        
        for x in range(game_board.width):
            row.append(board[x][y])

        print("|" + "".join(row) + "|")

    print(header)


if __name__ == "__main__":
    battleships = [
        Battleship.build((1,1), 2, "S"),
        # Battleship.build((5,8), 5, "N"),
        # Battleship.build((2,3), 4, "E")
    ]
    
    game_boards = [
        GameBoard(battleships, 10, 10),
        GameBoard(copy.deepcopy(battleships), 10, 10)
    ]
    
    off_idx = 0    
    while True:
        def_idx = (off_idx + 1) % 2
        def_board = game_boards[def_idx]
        
        print("Player %d, it is your turn" % (off_idx + 1))
        inp = input("Where do you want to shoot?\n")
        xstr, ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)
        
        def_board.take_shot((x,y))
        render(def_board)

        if def_board.is_game_over():
            print("PLAYER %d YOU WIN!" % (off_idx + 1))
            break
        
        off_idx = def_idx
        