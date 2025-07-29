import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Text Input')

# Set up fonts
font = pygame.font.Font(None, 32)
text = ''
lines = []

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if text:  # If there's text in the current line
                    text = text[:-1]  # Remove the last character from the current line
                elif lines:  # If there are lines already typed
                    text = lines.pop()  # Remove the last line and continue typing from it
            elif event.key == pygame.K_RETURN:
                print("Typed text:", text)
                lines.append(text)
                text = ''
            else:
                text += event.unicode

    # Clear the screen
    window.fill((255, 255, 255))

    # Render the text
    y_offset = 10
    for line in lines:
        input_surface = font.render(line, True, (0, 0, 0))
        window.blit(input_surface, (10, y_offset))
        y_offset += font.get_height()  # Adjusting y offset by font height

    # Render the current line being typed
    input_surface = font.render(text, True, (0, 0, 0))
    text_width = input_surface.get_width()
    if text_width > WINDOW_WIDTH - 20:
        lines.append(text)
        text = ''
        y_offset += font.get_height()  # Move to the next line
    window.blit(input_surface, (10, y_offset))

    # Update the display
    pygame.display.flip()
