import numpy as np
from termcolor import colored

class TicTacToe:
    def __init__(self):
        self.board = np.array([['_' for _ in range(3)] for _ in range(3)])
        self.player = 1
        self.max_depth = 2 # adjust max depth as per requirement
    def check_game_over(self):
        for row in self.board:
            if row.tolist() == ['X', 'X', 'X']:
                return 1
            elif row.tolist() == ['O', 'O', 'O']:
                return 2
        for col in self.board.T:
            if col.tolist() == ['X', 'X', 'X']:
                return 1
            elif col.tolist() == ['O', 'O', 'O']:
                return 2
        diag1 = [self.board[i][i] for i in range(3)]
        diag2 = [self.board[i][2-i] for i in range(3)]
        if diag1 == ['X', 'X', 'X'] or diag2 == ['X', 'X','X']:
            return 1
        elif diag1 == ['O', 'O', 'O'] or diag2 == ['O', 'O', 'O']:
            return 2
        if not np.any(self.board == '_'):
            return 3
        return 0
    
    def minimax(self, board, depth, is_max, alpha, beta):
        result = self.check_game_over()
        if result != 0:
            if result == 1:
                return 10-depth #returning a score based on the depth of the search
            elif result == 2:
                return depth-10
            else:
                return 0
        if is_max:
            best_val = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = 'X'
                        best_val = max(best_val, self.minimax(board, depth+1, not is_max, alpha, beta))
                        alpha = max(alpha, best_val)
                        board[i][j] = '_'
                        if beta <= alpha:
                            break
                if beta <= alpha:
                    break
            return best_val
        else:
            best_val = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = 'O'
                        best_val = min(best_val, self.minimax(board, depth+1, not is_max, alpha, beta))
                        beta = min(beta, best_val)
                        board[i][j] = '_'
                        if beta <= alpha:
                            break
                if beta <= alpha:
                    break
            return best_val
    
    def find_best_move(self):
        best_val = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    self.board[i][j] = 'X'
                    move_val = self.minimax(self.board, 0, False, -float('inf'), float('inf'))
                    self.board[i][j] = '_'
                    if move_val > best_val:
                        best_val = move_val
                        best_move = (i, j)
        return best_move
    
    def play(self):
        while True:
            if self.player == 1:
                print("Player's turn")
                x, y = map(int, input("Enter row and column (0-2) : ").split())
                if self.board[x][y] == '_':
                    self.board[x][y] = 'O'
                    print(colored(f"Player's move: {x}, {y}", 'green'))
                else:
                    print("Invalid move! Try again")
                    continue
                self.player = 2
            else:
                print("Computer's turn")

                x, y = self.find_best_move()

                self.board[x][y] = 'X'
                print(colored(f"Computer's move: {x}, {y}", 'red'))
                self.player = 1

            self.print_board()

            result = self.check_game_over()

            if result != 0:
                if result == 1:
                    print("Computer wins!")
                elif result == 2:
                    print("Player wins!")
                else:
                    print("It's a tie!")
                break
            
    def print_board(self):
        for row in self.board:
            print(row)

game = TicTacToe()
game.play()


