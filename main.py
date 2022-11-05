### main.py

import pygame
<<<<<<< HEAD
pygame.init()

def main():
    screen = pygame.display.set_mode([500, 500])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        

        pygame.draw.circle(screen, (0, 0,  255), (250, 250), 75)
    
    pygame.quit()


if __name__ == '__main__':
    main()
=======
>>>>>>> 5cb968d8c3abfbada15c9d6a4cbbc4439733f73f

