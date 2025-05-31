import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('Arial', 28)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("What is this? Choose the correct English word!")

# Load images and labels
items = [
    {"file": "bird.jpg", "label": "bird"},
    {"file": "dog.jpg", "label": "dog"},
    {"file": "pen.jpg", "label": "pen"},
    {"file": "apple.png", "label": "apple"},
    {"file": "car.jpeg", "label": "car"},
    {"file": "bike.jpg", "label": "bike"},
    {"file": "cat.jpg", "label": "cat"},
    {"file": "chair.jpeg", "label": "chair"},
    {"file": "lion.jpg", "label": "lion"},
    {"file": "computer.jpg", "label": "computer"},
    {"file": "sea.png", "label": "sea"},
    {"file": "moon.jpg", "label": "moon"},
    {"file": "tiger.jpg", "label": "tiger"},
    {"file": "sun.jpeg", "label": "sun"},
    {"file": "banana.jpeg", "label": "banana"},
    {"file": "elephant.jpg", "label": "elephant"}
]

def load_image(file):
    """Load an image file and resize it to a fixed size."""
    img = pygame.image.load(file)
    return pygame.transform.scale(img, (300, 300))

def prepare_items():
    """Load and prepare all item images for display."""
    for item in items:
        item["image"] = load_image(item["file"])

def display_message(text):
    """Display a message at the center of the screen briefly."""
    screen.fill(WHITE)
    message = FONT.render(text, True, BLACK)
    screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    pygame.time.delay(600)  # Shorter delay

def display_question(current_item, options, score):
    """Display the current image and multiple choice options."""
    screen.fill(WHITE)
    screen.blit(current_item["image"], (250, 50))

    instruction = FONT.render("Choose the correct word for the image:", True, BLACK)
    screen.blit(instruction, (100, 350))

    for i, opt in enumerate(options):
        label = FONT.render(f"{i + 1}. {opt['label']}", True, BLACK)
        screen.blit(label, (100, 400 + i * 40))

    score_label = FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_label, (600, 20))
    pygame.display.flip()

def display_end_screen(score):
    """Display the end screen with the final score and restart options."""
    screen.fill(WHITE)
    end_message = FONT.render(f"Game over! Your score: {score}/{len(items)}", True, BLACK)
    screen.blit(end_message, (200, 250))
    continue_msg = FONT.render("Press any key to restart or ESC to quit.", True, BLACK)
    screen.blit(continue_msg, (180, 300))
    pygame.display.flip()

def run_game():
    """Main loop to run the game logic."""
    score = 0
    used_items = items[:]
    random.shuffle(used_items)
    current_index = 0

    while current_index < len(used_items):
        current_item = used_items[current_index]

        # Generate options
        options = random.sample(items, 3)
        if current_item not in options:
            options[random.randint(0, 2)] = current_item
        random.shuffle(options)

        waiting_for_input = True
        while waiting_for_input:
            display_question(current_item, options, score)

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif events.type == pygame.KEYDOWN:
                    if pygame.K_1 <= events.key <= pygame.K_3:
                        selected = events.key - pygame.K_1
                        if options[selected] == current_item:
                            score += 1
                            display_message("Correct!")
                        else:
                            display_message(f"Wrong! Correct answer: {current_item['label']}")
                        waiting_for_input = False

        current_index += 1

    display_end_screen(score)

    # Wait for user to restart or quit
    waiting_for_restart = True
    while waiting_for_restart:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    run_game()
                    return

# Prepare game data
prepare_items()

# Run the game
run_game()

