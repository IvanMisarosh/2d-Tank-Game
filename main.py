import pygame
import tank

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = tank.Tank(screen, player_pos.x, player_pos.y)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # pygame.draw.circle(screen, "red", player_pos, 40)

    # update the player
    player.update(dt)
    player.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
