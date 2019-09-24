import Player


class Game:

    def __init__(self):
        self.player_1 = None
        self.player_2 = None
        self.current_player = None
        self.current_player_index = None
        self.remaining_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.winning_moves = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    def initialize(self):
        self.player_1 = Player.Player(input('Enter player1 name:'), 'X')
        self.player_2 = Player.Player(input('Enter player2 name:'), 'O')
        self.current_player = self.player_1
        self.current_player_index = 0
        self.show_board()

    def is_draw(self):
        return len(self.remaining_moves) is 0

    def is_valid_move(self, move):
        return move in self.remaining_moves

    def start(self):
        while not self.has_won():
            if self.is_draw():
                print('draw!!!!!')
                return
            input_move = int(input(self.current_player.name+'\'s turn \n Enter your move:'))
            while not self.is_valid_move(input_move):
                input_move = int(input('Invalid move!! Please Enter valid move:'))
            self.place_move(input_move)
            if self.has_won():
                print(self.current_player.name, 'won the game!!')
                return
            self.switch_player()

    def place_move(self, input_move):
        self.current_player.moves.append(input_move)
        self.remaining_moves.remove(input_move)
        self.board[input_move - 1] = self.current_player.symbol
        self.show_board()

    def is_subset(self, x):
        set(x).issubset(self.current_player.moves)

    def has_won(self):
        for x in self.winning_moves:
            if self.is_subset(x):
                return True
        return False

    def switch_player(self):
        if self.current_player_index is 0:
            self.current_player = self.player_2
            self.current_player_index = 1
        else:
            self.current_player = self.player_1
            self.current_player_index = 0

    def show_board(self):
        print(' '+self.board[0]+'|'+self.board[1]+'|'+self.board[2]+'\n-------')
        print(' '+self.board[3] + '|' + self.board[4] + '|' + self.board[5] + '\n-------')
        print(' '+self.board[6] + '|' + self.board[7] + '|' + self.board[8])
