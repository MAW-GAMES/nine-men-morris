import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 128)
RED = (255, 0, 0)
DARK_RED = (139, 0, 0)
GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Moulin (Nine Men's Morris)")

# Font for text
font = pygame.font.Font(None, 40)

# Board positions
POSITIONS = [
    (100, 100), (300, 100), (500, 100),  # Top row
    (100, 300), (300, 300), (500, 300),  # Middle row
    (100, 500), (300, 500), (500, 500),  # Bottom row
    (200, 200), (400, 200),  # Inner square top
    (200, 400), (400, 400),  # Inner square bottom
    (300, 200), (300, 400)   # Inner square vertical middle
]

# Board lines (connections between positions)
LINES = [
    ((100, 100), (300, 100)), ((300, 100), (500, 100)),  # Top row
    ((100, 300), (300, 300)), ((300, 300), (500, 300)),  # Middle row
    ((100, 500), (300, 500)), ((300, 500), (500, 500)),  # Bottom row
    ((100, 100), (100, 300)), ((100, 300), (100, 500)),  # Left column
    ((300, 100), (300, 300)), ((300, 300), (300, 500)),  # Middle column
    ((500, 100), (500, 300)), ((500, 300), (500, 500)),  # Right column
    ((200, 200), (400, 200)), ((200, 200), (200, 400)),  # Inner square
    ((400, 200), (400, 400)), ((200, 400), (400, 400))
]

# Player pieces
player_turn = 1
player1_pieces = []
player2_pieces = []

# Draw the board
def draw_board():
    # Fill the background
    screen.fill(GREY)
    
    # Draw lines
    for line in LINES:
        pygame.draw.line(screen, DARK_GREY, line[0], line[1], 5)
    
    # Draw positions
    for pos in POSITIONS:
        pygame.draw.circle(screen, DARK_GREY, pos, 12)  # Outer border
        pygame.draw.circle(screen, WHITE, pos, 8)      # Inner fill
    
    # Draw pieces
    for piece in player1_pieces:
        pygame.draw.circle(screen, DARK_BLUE, piece, 15)  # Outer shadow
        pygame.draw.circle(screen, BLUE, piece, 12)       # Inner fill
    for piece in player2_pieces:
        pygame.draw.circle(screen, DARK_RED, piece, 15)   # Outer shadow
        pygame.draw.circle(screen, RED, piece, 12)        # Inner fill

    # Display turn
    turn_text = font.render(f"Player {player_turn}'s Turn", True, BLACK, WHITE)
    text_rect = turn_text.get_rect(center=(WIDTH // 2, 30))
    screen.blit(turn_text, text_rect)

# Check if a click is near a position
def get_nearest_position(pos):
    for p in POSITIONS:
        if (pos[0] - p[0]) ** 2 + (pos[1] - p[1]) ** 2 <= 20 ** 2:
            return p
    return None

# Main game loop
def main():
    global player_turn

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                nearest_pos = get_nearest_position(click_pos)
                if nearest_pos and nearest_pos not in player1_pieces and nearest_pos not in player2_pieces:
                    if player_turn == 1:
                        player1_pieces.append(nearest_pos)
                        player_turn = 2
                    else:
                        player2_pieces.append(nearest_pos)
                        player_turn = 1

        draw_board()
        pygame.display.flip()

if __name__ == "__main__":
    main()