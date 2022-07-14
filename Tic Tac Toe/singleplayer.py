# Singleplayer version of TicTacToe

import random 

class TicTacToe:
    def __init__(self):
        self.pl = str(input("\nX or O?: ")).lower()
        if self.pl == 'x':
            self.cl = 'o'
        else:
            self.cl = 'x' 
            self.pl = 'o'

        self.board = ['-' for i in range(9)]
        self.game_over = False 
        self.winner = None 

    def play_tictactoe(self):
        self.print_board()
        while not self.game_over:
            self.player_turn()
            self.check_winner()
            self.check_tie()
            self.computer_turn()
            self.check_winner()
            self.check_tie()

        print(f"\nThe winner is: {self.winner}")

    def print_board(self):
        print()
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}         {i+1} | {i+2} | {i+3}")

    def player_turn(self):
        self.player_spottaken = True 

        while self.player_spottaken:
            self.user_choice = int(input(f"\nChoose where to place {self.pl}. 1 to 9: "))
            while self.user_choice > 9 or self.user_choice < 1:
                print("\nThat spot is invalid. Choose again.")
                self.user_choice = int(input(f"\nChoose where to place {self.pl}. 1 to 9: "))
            self.user_choice -= 1

            if self.board[self.user_choice] == '-':
                self.player_spottaken = False 
            else:
                print("\nThat spot is already taken. Go again.")

        self.board[self.user_choice] = self.pl 
        self.print_board()

    def computer_turn(self):
        self.computer_spottaken = True 

        while self.computer_spottaken:
            self.computer_choice = random.randint(0, 8)
            if self.board[self.computer_choice] == '-':
                self.computer_spottaken = False 

        self.board[self.computer_choice] = self.cl 
        print("\nThe computer has made a move.")
        self.print_board()

    def check_rows(self):
        self.row_1 = self.board[0] == self.board[1] == self.board[2] != '-'
        self.row_2 = self.board[3] == self.board[4] == self.board[5] != '-'
        self.row_3 = self.board[6] == self.board[7] == self.board[8] != '-'

        if self.row_1 or self.row_2 or self.row_3:
            self.game_over = True 

        if self.row_1:
            return self.board[0]
        elif self.row_2:
            return self.board[3]
        elif self.row_3:
            return self.board[6]
        else:
            return None 

    def check_columns(self):
        self.column_1 = self.board[0] == self.board[3] == self.board[6] != '-'
        self.column_2 = self.board[1] == self.board[4] == self.board[7] != '-'
        self.column_3 = self.board[2] == self.board[5] == self.board[8] != '-'

        if self.column_1 or self.column_2 or self.column_3:
            self.game_over = True 

        if self.column_1:
            return self.board[0]
        elif self.column_2:
            return self.board[1]
        elif self.column_3:
            return self.board[2]
        else:
            return None 

    def check_diagonals(self):
        self.diagonal_one = self.board[0] == self.board[4] == self.board[8] != '-'
        self.diagonal_two = self.board[2] == self.board[4] == self.board[6] != '-'

        if self.diagonal_one or self.diagonal_two:
            self.game_over = True 

        if self.diagonal_one:
            return self.board[0]
        elif self.diagonal_two:
            return self.board[2]
        else:
            return None

    def check_winner(self):
        self.row_winner = self.check_rows()
        self.column_winner = self.check_columns()
        self.diagonal_winner = self.check_diagonals() 

        if self.row_winner:
            self.winner = self.row_winner
        elif self.column_winner:
            self.winner = self.column_winner
        elif self.diagonal_winner:
            self.winner = self.diagonal_winner
        else:
            self.winner = None 

    def check_tie(self):
        if '-' not in self.board:
            print('\nTie!')
            exit() 

def main():
    t = TicTacToe()
    t.play_tictactoe()
    print()

main()