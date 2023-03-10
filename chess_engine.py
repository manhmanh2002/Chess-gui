from Piece import Rock, Knight, Bishop, Queen, King, Pawn
from enums import Player

'''
r \ c     0           1           2           3           4           5           6           7 
0   [(r=0, c=0), (r=0, c=1), (r=0, c=2), (r=0, c=3), (r=0, c=4), (r=0, c=5), (r=0, c=6), (r=0, c=7)]
1   [(r=1, c=0), (r=1, c=1), (r=1, c=2), (r=1, c=3), (r=1, c=4), (r=1, c=5), (r=1, c=6), (r=1, c=7)]
2   [(r=2, c=0), (r=2, c=1), (r=2, c=2), (r=2, c=3), (r=2, c=4), (r=2, c=5), (r=2, c=6), (r=2, c=7)]
3   [(r=3, c=0), (r=3, c=1), (r=3, c=2), (r=3, c=3), (r=3, c=4), (r=3, c=5), (r=3, c=6), (r=3, c=7)]
4   [(r=4, c=0), (r=4, c=1), (r=4, c=2), (r=4, c=3), (r=4, c=4), (r=4, c=5), (r=4, c=6), (r=4, c=7)]
5   [(r=5, c=0), (r=5, c=1), (r=5, c=2), (r=5, c=3), (r=5, c=4), (r=5, c=5), (r=5, c=6), (r=5, c=7)]
6   [(r=6, c=0), (r=6, c=1), (r=6, c=2), (r=6, c=3), (r=6, c=4), (r=6, c=5), (r=6, c=6), (r=6, c=7)]
7   [(r=7, c=0), (r=7, c=1), (r=7, c=2), (r=7, c=3), (r=7, c=4), (r=7, c=5), (r=7, c=6), (r=7, c=7)]
'''
class chess_state:
    # khởi tạo mảng 2D để biểu diễn bàn cờ
    def __init__(self):
        self.white_captives = []
        self.black_captives = []
        self.move_log = []
        self.white_turn = True
        self.can_en_passant_bool = False
        self._en_passant_previous = (-1, -1)
        self.checkmate = False
        self.stalemate = False

        self._is_check = False
        self._white_king_location = [0, 3]
        self._black_king_location = [7, 3]

        self.white_king_can_castle = [True, True,
                                      True]  # quân vua không di chuyển có biến Rock1(col=0) không di chuyển, biến Rock2(col=7) không di chuyển
        self.black_king_can_castle = [True, True, True]

        # khởi tạo quân trắng
        white_rock_1 = Rock('r', 0, 0, Player.PLAYER_1)
        white_rock_2 = Rock('r', 0, 7, Player.PLAYER_1)
        white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
        white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
        white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
        white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
        white_queen = Queen('q', 0, 4, Player.PLAYER_1)
        white_king = King('k', 0, 3, Player.PLAYER_1)
        white_pawn_1 = Pawn('p', 1, 0, Player.PLAYER_1)
        white_pawn_2 = Pawn('p', 1, 1, Player.PLAYER_1)
        white_pawn_3 = Pawn('p', 1, 2, Player.PLAYER_1)
        white_pawn_4 = Pawn('p', 1, 3, Player.PLAYER_1)
        white_pawn_5 = Pawn('p', 1, 4, Player.PLAYER_1)
        white_pawn_6 = Pawn('p', 1, 5, Player.PLAYER_1)
        white_pawn_7 = Pawn('p', 1, 6, Player.PLAYER_1)
        white_pawn_8 = Pawn('p', 1, 7, Player.PLAYER_1)
        self.white_pieces = [white_rock_1, white_rock_2, white_knight_1, white_knight_2, white_bishop_1, white_bishop_2,
                             white_queen, white_king, white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4,
                             white_pawn_5,
                             white_pawn_6, white_pawn_7, white_pawn_8]

        # khởi tạo quân đen
        black_rock_1 = Rock('r', 7, 0, Player.PLAYER_2)
        black_rock_2 = Rock('r', 7, 7, Player.PLAYER_2)
        black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
        black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
        black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
        black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
        black_queen = Queen('q', 7, 4, Player.PLAYER_2)
        black_king = King('k', 7, 3, Player.PLAYER_2)
        black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
        black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
        black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
        black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
        black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
        black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
        black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
        black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)
        self.black_pieces = [black_rock_1, black_rock_2, black_knight_1, black_knight_2, black_bishop_1, black_bishop_2,
                             black_queen, black_king, black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4,
                             black_pawn_5,
                             black_pawn_6, black_pawn_7, black_pawn_8]

        self.board = [
            [white_rock_1, white_knight_1, white_bishop_1, white_king, white_queen, white_bishop_2, white_knight_2,
             white_rock_2],
            [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7,
             white_pawn_8],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4, black_pawn_5, black_pawn_6, black_pawn_7,
             black_pawn_8],
            [black_rock_1, black_knight_1, black_bishop_1, black_king, black_queen, black_bishop_2, black_knight_2,
             black_rock_2]
        ]

    def get_piece(self, row, col):
        if (0 <= row < 8) and (0 <= col < 8):
            return self.board[row][col]

    def is_valid_piece(self, row, col):
        evaluated_piece = self.get_piece(row, col)
        return (evaluated_piece is not None) and (evaluated_piece != Player.EMPTY)

    def get_valid_moves(self, starting_square):

        current_row = starting_square[0]
        current_col = starting_square[1]

        if self.is_valid_piece(current_row, current_col):
            valid_moves = []
            moving_piece = self.get_piece(current_row, current_col)
            if self.get_piece(current_row, current_col).is_player(Player.PLAYER_1):
                king_location = self._white_king_location
            else:
                king_location = self._black_king_location
            group = self.check_for_check(king_location, moving_piece.get_player())
            checking_pieces = group[0]
            pinned_pieces = group[1]
            pinned_checks = group[2]
            initial_valid_piece_moves = moving_piece.get_valid_piece_moves(self)

            # chiếu tướng
            if checking_pieces:
                for move in initial_valid_piece_moves:
                    can_move = True
                    for piece in checking_pieces:
                        if moving_piece.get_name() == "k":
                            temp = self.board[current_row][current_col]
                            self.board[current_row][current_col] = Player.EMPTY
                            temp2 = self.board[move[0]][move[1]]
                            self.board[move[0]][move[1]] = temp
                            if not self.check_for_check(move, moving_piece.get_player())[0]:
                                pass
                            else:
                                can_move = False
                            self.board[current_row][current_col] = temp
                            self.board[move[0]][move[1]] = temp2
                        elif move == piece and len(checking_pieces) == 1 and moving_piece.get_name() != "k" and \
                                (current_row, current_col) not in pinned_pieces:
                            pass
                        elif move != piece and len(checking_pieces) == 1 and moving_piece.get_name() != "k" and \
                                (current_row, current_col) not in pinned_pieces:
                            temp = self.board[move[0]][move[1]]
                            self.board[move[0]][move[1]] = moving_piece
                            self.board[current_row][current_col] = Player.EMPTY
                            if self.check_for_check(king_location, moving_piece.get_player())[0]:
                                can_move = False
                            self.board[current_row][current_col] = moving_piece
                            self.board[move[0]][move[1]] = temp
                        else:
                            can_move = False
                    if can_move:
                        valid_moves.append(move)
                self._is_check = True
            # kiểm tra có di chuyển hay không
            elif pinned_pieces and moving_piece.get_name() != "k":
                if starting_square not in pinned_pieces:
                    for move in initial_valid_piece_moves:
                        valid_moves.append(move)
                elif starting_square in pinned_pieces:
                    for move in initial_valid_piece_moves:

                        temp = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = moving_piece
                        self.board[current_row][current_col] = Player.EMPTY
                        if not self.check_for_check(king_location, moving_piece.get_player())[0]:
                            valid_moves.append(move)
                        self.board[current_row][current_col] = moving_piece
                        self.board[move[0]][move[1]] = temp
            else:
                if moving_piece.get_name() == "k":
                    for move in initial_valid_piece_moves:
                        temp = self.board[current_row][current_col]
                        temp2 = self.board[move[0]][move[1]]
                        self.board[current_row][current_col] = Player.EMPTY
                        self.board[move[0]][move[1]] = temp
                        if not self.check_for_check(move, moving_piece.get_player())[0]:
                            valid_moves.append(move)
                        self.board[current_row][current_col] = temp
                        self.board[move[0]][move[1]] = temp2
                else:
                    for move in initial_valid_piece_moves:
                        valid_moves.append(move)
            return valid_moves
        else:
            return None

    # 0 nếu trắng thua, 1 nếu đen thua, 2 if hòa, 3 if không kết thúc
    def checkmate_stalemate_checker(self):
        all_white_moves = self.get_all_legal_moves(Player.PLAYER_1)
        all_black_moves = self.get_all_legal_moves(Player.PLAYER_2)
        if self._is_check and self.whose_turn() and not all_white_moves:
            return 0
        elif self._is_check and not self.whose_turn() and not all_black_moves:
            return 1
        elif not all_white_moves and not all_black_moves:
            return 2
        else:
            return 3

    def get_all_legal_moves(self, player):
        _all_valid_moves = []
        for row in range(0, 8):
            for col in range(0, 8):
                if self.is_valid_piece(row, col) and self.get_piece(row, col).is_player(player):
                    valid_moves = self.get_valid_moves((row, col))
                    for move in valid_moves:
                        _all_valid_moves.append(((row, col), move))
        return _all_valid_moves

    def king_can_castle_left(self, player):
        if player == Player.PLAYER_1:
            return self.white_king_can_castle[0] and self.white_king_can_castle[1] and \
                   self.get_piece(0, 1) is Player.EMPTY and self.get_piece(0, 2) is Player.EMPTY and not self._is_check
        else:
            return self.black_king_can_castle[0] and self.black_king_can_castle[1] and \
                   self.get_piece(7, 1) is Player.EMPTY and self.get_piece(7, 2) is Player.EMPTY and not self._is_check

    def king_can_castle_right(self, player):
        if player == Player.PLAYER_1:
            return self.white_king_can_castle[0] and self.white_king_can_castle[2] and \
                   self.get_piece(0, 6) is Player.EMPTY and self.get_piece(0, 5) is Player.EMPTY and not self._is_check
        else:
            return self.black_king_can_castle[0] and self.black_king_can_castle[2] and \
                   self.get_piece(7, 6) is Player.EMPTY and self.get_piece(7, 5) is Player.EMPTY and not self._is_check

    def promote_pawn(self, starting_square, moved_piece, ending_square):
        while True:
            new_piece_name = input("Change pawn to (r, n, b, q):\n")
            piece_classes = {"r": Rock, "n": Knight, "b": Bishop, "q": Queen}
            if new_piece_name in piece_classes:
                move = chess_move(starting_square, ending_square, self, self._is_check)

                new_piece = piece_classes[new_piece_name](new_piece_name, ending_square[0],
                                                          ending_square[1], moved_piece.get_player())
                self.board[ending_square[0]][ending_square[1]] = new_piece
                self.board[moved_piece.get_row_number()][moved_piece.get_col_number()] = Player.EMPTY
                moved_piece.change_row_number(ending_square[0])
                moved_piece.change_col_number(ending_square[1])
                move.pawn_promotion_move(new_piece)
                self.move_log.append(move)
                break

    def promote_pawn_ai(self, starting_square, moved_piece, ending_square):
        move = chess_move(starting_square, ending_square, self, self._is_check)
        # phong tốt thành hậu
        new_piece = Queen("q", ending_square[0], ending_square[1], moved_piece.get_player())
        self.board[ending_square[0]][ending_square[1]] = new_piece
        self.board[moved_piece.get_row_number()][moved_piece.get_col_number()] = Player.EMPTY
        moved_piece.change_row_number(ending_square[0])
        moved_piece.change_col_number(ending_square[1])
        move.pawn_promotion_move(new_piece)
        self.move_log.append(move)

    def can_en_passant(self, current_square_row, current_square_col):
        return False

    def previous_piece_en_passant(self):
        return self._en_passant_previous

    # di chuyển quân
    def move_piece(self, starting_square, ending_square, is_ai):
        current_square_row = starting_square[0] 
        current_square_col = starting_square[1]  
        next_square_row = ending_square[0]  
        next_square_col = ending_square[1]  

        if self.is_valid_piece(current_square_row, current_square_col) and \
                (((self.whose_turn() and self.get_piece(current_square_row, current_square_col).is_player(
                    Player.PLAYER_1)) or
                  (not self.whose_turn() and self.get_piece(current_square_row, current_square_col).is_player(
                      Player.PLAYER_2)))):

            # các quân cờ ở trạng thái ban đầu
            moving_piece = self.get_piece(current_square_row, current_square_col)

            valid_moves = self.get_valid_moves(starting_square)

            temp = True

            if ending_square in valid_moves:
                moved_to_piece = self.get_piece(next_square_row, next_square_col)
                if moving_piece.get_name() == "k":
                    if moving_piece.is_player(Player.PLAYER_1):
                        if moved_to_piece == Player.EMPTY and next_square_col == 1 and self.king_can_castle_left(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((0, 0), (0, 2), self)
                            self.move_log.append(move)

                            # di chuyển quân xe
                            self.get_piece(0, 0).change_col_number(2)

                            self.board[0][2] = self.board[0][0]
                            self.board[0][0] = Player.EMPTY

                            self.white_king_can_castle[0] = False
                            self.white_king_can_castle[1] = False

                        elif moved_to_piece == Player.EMPTY and next_square_col == 5 and self.king_can_castle_right(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((0, 7), (0, 4), self)
                            self.move_log.append(move)
                            # di chuyển xe
                            self.get_piece(0, 7).change_col_number(4)

                            self.board[0][4] = self.board[0][7]
                            self.board[0][7] = Player.EMPTY

                            self.white_king_can_castle[0] = False
                            self.white_king_can_castle[2] = False
                        else:
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            self.move_log.append(move)
                            self.white_king_can_castle[0] = False
                        self._white_king_location = (next_square_row, next_square_col)
                    else:
                        if moved_to_piece == Player.EMPTY and next_square_col == 1 and self.king_can_castle_left(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((7, 0), (7, 2), self)
                            self.move_log.append(move)

                            self.get_piece(7, 0).change_col_number(2)
                            # di chuyển xe
                            self.board[7][2] = self.board[7][0]
                            self.board[7][0] = Player.EMPTY

                            self.black_king_can_castle[0] = False
                            self.black_king_can_castle[1] = False
                        elif moved_to_piece == Player.EMPTY and next_square_col == 5 and self.king_can_castle_right(
                                moving_piece.get_player()):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.castling_move((7, 7), (7, 4), self)
                            self.move_log.append(move)

                            self.get_piece(0, 7).change_col_number(4)

                            # di chuyển xe
                            self.board[7][4] = self.board[7][7]
                            self.board[7][7] = Player.EMPTY

                            self.black_king_can_castle[0] = False
                            self.black_king_can_castle[2] = False
                        else:
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            self.move_log.append(move)
                            self.black_king_can_castle[0] = False
                        self._black_king_location = (next_square_row, next_square_col)
                elif moving_piece.get_name() == "r":
                    if moving_piece.is_player(Player.PLAYER_1) and current_square_col == 0:
                        self.white_king_can_castle[1] = False
                    elif moving_piece.is_player(Player.PLAYER_1) and current_square_col == 7:
                        self.white_king_can_castle[2] = False
                    elif moving_piece.is_player(Player.PLAYER_2) and current_square_col == 0:
                        self.white_king_can_castle[1] = False
                    elif moving_piece.is_player(Player.PLAYER_2) and current_square_col == 7:
                        self.white_king_can_castle[2] = False
                    self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                    self.can_en_passant_bool = False
                elif moving_piece.get_name() == "p":
                    # thăng tốt trắng
                    if moving_piece.is_player(Player.PLAYER_1) and next_square_row == 7:
                        if is_ai:
                            self.promote_pawn_ai(starting_square, moving_piece, ending_square)
                        else:
                            self.promote_pawn(starting_square, moving_piece, ending_square)
                        temp = False
                    # thăng tốt đen
                    elif moving_piece.is_player(Player.PLAYER_2) and next_square_row == 0:
                        if is_ai:
                            self.promote_pawn_ai(starting_square, moving_piece, ending_square)
                        else:
                            self.promote_pawn(starting_square, moving_piece, ending_square)
                        temp = False
                    # đi tốt 2 bước
                    elif abs(next_square_row - current_square_row) == 2 and current_square_col == next_square_col:
                        self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                        self._en_passant_previous = (next_square_row, next_square_col)
                    elif abs(next_square_row - current_square_row) == 1 and abs(
                            current_square_col - next_square_col) == 1 and \
                            self.can_en_passant(current_square_row, current_square_col):
                        if moving_piece.is_player(Player.PLAYER_1):
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.en_passant_move(self.board[next_square_row - 1][next_square_col],
                                                 (next_square_row - 1, next_square_col))
                            self.move_log.append(move)
                            self.board[next_square_row - 1][next_square_col] = Player.EMPTY
                        else:
                            move = chess_move(starting_square, ending_square, self, self._is_check)
                            move.en_passant_move(self.board[next_square_row + 1][next_square_col],
                                                 (next_square_row + 1, next_square_col))
                            self.move_log.append(move)
                            self.board[next_square_row + 1][next_square_col] = Player.EMPTY
                    # đi lên 1 hoặc ăn chéo
                    else:
                        self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                        self.can_en_passant_bool = False
                else:
                    self.move_log.append(chess_move(starting_square, ending_square, self, self._is_check))
                    self.can_en_passant_bool = False

                if temp:
                    moving_piece.change_row_number(next_square_row)
                    moving_piece.change_col_number(next_square_col)
                    self.board[next_square_row][next_square_col] = self.board[current_square_row][current_square_col]
                    self.board[current_square_row][current_square_col] = Player.EMPTY

                self.white_turn = not self.white_turn

            else:
                pass

    def undo_move(self):
        if self.move_log:
            undoing_move = self.move_log.pop()
            if undoing_move.castled == True:
                self.board[undoing_move.starting_square_row][
                    undoing_move.starting_square_col] = undoing_move.moving_piece
                self.board[undoing_move.ending_square_row][undoing_move.ending_square_col] = undoing_move.removed_piece
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_row_number(
                    undoing_move.starting_square_row)
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_col_number(
                    undoing_move.starting_square_col)

                self.board[undoing_move.rock_starting_square[0]][
                    undoing_move.rock_starting_square[1]] = undoing_move.moving_rock
                self.board[undoing_move.rock_ending_square[0]][undoing_move.rock_ending_square[1]] = Player.EMPTY
                undoing_move.moving_rock.change_row_number(undoing_move.rock_starting_square[0])
                undoing_move.moving_rock.change_col_number(undoing_move.rock_starting_square[1])
                if undoing_move.moving_piece is Player.PLAYER_1:
                    if undoing_move.rock_starting_square[1] == 0:
                        self.white_king_can_castle[0] = True
                        self.white_king_can_castle[1] = True
                    elif undoing_move.rock_starting_square[1] == 7:
                        self.white_king_can_castle[0] = True
                        self.white_king_can_castle[2] = True
                else:
                    if undoing_move.rock_starting_square[1] == 0:
                        self.black_king_can_castle[0] = True
                        self.black_king_can_castle[1] = True
                    elif undoing_move.rock_starting_square[1] == 7:
                        self.black_king_can_castle[0] = True
                        self.black_king_can_castle[2] = True
            elif undoing_move.pawn_promoted == True:
                self.board[undoing_move.starting_square_row][
                    undoing_move.starting_square_col] = undoing_move.moving_piece
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_row_number(
                    undoing_move.starting_square_row)
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_col_number(
                    undoing_move.starting_square_col)

                self.board[undoing_move.ending_square_row][undoing_move.ending_square_col] = undoing_move.removed_piece
                if undoing_move.removed_piece != Player.EMPTY:
                    self.get_piece(undoing_move.ending_square_row, undoing_move.ending_square_col).change_row_number(
                        undoing_move.ending_square_row)
                    self.get_piece(undoing_move.ending_square_row, undoing_move.ending_square_col).change_col_number(
                        undoing_move.ending_square_col)
            elif undoing_move.en_passaned == True:
                self.board[undoing_move.starting_square_row][
                    undoing_move.starting_square_col] = undoing_move.moving_piece
                self.board[undoing_move.ending_square_row][undoing_move.ending_square_col] = undoing_move.removed_piece
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_row_number(
                    undoing_move.starting_square_row)
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_col_number(
                    undoing_move.starting_square_col)

                self.board[undoing_move.en_passant_eaten_square[0]][
                    undoing_move.en_passant_eaten_square[1]] = undoing_move.en_passant_eaten_piece
                self.can_en_passant_bool = True
            else:
                self.board[undoing_move.starting_square_row][
                    undoing_move.starting_square_col] = undoing_move.moving_piece
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_row_number(
                    undoing_move.starting_square_row)
                self.get_piece(undoing_move.starting_square_row, undoing_move.starting_square_col).change_col_number(
                    undoing_move.starting_square_col)

                self.board[undoing_move.ending_square_row][undoing_move.ending_square_col] = undoing_move.removed_piece
                if undoing_move.removed_piece != Player.EMPTY:
                    self.get_piece(undoing_move.ending_square_row, undoing_move.ending_square_col).change_row_number(
                        undoing_move.ending_square_row)
                    self.get_piece(undoing_move.ending_square_row, undoing_move.ending_square_col).change_col_number(
                        undoing_move.ending_square_col)

            self.white_turn = not self.white_turn
          
            if undoing_move.moving_piece.get_name() == 'k' and undoing_move.moving_piece.get_player() == Player.PLAYER_1:
                self._white_king_location = (undoing_move.starting_square_row, undoing_move.starting_square_col)
            elif undoing_move.moving_piece.get_name() == 'k' and undoing_move.moving_piece.get_player() == Player.PLAYER_2:
                self._black_king_location = (undoing_move.starting_square_row, undoing_move.starting_square_col)

            return undoing_move
    # True nếu là quân trắng, False nếu là quân đen
    def whose_turn(self):
        return self.white_turn

    def check_for_check(self, king_location, player):
        _checks = []
        _pins = []
        _pins_check = []

        king_location_row = king_location[0]
        king_location_col = king_location[1]

        _up = 1
        _down = 1
        _left = 1
        _right = 1

        # trái quân vua
        _possible_pin = ()
        while king_location_col - _left >= 0 and self.get_piece(king_location_row,
                                                                king_location_col - _left) != None:
            if self.is_valid_piece(king_location_row, king_location_col - _left) and \
                    self.get_piece(king_location_row, king_location_col - _left).is_player(player) and \
                    self.get_piece(king_location_row, king_location_col - _left).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row, king_location_col - _left)
                else:
                    break
            elif self.is_valid_piece(king_location_row, king_location_col - _left) and \
                    not self.get_piece(king_location_row, king_location_col - _left).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row, king_location_col - _left))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        _checks.append((king_location_row, king_location_col - _left))
                break
            _left += 1

        # phải quân vua
        _possible_pin = ()
        while king_location_col + _right < 8 and self.get_piece(king_location_row,
                                                                king_location_col + _right) != None:
            if self.is_valid_piece(king_location_row, king_location_col + _right) and \
                    self.get_piece(king_location_row, king_location_col + _right).is_player(player) and \
                    self.get_piece(king_location_row, king_location_col + _right).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row, king_location_col + _right)
                else:
                    break
            elif self.is_valid_piece(king_location_row, king_location_col + _right) and \
                    not self.get_piece(king_location_row, king_location_col + _right).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row, king_location_col + _right))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
    
                        _checks.append((king_location_row, king_location_col + _right))
                break
            _right += 1

        # bên dưới vua
        _possible_pin = ()
        while king_location_row + _down < 8 and self.get_piece(king_location_row + _down,
                                                               king_location_col) != None:
            if self.is_valid_piece(king_location_row + _down, king_location_col) and \
                    self.get_piece(king_location_row + _down, king_location_col).is_player(player) and \
                    self.get_piece(king_location_row + _down, king_location_col).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row + _down, king_location_col)
                else:
                    break
            elif self.is_valid_piece(king_location_row + _down, king_location_col) and \
                    not self.get_piece(king_location_row + _down, king_location_col).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row + _down, king_location_col))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col).get_valid_piece_takes(
                        self):
                       
                        _checks.append((king_location_row + _down, king_location_col))
                break
            _down += 1

        # bên trên quân vua
        _possible_pin = ()
        while king_location_row - _up >= 0 and self.get_piece(king_location_row - _up, king_location_col) != None:
            if self.is_valid_piece(king_location_row - _up, king_location_col) and \
                    self.get_piece(king_location_row - _up, king_location_col).is_player(player) and \
                    self.get_piece(king_location_row - _up, king_location_col).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row - _up, king_location_col)
                else:
                    break
            elif self.is_valid_piece(king_location_row - _up, king_location_col) and \
                    not self.get_piece(king_location_row - _up, king_location_col).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row - _up, king_location_col))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col).get_valid_piece_takes(
                            self):
                    
                        _checks.append((king_location_row - _up, king_location_col))
                break
            _up += 1

        # di chuyển sang trái
        _up = 1
        _left = 1
        _possible_pin = ()
        while king_location_col - _left >= 0 and king_location_row - _up >= 0 and \
                self.get_piece(king_location_row - _up, king_location_col - _left) != None:
            if self.is_valid_piece(king_location_row - _up, king_location_col - _left) and \
                    self.get_piece(king_location_row - _up, king_location_col - _left).is_player(player) and \
                    self.get_piece(king_location_row - _up, king_location_col - _left).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row - _up, king_location_col - _left)
                else:
                    break
            elif self.is_valid_piece(king_location_row - _up, king_location_col - _left) and \
                    not self.get_piece(king_location_row - _up, king_location_col - _left).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row - _up, king_location_col - _left))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col - _left).get_valid_piece_takes(
                        self):
                        _checks.append((king_location_row - _up, king_location_col - _left))
                break
            _left += 1
            _up += 1

        # di chuyển sang phải
        _up = 1
        _right = 1
        _possible_pin = ()
        while king_location_col + _right < 8 and king_location_row - _up >= 0 and \
                self.get_piece(king_location_row - _up, king_location_col + _right) != None:
            if self.is_valid_piece(king_location_row - _up, king_location_col + _right) and \
                    self.get_piece(king_location_row - _up, king_location_col + _right).is_player(player) and \
                    self.get_piece(king_location_row - _up, king_location_col + _right).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row - _up, king_location_col + _right)
                else:
                    break
            elif self.is_valid_piece(king_location_row - _up, king_location_col + _right) and \
                    not self.get_piece(king_location_row - _up, king_location_col + _right).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row - _up, king_location_col + _right))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row - _up,
                                                                                king_location_col + _right).get_valid_piece_takes(
                        self):
                        _checks.append((king_location_row - _up, king_location_col + _right))
                break
            _right += 1
            _up += 1

        # di chuyển dưới
        _down = 1
        _left = 1
        _possible_pin = ()
        while king_location_col - _left >= 0 and king_location_row + _down < 8 and \
                self.get_piece(king_location_row + _down, king_location_col - _left) != None:
            if self.is_valid_piece(king_location_row + _down, king_location_col - _left) and \
                    self.get_piece(king_location_row + _down, king_location_col - _left).is_player(player) and \
                    self.get_piece(king_location_row + _down, king_location_col - _left).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row + _down, king_location_col - _left)
                else:
                    break
            elif self.is_valid_piece(king_location_row + _down, king_location_col - _left) and \
                    not self.get_piece(king_location_row + _down, king_location_col - _left).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col - _left).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row + _down, king_location_col - _left))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col - _left).get_valid_piece_takes(
                        self):
                        _checks.append((king_location_row + _down, king_location_col - _left))
                break
            _left += 1
            _down += 1

        # chéo phải dưới
        _down = 1
        _right = 1
        _possible_pin = ()
        while king_location_col + _right < 8 and king_location_row + _down < 8 and \
                self.get_piece(king_location_row + _down, king_location_col + _right) != None:
            if self.is_valid_piece(king_location_row + _down, king_location_col + _right) and \
                    self.get_piece(king_location_row + _down, king_location_col + _right).is_player(player) and \
                    self.get_piece(king_location_row + _down, king_location_col + _right).get_name() != "k":
                if not _possible_pin:
                    _possible_pin = (king_location_row + _down, king_location_col + _right)
                else:
                    break
            elif self.is_valid_piece(king_location_row + _down, king_location_col + _right) and \
                    not self.get_piece(king_location_row + _down, king_location_col + _right).is_player(player):
                if _possible_pin:
                    temp = self.board[_possible_pin[0]][_possible_pin[1]]
                    self.board[_possible_pin[0]][_possible_pin[1]] = Player.EMPTY
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col + _right).get_valid_piece_takes(
                            self):
                        _pins.append(_possible_pin)
                        _pins_check.append((king_location_row + _down, king_location_col + _right))
                    self.board[_possible_pin[0]][_possible_pin[1]] = temp
                else:
                    if (king_location_row, king_location_col) in self.get_piece(king_location_row + _down,
                                                                                king_location_col + _right).get_valid_piece_takes(
                        self):
                        # self._is_check = True
                        _checks.append((king_location_row + _down, king_location_col + _right))
                break
            _right += 1
            _down += 1

        # mã
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]
        for i in range(0, 8):
            if self.is_valid_piece(king_location_row + row_change[i], king_location_col + col_change[i]) and \
                    not self.get_piece(king_location_row + row_change[i], king_location_col + col_change[i]).is_player(
                        player):
                if (king_location_row, king_location_col) in self.get_piece(king_location_row + row_change[i],
                                                                            king_location_col + col_change[
                                                                                i]).get_valid_piece_takes(self):
                    _checks.append((king_location_row + row_change[i], king_location_col + col_change[i]))
        return [_checks, _pins, _pins_check]


class chess_move():
    def __init__(self, starting_square, ending_square, chess_state, in_check):
        self.starting_square_row = starting_square[0]
        self.starting_square_col = starting_square[1]
        self.moving_piece = chess_state.get_piece(self.starting_square_row, self.starting_square_col)
        self.in_check = in_check

        self.ending_square_row = ending_square[0]
        self.ending_square_col = ending_square[1]
        if chess_state.is_valid_piece(self.ending_square_row, self.ending_square_col):
            self.removed_piece = chess_state.get_piece(self.ending_square_row, self.ending_square_col)
        else:
            self.removed_piece = Player.EMPTY

        self.castled = False
        self.rock_starting_square = None
        self.rock_ending_square = None
        self.moving_rock = None

        self.pawn_promoted = False
        self.replacement_piece = None

        self.en_passaned = False
        self.en_passant_eaten_piece = None
        self.en_passant_eaten_square = None

    def castling_move(self, rock_starting_square, rock_ending_square, chess_state):
        self.castled = True
        self.rock_starting_square = rock_starting_square
        self.rock_ending_square = rock_ending_square
        self.moving_rock = chess_state.get_piece(rock_starting_square[0], rock_starting_square[1])

    def pawn_promotion_move(self, new_piece):
        self.pawn_promoted = True
        self.replacement_piece = new_piece

    def en_passant_move(self, eaten_piece, eaten_piece_square):
        self.en_passaned = True
        self.en_passant_eaten_piece = eaten_piece
        self.en_passant_eaten_square = eaten_piece_square

    def get_moving_piece(self):
        return self.moving_piece
