#
# 
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player(Board): 
    def __init__(self, checker): 
        """creates an attribute for checker and for the amount of moves made
        nume_moves"""
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self): 
        """returns Player and the checker they are"""
        return 'Player ' + self.checker
    
    def opponent_checker(self): 
        """depending on what the player checker is it will return 
        the opponents checker"""
        if self.checker == 'X':
            return 'O'
        if self.checker == 'O': 
            return 'X'
    
    def  next_move(self,b): 
        """uses the can_add_to function and checks if the player can add a checker to that column"""
        self.num_moves +=1
        while True: 
            col = int(input('Enter a column: ' ))
            if b.can_add_to(col) == True: 
                return col
            else: 
                print('Try again', end='')
                print()