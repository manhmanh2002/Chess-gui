import sys
from button import Button
import chess_engine
import pygame 
import pygame_gui as py_gui
import ai_engine
from enums import Player

# GOBAL VARIABLES
WIDTH = 1280 
HEIGHT = 720  # width and height of the chess board
DIMENSION = 8  # the dimensions of the chess board
SQ_SIZE = HEIGHT // DIMENSION  # the size of each of the squares in the board
MAX_FPS = 60  # FPS for animations
IMAGES = {}  # images for the chess pieces
colors = [pygame.Color("white"), pygame.Color("gray")]
pygame.init()
black = "b"
white = "w"

def get_font(size): # Returns Press-Start-2P in the desired size

    return pygame.font.Font("assets/font.ttf", size)
def load_images():
    '''
    Load images for the chess pieces
    '''
    for p in Player.PIECES:
        IMAGES[p] = pygame.transform.scale(pygame.image.load("images/" + p + ".png"), (SQ_SIZE, SQ_SIZE))

def draw_game_state(screen, game_state, valid_moves, square_selected):
    ''' Draw the complete chess board with pieces

    Keyword arguments:
        :param screen       -- the pygame screen
        :param game_state   -- the state of the current chess game
    '''
    draw_squares(screen)
    highlight_square(screen, game_state, valid_moves, square_selected)
    draw_pieces(screen, game_state)

def draw_squares(screen):
    ''' Draw the chess board with the alternating two colors

    :param screen:          -- the pygame screen
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, game_state):
    ''' Draw the chess pieces onto the board

    :param screen:          -- the pygame screen
    :param game_state:      -- the current state of the chess game
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = game_state.get_piece(r, c)
            if piece is not None and piece != Player.EMPTY:
                screen.blit(IMAGES[piece.get_player() + "_" + piece.get_name()],
                            pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def highlight_square(screen, game_state, valid_moves, square_selected):
    if square_selected != () and game_state.is_valid_piece(square_selected[0], square_selected[1]):
        row = square_selected[0]
        col = square_selected[1]

        if (game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_1)) or \
                (not game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_2)):
            # hightlight selected square
            s = pygame.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(pygame.Color("blue"))
            screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))

            # highlight move squares
            s.fill(pygame.Color("green"))

            for move in valid_moves:
                screen.blit(s, (move[1] * SQ_SIZE, move[0] * SQ_SIZE))

def main():

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Duy đầu buồi")
    BG = pygame.image.load("assets/Background.png")
    icon = pygame.image.load("assets/icon.jfif")
    pygame.display.set_icon(icon)
    while(True):
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("CHESS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        COMPUTER_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 250), 
                            text_input="COMPUTER", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        PVP_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 400), 
                            text_input="PVP", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [QUIT_BUTTON, COMPUTER_BUTTON, PVP_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if PVP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Pvp_mode()
                if COMPUTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Computer_menu()
        pygame.display.update()

def Pvp_mode():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_state = chess_engine.game_state()
    load_images()
    running = True
    square_selected = ()  # keeps track of the last selected square
    player_clicks = []  # keeps track of player clicks (two tuples)
    valid_moves = []
    game_over = False
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    location = pygame.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if square_selected == (row, col):
                        square_selected = ()
                        player_clicks = []
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)
                    if len(player_clicks) == 2:
                        # this if is useless right now
                        if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                        else:
                            game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                  (player_clicks[1][0], player_clicks[1][1]), False)
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                    else:
                        valid_moves = game_state.get_valid_moves((row, col))
                        if valid_moves == None:
                            valid_moves = []
            #elif e.type == pygame.MOUSEBUTTONDOWN:
            #     if e.ui_element == button_layout_rect:
            #        game_over = False
            #        game_state = chess_engine.game_state()
            #        valid_moves = []
            #        square_selected = ()
            #        player_clicks = []
            #        valid_moves = []
            #    #elif e.key == pygame.K_u:
            #    #    game_state.undo_move()
            #    #    print(len(game_state.move_log))
        draw_game_state(SCREEN, game_state, valid_moves, square_selected)
        endgame = game_state.checkmate_stalemate_checker()
        if endgame == 0:
            game_over = True
            draw_text(SCREEN, "Black wins.")
        elif endgame == 1:
            game_over = True
            draw_text(SCREEN, "White wins.")
        elif endgame == 2:
            game_over = True
            draw_text(SCREEN, "Stalemate.")
        clock.tick(MAX_FPS)
        pygame.display.flip()

def Computer_menu():
    SCREEN2 = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Duy đầu buồi")
    BG = pygame.image.load("assets/Background.png")
    icon = pygame.image.load("assets/icon.jfif")
    pygame.display.set_icon(icon)
    while(True):
        SCREEN2.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("CHESS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        BLACK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 250), 
                            text_input="BLACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        WHITE_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 400), 
                            text_input="WHITE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        SCREEN2.blit(MENU_TEXT, MENU_RECT)
        for button in [BLACK_BUTTON, WHITE_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main()
                if BLACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Computer_mode(black)
                if WHITE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Computer_mode(white)
        pygame.display.update()
    

    pygame.display.update()

def Computer_mode(mode):
    human_player = ""
    while True:
        human_player = mode
        if human_player == "w" or human_player == "b":
            break
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_state = chess_engine.game_state()
    load_images()
    running = True
    square_selected = ()  # keeps track of the last selected square
    player_clicks = []  # keeps track of player clicks (two tuples)
    valid_moves = []
    game_over = False

    ai = ai_engine.chess_ai()
    game_state = chess_engine.game_state()
    if human_player == 'b':
        ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
        game_state.move_piece(ai_move[0], ai_move[1], True)

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    location = pygame.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    if square_selected == (row, col):
                        square_selected = ()
                        player_clicks = []
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)
                    if len(player_clicks) == 2:
                        # this if is useless right now
                        if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                        else:
                            game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                  (player_clicks[1][0], player_clicks[1][1]), False)
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []

                            if human_player == 'w':
                                ai_move = ai.minimax_white(game_state, 3, -100000, 100000, True, Player.PLAYER_2)
                                game_state.move_piece(ai_move[0], ai_move[1], True)
                            elif human_player == 'b':
                                ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
                                game_state.move_piece(ai_move[0], ai_move[1], True)
                    else:
                        valid_moves = game_state.get_valid_moves((row, col))
                        if valid_moves == None:
                            valid_moves = []
            #elif e.type == pygame.MOUSEBUTTONDOWN:
            #    if e.ui_element == button_layout_rect:
            #        game_over = False
            #        game_state = chess_engine.game_state()
            #        valid_moves = []
            #        square_selected = ()
            #        player_clicks = []
            #        valid_moves = []
            #    #elif e.key == py.K_u:
            #    #    game_state.undo_move()
            #    #    print(len(game_state.move_log))
        draw_game_state(SCREEN, game_state, valid_moves, square_selected)

        endgame = game_state.checkmate_stalemate_checker()
        if endgame == 0:
            game_over = True
            draw_text(SCREEN, "Black wins.")
        elif endgame == 1:
            game_over = True
            draw_text(SCREEN, "White wins.")
        elif endgame == 2:
            game_over = True
            draw_text(SCREEN, "Stalemate.")
        clock.tick(MAX_FPS)
        pygame.display.flip()
    
def draw_text(screen, text):
    font = pygame.font.Font("assets/font.ttf", 32)
    text_object = font.render(text, False, pygame.Color("Black"))
    text_location = pygame.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2,
                                                      HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)


if __name__ == "__main__":
    main()