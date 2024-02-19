import math

import pygame


class Enemy:
    def __init__(self, x, y, width, height, screen_width, screen_height, player, all_enemies):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 2
        self.player = player
        self.all_enemies = all_enemies

        self.enemy_img = pygame.image.load('enemy.png').convert()  # Lade das Bild
        self.enemy_img = pygame.transform.scale(self.enemy_img, (80, 80))


    def move_towards_player(self):
        angle = math.atan2(self.player.y - self.y, self.player.x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

    def draw(self, window):
        window.blit(self.enemy_img, (self.x, self.y))

       # pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def check_collision_with_other_enemies(self):
        for other_enemy in self.all_enemies:
            if other_enemy != self:
                if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                        other_enemy.x, other_enemy.y, other_enemy.width, other_enemy.height):
                    return True
        return False