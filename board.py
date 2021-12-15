#########################################################
###
### Board class used to create Board() objects
### Used to hold the game_board, represent child states
###
#########################
import copy
from random import randint

class Board(object):
    
    def __init__(self, player=1, score=0, board=[], parent=None, move=None, value=None, depth=0):
        self.player = player
        self.score = score
        self.board = copy.deepcopy(board)
        self.parent = parent
        self.move = move
        self.value = value
        self.depth = depth
        self.moves_remaining = float("inf")
        self.children = []
        
        if board == []:
            size = int(input("How large would you like the board to be (N x N)? \n Enter an integer: "))
            if type(size) != type(1):
                print("Invalid argument, default to size 3")
                self.createBoard()
            self.createBoard(size)

    def createBoard(self, size=3):
        self.moves_remaining = 2*size*(size-1)
        if self.board == []:
            for row in range(0, size*2 - 1): 
                self.board.append([])
                for col in range(0, size*2 - 1):
                    try:
                        if (row%2 == 0 and col%2 == 0):
                            self.board[row].append("*")
                        elif (row%2 == 1 and col%2 == 1):
                            self.board[row].append(randint(1, 9))
                        elif ((row%2 == 0) ^ (col%2 == 0)):
                            if row%2 == 0:
                                self.board[row].append("   ")
                            else:
                                self.board[row].append(" ")
                    except:
                        print("Unexpected Error While Creating Game Board") 
                   
    def makeMove(self, row=0, col=0):
        if ((row < 0) or (row > len(self.board))) or ((col < 0) or (col > len(self.board[0]))):
            return "Out Of Bounds"
        if not ((row%2 == 0) ^ (col%2 == 0)):
            return "Not A Valid Move"
        elif ((self.board[row][col] != " ") and (self.board[row][col] != "   ")):
            return "Edge Already Filled"
        elif row%2 == 0: 
            self.board[row][col] = "---"
            if (self.completeSquare(row-1, col)):
                self.score += (self.player * self.board[row-1][col]) 
            if (self.completeSquare(row+1, col)): 
                self.score += (self.player * self.board[row+1][col])
            self.player = (-1 * self.player)
        else:
            self.board[row][col] = "|"
            if (self.completeSquare(row, col-1)):
                self.score += (self.player * self.board[row][col-1])
            if (self.completeSquare(row, col+1)):
                self.score += (self.player * self.board[row][col+1])
            self.player = (-1 * self.player)
        self.moves_remaining -= 1
        
    def completeSquare(self, row, col):
            if ((row > 0) and (col > 0) and
                (row < len(self.board) - 1) and
                (col < len(self.board[0]) - 1)):
                return ((self.board[row-1][col] == "---") and
                        (self.board[row+1][col] == "---") and
                        (self.board[row][col-1] == "|") and
                        (self.board[row][col+1] == "|"))
                
    def getChildren(self):
        p, s, b, pr, d = self.player, copy.deepcopy(self.score), copy.deepcopy(self.board), self, (self.depth+1) 
        for row in range(0, len(self.board)): 
            if row%2 == 0: 
                for col in range(1, len(self.board[0]), 2):
                    if self.board[row][col] != "---":
                        child = Board(player=p, score=s, board=b, parent=pr, move=(row, col), depth=d)
                        child.makeMove(row, col)
                        self.children.append(child)
            else:
                for col in range(0, len(self.board[0]), 2):
                    if self.board[row][col] != "|": 
                        child = Board(player=p, score=s, board=b, parent=pr, move=(row, col), depth=d)
                        child.makeMove(row, col)
                        self.children.append(child)
               
    def isOver(self):
        if self.moves_remaining <= 0:
            return True
        return False
        

    def display(self): 
        board = self.board
        print("  ", end='')
        for idx in range(0, len(board[0])): 
            if idx%2 == 1:
                print(" {} ".format(idx), end='')
            else:
                print(idx, end='')
        print("\n")
        for row in range (0, (len(board))):
            print("{} ".format(row), end='')
            for col in range(0, (len(board[0]))):
                if (row%2 ==0) and (col%2 ==0):
                    print(board[row][col], end='')
                elif row%2 == 0:
                    print(board[row][col], end='')
                elif col%2 == 0:
                    print(board[row][col], end='')
                else:
                    print(" {} ".format(board[row][col]), end='')
            print("\n")
        print("\n")
        print(self.score)
                        
    def copy(self):
        p, s, b, pr, m, d = self.player, copy.deepcopy(self.score), copy.deepcopy(self.board), self, self.move, self.depth
        return Board(p, s, b, pr, m, d)
    
    def getScore(self):
        return copy.deepcopy(self.score)   
