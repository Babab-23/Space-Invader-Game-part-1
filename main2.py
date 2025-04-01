import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Colors
WHITE = (255, 255, 255)

# Load player and enemy images
player_image = pygame.Surface((50, 50))
player_image.fill((0, 255, 0))  # Green square

enemy_image = pygame.Surface((50, 50))
enemy_image.fill((255, 0, 0))  # Red square

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, x_change=0, y_change=0):
        self.rect.x += x_change
        self.rect.y += y_change

# Create player sprite
player = Sprite(WIDTH // 2, HEIGHT // 2, player_image)

# Create enemy sprites
enemies = pygame.sprite.Group()
for _ in range(7):
    x, y = random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)
    enemy = Sprite(x, y, enemy_image)
    enemies.add(enemy)

# Group all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)

# Game loop
running = True
score = 0
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key states
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    
    # Update player position
    player.update(x_change, y_change)
    
    # Check for collisions
    collisions = pygame.sprite.spritecollide(player, enemies, True)
    score += len(collisions)  # Increase score per collision
    
    # Redraw everything
    all_sprites.draw(screen)
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
