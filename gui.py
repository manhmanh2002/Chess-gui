import sys
from button import Button
import chess_engine
import pygame 
import ai_engine
from enums import Player

WIDTH = 1280 
HEIGHT = 720  # chiều rộng và chiều cao của bàn cờ
DIMENSION = 8 # kích thước của bàn cờ vua
SQ_SIZE = HEIGHT // DIMENSION  # kích thước của mỗi ô vuông trong bảng
MAX_FPS = 60  # khung hình
IMAGES = {}  # ảnh cho mỗi quân cờ
colors = [pygame.Color("white"), pygame.Color("gray")]
pygame.init()
black = "b"
white = "w"

def get_font(size): # Trả về Press-Start-2P ở kích thước mong muốn

    return pygame.font.Font("assets/font.ttf", size)
def load_images():
    '''
    Tải hình ảnh bàn cờ
    '''
    for p in Player.PIECES:
        IMAGES[p] = pygame.transform.scale(pygame.image.load("images/" + p + ".png"), (SQ_SIZE, SQ_SIZE))

def draw_chess_state(screen, chess_state, valid_moves, square_selected):
    ''' 
    vẽ hoàn chỉnh bàn cờ với các quân cờ
    '''
    draw_squares(screen)
    highlight_square(screen, chess_state, valid_moves, square_selected)
    draw_pieces(screen, chess_state)

def draw_squares(screen):
    ''' 
    vẽ bàn cờ với 2 màu đen trắng
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, chess_state):
    ''' 
    vẽ các quân cờ lên bàn cờ
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = chess_state.get_piece(r, c)
            if piece is not None and piece != Player.EMPTY:
                screen.blit(IMAGES[piece.get_player() + "_" + piece.get_name()],
                            pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def highlight_square(screen, chess_state, valid_moves, square_selected):
    if square_selected != () and chess_state.is_valid_piece(square_selected[0], square_selected[1]):
        row = square_selected[0]
        col = square_selected[1]

        if (chess_state.whose_turn() and chess_state.get_piece(row, col).is_player(Player.PLAYER_1)) or \
                (not chess_state.whose_turn() and chess_state.get_piece(row, col).is_player(Player.PLAYER_2)):
            # bôi đậm ô vuông được chọn
            s = pygame.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(pygame.Color("blue"))
            screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))

            # bôi đậm ô vuông có thể di chuyển
            s.fill(pygame.Color("green"))

            for move in valid_moves:
                screen.blit(s, (move[1] * SQ_SIZE, move[0] * SQ_SIZE))

def main():
    #màn hình menu game
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")
    BG = pygame.image.load("assets/Background.png")
    icon = pygame.image.load("assets/icon.jfif")
    pygame.display.set_icon(icon)
    while(True):
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("CHESS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        COMPUTER_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 250), 
                            text_input="COMPUTER", font=get_font(40), base_color="#d7fcd4", hovering_color="White") #computer mode
        PVP_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 400), 
                            text_input="PVP", font=get_font(40), base_color="#d7fcd4", hovering_color="White")  #pvp mode
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(40), base_color="#d7fcd4", hovering_color="White") #quit window
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
    chess_state = chess_engine.chess_state()
    load_images()
    running = True
    square_selected = ()  # theo dõi hình vuông được chọn cuối cùng
    player_clicks = []  # theo dõi các lần nhấp của người chơi (hai người)
    valid_moves = []
    game_over = False
    BG = pygame.image.load("assets/Background.png")
    while running:
        MOUSE_POS = pygame.mouse.get_pos()
        UNDO_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(1000, 250), 
                    text_input="UNDO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        RESTART_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(1000, 400), 
                    text_input="RESTART", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(1000, 550), 
                    text_input="BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        for button in [UNDO_BUTTON, RESTART_BUTTON, BACK_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(MOUSE_POS):
                    game_over = False
                    chess_state = chess_engine.chess_state()
                    valid_moves = []
                    square_selected = ()
                    player_clicks = []
                    valid_moves = []
                elif UNDO_BUTTON.checkForInput(MOUSE_POS):
                    chess_state.undo_move()
                elif BACK_BUTTON.checkForInput(MOUSE_POS):
                    main()
                pygame.display.update() 
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                        if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                        else:
                            chess_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                  (player_clicks[1][0], player_clicks[1][1]), False)
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                    else:
                        valid_moves = chess_state.get_valid_moves((row, col))
                        if valid_moves == None:
                            valid_moves = [] 
          
        draw_chess_state(SCREEN, chess_state, valid_moves, square_selected)
        endgame = chess_state.checkmate_stalemate_checker()
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
        BLACK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 250), 
                            text_input="BLACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        WHITE_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 400), 
                            text_input="WHITE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [BLACK_BUTTON, WHITE_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
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

def Computer_mode(mode):
    human_player = ""
    while True:
        human_player = mode
        if human_player == "w" or human_player == "b":
            break
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    chess_state = chess_engine.chess_state()
    load_images()
    running = True
    square_selected = ()  # theo dõi hình vuông được chọn cuối cùng
    player_clicks = []  # theo dõi các lần nhấp của người chơi (hai bộ)
    valid_moves = []
    game_over = False
    BG = pygame.image.load("assets/Background.png")
    ai = ai_engine.chess_ai()
    chess_state = chess_engine.chess_state()
    if human_player == 'b':
        ai_move = ai.minimax_black(chess_state, 3, -100000, 100000, True, Player.PLAYER_1)
        chess_state.move_piece(ai_move[0], ai_move[1], True)

    while running:
        MOUSE_POS = pygame.mouse.get_pos()
        UNDO_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(1000, 250), 
                            text_input="UNDO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        RESTART_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(1000, 400), 
                            text_input="RESTART", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(1000, 550), 
                    text_input="BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        for button in [UNDO_BUTTON, RESTART_BUTTON,BACK_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(MOUSE_POS):
                    Computer_menu()
                elif UNDO_BUTTON.checkForInput(MOUSE_POS):
                    chess_state.undo_move()
                elif BACK_BUTTON.checkForInput(MOUSE_POS):
                    main()
                pygame.display.update()  
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                        if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []
                        else:
                            chess_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
                                                  (player_clicks[1][0], player_clicks[1][1]), False)
                            square_selected = ()
                            player_clicks = []
                            valid_moves = []

                            if human_player == 'w':
                                ai_move = ai.minimax_white(chess_state, 3, -100000, 100000, True, Player.PLAYER_2)
                                chess_state.move_piece(ai_move[0], ai_move[1], True)
                            elif human_player == 'b':
                                ai_move = ai.minimax_black(chess_state, 3, -100000, 100000, True, Player.PLAYER_1)
                                chess_state.move_piece(ai_move[0], ai_move[1], True)
                    else:
                        valid_moves = chess_state.get_valid_moves((row, col))
                        if valid_moves == None:
                            valid_moves = []
        draw_chess_state(SCREEN, chess_state, valid_moves, square_selected)
        endgame = chess_state.checkmate_stalemate_checker()
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