import pygame
pygame.init()

WIDTH, HEIGHT = 800, 700
WIN = pygame.display.set_mode([WIDTH, HEIGHT])
user_text = ""
correct = "PENIS"
guesses = [user_text]
current_line = 0
first = True

def draw_win():
    global guesses
    WIN.fill((240, 240, 240))
    FONT = pygame.font.SysFont("Times New Roman", 60, True)
    main_text = FONT.render("WORDLE", True, (0, 0, 0))
    main_text_rect = main_text.get_rect()
    main_text_rect.center = (WIDTH//2, 50)
    color = (200, 200, 200)

    for i in range(1, 6):
        for j in range(1, 7):
            square = pygame.Rect(50 + 100 * i, 100 * j, 75, 75)
            pygame.draw.rect(WIN, (200, 200, 200), square)
    for i, word in enumerate(guesses):
        if i + 1 == current_line and not first or i == current_line and first:
            for j, letter in enumerate(user_text):
                letter_t = FONT.render(letter, True, (0, 0, 0))
                letter_rect = letter_t.get_rect()
                if first:
                    letter_rect.center = (185 + 100 * j, 135 + 100 * i)
                else:
                    letter_rect.center = (185 + 100 * j, 135 + 100 * (i + 1))
                WIN.blit(letter_t, letter_rect)
        for j, letter in enumerate(word):
            if letter == correct[j]:
                color = (0, 200, 0)
            elif letter in correct:
                color = (240, 230, 140)
            else:
                color = (200, 200, 200)
            letter_t = FONT.render(letter, True, (0, 0, 0))
            letter_rect = letter_t.get_rect()
            letter_rect.center = (185 + 100 * j, 135 + 100 * i)
            pygame.draw.rect(WIN, color, pygame.Rect(50 + 100 * (j + 1), 100 * (i + 1), 75, 75))
            
            WIN.blit(letter_t, letter_rect)

    
    WIN.blit(main_text, main_text_rect)
    pygame.display.update()

def main():
    global user_text, current_line, guesses, first

    FPS = 60
    pygame.display.set_caption("Wordle")

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        draw_win()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN and len(user_text) < 5:
                    user_text += event.unicode.upper()
                elif event.key == pygame.K_RETURN and len(user_text) == 5:
                    if first:
                        guesses = [user_text]
                        first = False
                    else:
                        guesses.append(user_text)
                    current_line += 1
                    user_text = ""

    pygame.quit()

if __name__ == "__main__":
    main()