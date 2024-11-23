import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Musical Notes Game")

black = (0, 0, 0)
white = (255, 255, 255)
blue = (173, 216, 230)
font = pygame.font.Font(pygame.font.match_font('comicsansms'), 74)
title_font = pygame.font.Font(pygame.font.match_font('comicsansms'), 50)
button_font = pygame.font.Font(None, 36)

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def generate_sequence():
    sequence_length = random.randint(5, 10)
    return [random.choice(notes) for _ in range(sequence_length)]

note_sequence = generate_sequence()

def display_welcome_screen():
    screen.fill(blue)
    welcome_text = title_font.render("Benvenuto! :)", True, black)
    screen.blit(welcome_text, (width // 2 - welcome_text.get_width() // 2, height // 2 - 100))

    button_text = button_font.render("Inizia a suonare!", True, white)
    button_rect = pygame.Rect(width // 2 - 100, height // 2, 200, 50)
    pygame.draw.rect(screen, black, button_rect)
    screen.blit(button_text, (width // 2 - button_text.get_width() // 2, height // 2 + 10))
    pygame.display.flip()
    return button_rect

def display_sequence():
    screen.fill(blue)
    title_text = title_font.render("Generatore di note", True, black)
    screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 20))

    y_offset = 100
    for note in note_sequence:
        note_text = font.render(note, True, black)
        screen.blit(note_text, (width // 2 - note_text.get_width() // 2, y_offset))
        y_offset += 80
    pygame.display.flip()

def main():
    global note_sequence
    running = True
    welcome_screen = True
    while running:
        if welcome_screen:
            button_rect = display_welcome_screen()
        else:
            display_sequence()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and welcome_screen:
                if button_rect.collidepoint(event.pos):
                    welcome_screen = False
            elif event.type == pygame.KEYDOWN and not welcome_screen:
                if event.key == pygame.K_r:
                    note_sequence = generate_sequence()
                elif event.key == pygame.K_q:
                    running = False
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
