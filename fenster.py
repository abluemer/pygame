import random
import sys
import pygame
from gegner import Enemy

from spieler import Player


class GameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()  # Initialisiere Pygame
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mein Pygame-Fenster")
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load('background.png').convert()
        self.player = Player(400, 400, 50, 50, self.width, self.height)
        self.enemies = []


    def spawn_enemy(self):
        x = self.player.x
        y = self.player.y
        while self.player.x-100 < x < self.player.x+100 or self.player.y-100 < x < self.player.y+100: # solange im radius ist suche neu
            print(y)
            x = random.randint(0, self.width - 50)
            y = random.randint(0, self.height - 50)

        enemy = Enemy(x, y, 50, 50, self.player, self.enemies)
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

            self.window.blit(self.background_image, (0, 0))            # Hintergrundfarbe
            self.player.draw(self.window)

            for enemy in self.enemies:
                enemy.draw(self.window)

            pygame.display.flip()
            self.clock.tick(60)
