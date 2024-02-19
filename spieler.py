import pygame


class Player:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5

        self.player_img = pygame.image.load("player.png")  # Lade das Bild
        self.player_img = pygame.transform.scale(self.player_img, (80, 80))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.screen_width - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < self.screen_height - self.height:
            self.y += self.speed

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))
        # Zeichne das Bild auf das Fenster an der Position (x, y)




        #rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))
        #player_img = pygame.image.load("player.png").convert()
       # player_img = pygame.transform.scale(player_img, (30, 50))
    def check_collision(self, other):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(other.x, other.y, other.width, other.height)
