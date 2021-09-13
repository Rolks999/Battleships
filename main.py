"""
Created on Fri Jun  4 15:31:51 2021

@author: rolka

Based on YouTube instructions from Robert Heaton
"""

class Battleship(object):
    
    def __init__(self, hull):
        self.hull = hull
        
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
                
def render_battleships(board_width, board_height, battleships):
    header = "+" + "-" * board_width + "+"
    
    print(header)

    #Construct empty board
    board = []
    
    for x in range(board_width):
        row = []
        
        for y in range(board_height):
            row.append(" ")
        
        board.append(row)
        
    # Add the battleships to the board
    for b in battleships:
        for x, y in b.hull:
            board[x][y] = "O"
    
    for y in range(board_height):
        row = []
        
        for x in range(board_width):
            row.append(board[x][y])

        print("|" + "".join(row) + "|")

    print(header)
    
def render(board_width, board_height, shots):
    header = "+" + "-" * board_width + "+"
    
    print(header)
    
    shots_set = set(shots)
    for y in range(board_height):
        row = []
        
        for x in range(board_width):
            if (x,y) in shots_set:
                ch = "X"
            else:
                ch = " "
            row.append(ch)
        
        print("|" + "".join(row) + "|")
        
    print(header)
    

if __name__ == "__main__":

    battleships = [
        Battleship.build((1,1), 2, "S"),
        Battleship.build((5,8), 5, "N"),
        Battleship.build((2,3), 4, "E")
    ]

    for b in battleships:
        print(b.hull)
        
    render_battleships(10, 10, battleships)
    

"""
    exit(0)

    shots = []
    
    while True:
        inp = input("Where do you want to shoot?\n")
        xstr, ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)
        
        shots.append((x,y))
        render(10, 10, shots)
"""