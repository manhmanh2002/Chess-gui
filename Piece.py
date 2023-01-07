# Các class quân cờ

from enums import Player


class Piece:
    # khởi tạo các quân cờ
    def __init__(self, name, row_number, col_number, player):
        self._name = name
        self.row_number = row_number
        self.col_number = col_number
        self._player = player

    # giá trị x
    def get_row_number(self):
        return self.row_number

    # giá trị y
    def get_col_number(self):
        return self.col_number

    # tên
    def get_name(self):
        return self._name

    def get_player(self):
        return self._player

    def is_player(self, player_checked):
        return self.get_player() == player_checked

    def can_move(self, board, starting_square):
        pass

    def can_take(self, is_check):
        pass

    def change_row_number(self, new_row_number):
        self.row_number = new_row_number

    def change_col_number(self, new_col_number):
        self.col_number = new_col_number

    def get_valid_piece_takes(self, chess_state):
        pass

    def get_valid_peaceful_moves(self, chess_state):
        pass

    # chuyển động
    def get_valid_piece_moves(self, board):
        pass


# quân xe
class Rock(Piece):
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)
        self.has_moved = False

    def get_valid_peaceful_moves(self, chess_state):
        return self.traverse(chess_state)[0]

    def get_valid_piece_takes(self, chess_state):
        return self.traverse(chess_state)[1]

    def get_valid_piece_moves(self, chess_state):
        return self.get_valid_peaceful_moves(chess_state) + self.get_valid_piece_takes(chess_state)

    def traverse(self, chess_state):
        _peaceful_moves = []
        _piece_takes = []

        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1

        # bên trái
        self._breaking_point = False
        while self.get_col_number() - self._left >= 0 and not self._breaking_point:
            # khi ô vuông bên trái trống
            if chess_state.get_piece(self.get_row_number(), self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number(), self.get_col_number() - self._left))
                self._left += 1
            elif chess_state.is_valid_piece(self.get_row_number(), self.get_col_number() - self._left) and \
                    not chess_state.get_piece(self.get_row_number(), self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number(), self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # bên phải
        self._breaking_point = False
        while self.get_col_number() + self._right < 8 and not self._breaking_point:
            # khi ô vuông bên trái trống
            if chess_state.get_piece(self.get_row_number(), self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number(), self.get_col_number() + self._right))
                self._right += 1
            elif chess_state.is_valid_piece(self.get_row_number(), self.get_col_number() + self._right) and \
                    not chess_state.get_piece(self.get_row_number(), self.get_col_number() + self._right).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number(), self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # bên dưới
        self._breaking_point = False
        while self.get_row_number() + self._down < 8 and not self._breaking_point:
            # khi ô vuông bên trái trống
            if chess_state.get_piece(self.get_row_number() + self._down, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number()))
                self._down += 1
            elif chess_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number()) and \
                    not chess_state.get_piece(self.get_row_number() + self._down, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number()))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # bên trên
        self._breaking_point = False
        while self.get_row_number() - self._up >= 0 and not self._breaking_point:
            # khi ô vuông bên trái trống
            if chess_state.get_piece(self.get_row_number() - self._up, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number()))
                self._up += 1
            elif chess_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number()) and \
                    not chess_state.get_piece(self.get_row_number() - self._up, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number()))
                self._breaking_point = True
            else:
                self._breaking_point = True
        return (_peaceful_moves, _piece_takes)


# quân mã
class Knight(Piece):
    def get_valid_peaceful_moves(self, chess_state):
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = chess_state.get_piece(new_row, new_col)
            # khi mà ô vuông với new_row và new_col rỗng
            if evaluating_square == Player.EMPTY:
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_takes(self, chess_state):
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = chess_state.get_piece(new_row, new_col)
            # khi mà ô vuông với hàng mới và cột mới chứa màu sắc xác định và người chơi thứ 2
            if chess_state.is_valid_piece(new_row, new_col) and self.get_player() is not evaluating_square.get_player():
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_moves(self, chess_state):
        return self.get_valid_peaceful_moves(chess_state) + self.get_valid_piece_takes(chess_state)
# quân tượng
class Bishop(Piece):
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)

    def get_valid_piece_takes(self, chess_state):
        return self.traverse(chess_state)[1]

    def get_valid_peaceful_moves(self, chess_state):
        return self.traverse(chess_state)[0]

    def get_valid_piece_moves(self, chess_state):
        return self.get_valid_piece_takes(chess_state) + self.get_valid_peaceful_moves(chess_state)

    def traverse(self, chess_state):
        _peaceful_moves = []
        _piece_takes = []

        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() - self._left >= 0 and self.get_row_number() - self._up >= 0 and not self._breaking_point:
            # khi mà ô vuông trống
            if chess_state.get_piece(self.get_row_number() - self._up, self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number() - self._left))
                self._left += 1
                self._up += 1
            elif chess_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number() - self._left) and \
                    not chess_state.get_piece(self.get_row_number() - self._up, self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # bên phải quân tượng
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() + self._right < 8 and self.get_row_number() - self._up >= 0 and not self._breaking_point:
            # khi ô vuông trống
            if chess_state.get_piece(self.get_row_number() - self._up, self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number() + self._right))
                self._right += 1
                self._up += 1
            elif chess_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number() + self._right) and \
                    not chess_state.get_piece(self.get_row_number() - self._up, self.get_col_number() + self._right).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # bên dưới bên phải quân tượng
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() - self._left >= 0 and self.get_row_number() + self._down < 8 and not self._breaking_point:
            # khi ô vuông trống
            if chess_state.get_piece(self.get_row_number() + self._down, self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number() - self._left))
                self._down += 1
                self._left += 1
            elif chess_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number() - self._left) and \
                    not chess_state.get_piece(self.get_row_number() + self._down, self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # bên phải bên dưới quân tương
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() + self._right < 8 and self.get_row_number() + self._down < 8 and not self._breaking_point:
            # khi ô vuông trống
            if chess_state.get_piece(self.get_row_number() + self._down, self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number() + self._right))
                self._down += 1
                self._right += 1
            elif chess_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number() + self._right) and \
                    not chess_state.get_piece(self.get_row_number() + self._down, self.get_col_number() + self._right).is_player(
                        self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True
        return (_peaceful_moves, _piece_takes)



# quân tốt
class Pawn(Piece):
    def get_valid_piece_takes(self, chess_state):
        _moves = []
        if self.is_player(Player.PLAYER_1):
            # khi ô vuông ở vị trí dưới cùng bên trái của ô khới đầu có màu đen
            if chess_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() - 1) and \
                    chess_state.get_piece(self.get_row_number() + 1, self.get_col_number() - 1).is_player(Player.PLAYER_2):
                _moves.append((self.get_row_number() + 1, self.get_col_number() - 1))
            # khi ô vuông ở vị trí dưới cùng bên phaỉ của ô khới đầu có màu đen
            if chess_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() + 1) and \
                    chess_state.get_piece(self.get_row_number() + 1, self.get_col_number() + 1).is_player(Player.PLAYER_2):
                _moves.append((self.get_row_number() + 1, self.get_col_number() + 1))
            if chess_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() + 1, chess_state.previous_piece_en_passant()[1]))
        # khi quân tốt màu đen
        elif self.is_player(Player.PLAYER_2):
            # khi ô vuông ở vị trí bên trên phía trái của ô khởi đầu có màu trắng
            if chess_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() - 1) and \
                    chess_state.get_piece(self.get_row_number() - 1, self.get_col_number() - 1).is_player(Player.PLAYER_1):
                _moves.append((self.get_row_number() - 1, self.get_col_number() - 1))
            # khi ô vuông ở vị trí bên trên phía trái của ô khởi đầu có màu trắng
            if chess_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() + 1) and \
                    chess_state.get_piece(self.get_row_number() - 1, self.get_col_number() + 1).is_player(Player.PLAYER_1):
                _moves.append((self.get_row_number() - 1, self.get_col_number() + 1))
            if chess_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() - 1, chess_state.previous_piece_en_passant()[1]))
        return _moves

    def get_valid_peaceful_moves(self, chess_state):
        _moves = []
        # khi quân tốt màu trắng
        if self.is_player(Player.PLAYER_1):
            # khi ô bên dưới bên phải ô vuông rỗng
            if chess_state.get_piece(self.get_row_number() + 1, self.get_col_number()) == Player.EMPTY:
                # khi quân tốt chưa được di chuyển
                if self.get_row_number() == 1 and chess_state.get_piece(self.get_row_number() + 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append((self.get_row_number() + 1, self.get_col_number()))
                    _moves.append((self.get_row_number() + 2, self.get_col_number()))
                # khi quân tốt đã được di chuyển
                else:
                    _moves.append((self.get_row_number() + 1, self.get_col_number()))
        # khi quân tốt là quân đen
        elif self.is_player(Player.PLAYER_2):
            # khi ô vuông trên bên phải rỗng
            if chess_state.get_piece(self.get_row_number() - 1, self.get_col_number()) == Player.EMPTY:
                # khi quân tốt chưa di chuyển
                if self.get_row_number() == 6 and chess_state.get_piece(self.get_row_number() - 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append((self.get_row_number() - 1, self.get_col_number()))
                    _moves.append((self.get_row_number() - 2, self.get_col_number()))
                # khi quân tốt đã di chuyển
                else:
                    _moves.append((self.get_row_number() - 1, self.get_col_number()))
        return _moves

    def get_valid_piece_moves(self, chess_state):
        return self.get_valid_peaceful_moves(chess_state) + self.get_valid_piece_takes(chess_state)


# quân hậu
class Queen(Rock, Bishop):
    def get_valid_peaceful_moves(self, chess_state):
        return (Rock.get_valid_peaceful_moves(Rock(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), chess_state) +
                Bishop.get_valid_peaceful_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), chess_state))

    def get_valid_piece_takes(self, chess_state):
        return (Rock.get_valid_piece_takes( Rock(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), chess_state) +
                Bishop.get_valid_piece_takes(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), chess_state))

    def get_valid_piece_moves(self, chess_state):
        return (Rock.get_valid_piece_moves(Rock(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), chess_state) +
                Bishop.get_valid_piece_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), chess_state))

# quân vua
class King(Piece):
    def get_valid_piece_takes(self, chess_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = chess_state.get_piece(new_row, new_col)
            # khi ô vuông với hàng mới và cột mới chứa màu xác định
            if chess_state.is_valid_piece(new_row, new_col):
                # khi mà vua trắng và các màu cạnh quân vua là màu đen
                if self.is_player(Player.PLAYER_1) and evaluating_square.is_player(Player.PLAYER_2):
                    _moves.append((new_row, new_col))
                # khi mà vua đen và các màu cạnh quân vua là màu trắng
                elif self.is_player(Player.PLAYER_2) and evaluating_square.is_player(Player.PLAYER_1):
                    _moves.append((new_row, new_col))
        return _moves

    def get_valid_peaceful_moves(self, chess_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = chess_state.get_piece(new_row, new_col)
            # khi mà ô vuông với new_row và new_col rỗng
            if evaluating_square == Player.EMPTY:
                _moves.append((new_row, new_col))

        if chess_state.king_can_castle_left(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 1))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 1))
        elif chess_state.king_can_castle_right(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 5))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 5))
        return _moves

    def get_valid_piece_moves(self, chess_state):
        return self.get_valid_peaceful_moves(chess_state) + self.get_valid_piece_takes(chess_state)
