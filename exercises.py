# As a user (AAU), I want to see a welcome message at start of a game.

# AAU, before being prompted for a move, I want to see board printed in console to know what moves have been made.

# AAU, at beginning of each turn, told whose turn it is: It’s player X’s turn!

# AAU, I should be prompted to enter a move and be provided an example of valid input ('Enter a valid move (example: A1)').

# AAU, I want to be able to enter my move’s column letter in upper or lower case (a/A, b/B, or c/C) to make it easier to enter my move.

# AAU, if I enter a move in an invalid format or try to occupy a cell already taken, I want to see a message chastising me and be re-prompted.

# AAU, after entering a move, I should once again be presented with updated game board, notified of current turn,... 
    # ...and asked to enter a move for r player. This process should continue untilre is a winner or a tie

# AAU, I should see a message at end of game indicating winner or stating that game ended in a tie.


#==============================================================TIK-TAK-TOE=====================================================================#

# *Step 1: Define Game Class:
class Game:

    # Within Game class, use __init__ method to initialize properties that represent state of your game.
    def __init__(self):

        # Initialise game state with attributes for turn, tie, winner, board

        # turn: a string attribute indicating whose turn it is ('X' or 'O'). Initialize it with 'X'.
        self.turn = 'X'  

        # tie: a boolean attribute indicating if game ended in a tie. Initialize it as False.
        self.tie = False  

        # winner: an attribute to store game-winner. Initialize it as None.
        self.winner = None

        # board: a dictionary representing state of game board:
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

 #---------------------------------------------------------------------------------------------------------------------------------------------#       

# * Step 3 - Rendering
    
    # Rendering the board:  The print_board method visualizes the current state of the game board.    
    def print_board(self):

        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    # Rendering messages: The print_message method updates users about the current status of a game, 
                        # ...including whose turn it is, who won the game, and if the game ended in a tie.
    
    def print_message(self):

        # Print message indicating game's status
        if self.tie:

            # Inform players if game tied
            print("Tie game!")

        elif self.winner:

            # Announce winner
            print(f"{self.winner} wins game!")  

        else:
            # Indicate turn
            print(f"It's player {self.turn}'s turn!")  

    # Consolidated rendering: Optionally, a third render method can be used to consolidate the other two, streamlining the rendering process:       

    def render(self):
       
        # Call upon print_board
        self.print_board()

        # Call upon print_message
        self.print_message()

#---------------------------------------------------------------------------------------------------------------------------------------------# 
    
# * Step 4 - Handling player input

# you’ll need a method to handle user input, such as get_move or place_piece... 
# ..This method should prompt a user to enter the key of an empty space on the board.
    
    def get_move(self):

        # Continuously prompt player until a valid move is entered
        while True:

            # To capture player input, use the input() function. 
            # This function displays a prompt in the terminal and returns the string that the user enters.
            move = input(f"Enter a valid move (example: A1): ").lower()

            if move in self.board and self.board[move] is None:

                # Update board with current player's move
                self.board[move] = self.turn

                # Exit loop when a valid move is made  
                break

            # otherwise, print a message notifying the user of the invalid input and allow the loop to continue  
            else:
                print("Invalid move, please try again.") 

#---------------------------------------------------------------------------------------------------------------------------------------------# 

# *Step 5 - Checking for a winner

# create a method for determining a winner by checking the board for the eight possible winning combinations. Upon detecting a winning combination, 
# ...update the winner attribute to reflect the current player (turn).

    def check_for_winner(self):

        # List all possible winning combinations
        winning_combinations = [

            # Horizontal
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
            # Vertical  
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  
            # Diagonal
            ['a1', 'b2', 'c3'], ['c1', 'b2', 'a3']  
        ]

        for combo in winning_combinations:

            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:

                # Declare current player as winner if any combo is met
                self.winner = self.turn  
                return

#---------------------------------------------------------------------------------------------------------------------------------------------# 

# * Step 6 - Checking for a tie

# This method should check if both of the following conditions are true: 
# The board is entire: All spaces on the board are filled, with no positions marked as None.
# No winner: A winner has not already been declared.
# If both of these conditions are met, the value of tie should be set to True.

    def check_for_tie(self):

        # Check if board is full and no winner, declare a tie
        if all(self.board[pos] is not None for pos in self.board) and not self.winner:
            self.tie = True

#---------------------------------------------------------------------------------------------------------------------------------------------#

# * Step 7 - Switching turns

# The switch_turn method should alternate the value of turn between 'X' and 'O'. This should occur at the end of every turn. 
# There are several ways to accomplish this, but a small lookup table using a dictionary might work nicely.

    def switch_turn(self):

        # Switch current player from 'X' to 'O' or vice~versa
        self.turn = 'O' if self.turn == 'X' else 'X'

#---------------------------------------------------------------------------------------------------------------------------------------------#        

# * Step 2 - Playing the game

    # Define a play_game method and confirm that method is accessible on an instance of Game class... 
        #...This function will be used to activate and organize flow of game.
    def play_game(self):        

        #Within play_game method, print a welcome message of your choosing.
        print("Welcome to Tic-Tac-Toe!")

#---------------------------------------------------------------------------------------------------------------------------------------------#        

# * Step 8 - Managing gameplay

# The last step is combining all these methods in a functional gameplay loop. The loop should continue until a winner or tie is declared.

        # Main game loop that runs until a winner or tie
        while not self.winner and not self.tie:

            # Show current game state
            self.render()  

            # Prompt current player for a move
            self.get_move()

            # Check if current move caused a win
            self.check_for_winner()

            # Check if game is a tie
            self.check_for_tie()  

            if not self.winner and not self.tie:

                # Switch turns if game continues
                self.switch_turn()  

        # Final render to show game result
        self.render()  

#---------------------------------------------------------------------------------------------------------------------------------------------#        

# * Start game

if __name__ == "__main__":

    #Instantiate the Game class 
    game = Game()

    #invoke the play_game method:
    game.play_game()
