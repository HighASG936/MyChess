import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Draggable Sprites")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Create a sprite class
class DraggableSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, initial_position):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()

# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create draggable sprites and add them to the group
sprite1 = DraggableSprite(blue, 50, 50, (100, 100))
sprite2 = DraggableSprite(blue, 50, 50, (200, 200))
all_sprites.add(sprite1, sprite2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in all_sprites:
                if sprite.rect.collidepoint(event.pos):
                    sprite.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for sprite in all_sprites:
                sprite.dragging = False

    all_sprites.update()

    # Clear the screen
    screen.fill(white)

    # Draw sprites
    all_sprites.draw(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
