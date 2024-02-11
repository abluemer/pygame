import pygame
import sys
import random
import math

class Player:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5

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
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def check_collision(self, other):
        return pygame.Rect(self.x, self.y, self.width, self.height).colliderect(other.x, other.y, other.width, other.height)

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

    def move_towards_player(self):
        angle = math.atan2(self.player.y - self.y, self.player.x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def check_collision_with_other_enemies(self):
        for other_enemy in self.all_enemies:
            if other_enemy != self:
                if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                        other_enemy.x, other_enemy.y, other_enemy.width, other_enemy.height):
                    return True
        return False

class GameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mein Pygame-Fenster")
        self.clock = pygame.time.Clock()
        self.player = Player(400, 400, 50, 50, self.width, self.height)
        self.enemies = []

    def spawn_enemy(self):
        x = random.randint(0, self.width - 50)
        y = random.randint(0, self.height - 50)
        enemy = Enemy(x, y, 50, 50, self.width, self.height, self.player, self.enemies)
        self.enemies.append(enemy)

    def run_game(self):
        enemy_spawn_timer = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            current_time = pygame.time.get_ticks()
            if current_time - enemy_spawn_timer > 2000:  # Spawn alle 2 Sekunden einen Gegner
                self.spawn_enemy()
                enemy_spawn_timer = current_time

            for enemy in self.enemies:
                enemy.move_towards_player()
                if self.player.check_collision(enemy):
                    print("Game Over!")
                    pygame.quit()
                    sys.exit()

                if enemy.check_collision_with_other_enemies():
                    self.enemies.remove(enemy)
                    self.spawn_enemy()

            self.window.fill((255, 255, 255))  # Hintergrundfarbe
            self.player.draw(self.window)

            for enemy in self.enemies:
                enemy.draw(self.window)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    pygame.init()

    window_size = (800, 800)
    game_window = GameWindow(*window_size)
    game_window.run_game()
