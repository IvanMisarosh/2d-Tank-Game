import pygame
import tank
import enemy
import random

bullets = []
entities = []

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = tank.Tank(screen, player_pos.x, player_pos.y)

entities.append(player)

enenmy_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
test_enemy = enemy.EnemyTank(screen, enenmy_pos.x, enenmy_pos.y)

entities.append(test_enemy)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(player.shoot())

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_g]:
        new_enenmy_pos = pygame.Vector2(random.randint(0, screen.get_width() - 50), random.randint(0, screen.get_height() - 50))
        new_enemy = enemy.EnemyTank(screen, new_enenmy_pos.x, new_enenmy_pos.y)
        entities.append(new_enemy)

    for bullet in bullets:
        bullet.update(dt)
        bullet.draw()
        if bullet.pos.x < 0 or bullet.pos.x > screen.get_width() or bullet.pos.y < 0 or bullet.pos.y > screen.get_height():
            bullets.remove(bullet)

    for entity in entities:
        entity.update(dt)
        entity.draw()

    for bullet in bullets:
        for entity in entities:
            if bullet.rect.colliderect(entity.rect):
                if bullet.owner != entity:
                    bullets.remove(bullet)
                    entities.remove(entity)
                    break

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()
