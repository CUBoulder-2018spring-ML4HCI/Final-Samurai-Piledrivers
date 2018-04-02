import pygame
import math

self = pygame.init()
rbound = 1240
hbound = 380
screen = pygame.display.set_mode((rbound, hbound))


def main(self, screen):
    imagel = pygame.image.load('playerleft.png')
    imager = pygame.image.load('playerright.png')

    imagex = 320
    imagey = 240
    velocity_y = 0
    velocity_x = 0
    jumping = False
    jcount = 0
    left = True
    clock = pygame.time.Clock()
    bullets = []

    while 1:

        clock.tick(60)

        'active keypressing'
        keys = pygame.key.get_pressed()



        'moving left'
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            left = False

            'left boundary and movement'
            if imagex > -35:
                if velocity_x > 0:
                    acceleration = 2
                else:
                    acceleration = .3
                velocity_x = velocity_x - acceleration
                imagex = imagex + velocity_x
            else:
                velocity_x = 0

        'moving right'
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            left = True

            'setting boundaries and then movement'
            if imagex > rbound-20:
                velocity_x = 0
            else:
                if velocity_x < 0:
                    acceleration = 2
                else:
                    acceleration = .3
                velocity_x = velocity_x + acceleration
                imagex = imagex + velocity_x

        'jump init'
        if keys[pygame.K_SPACE]:
            jumping = True
            velocity_y = -12
        'jumping arc'
        if jumping and imagey <= 240:
            jcount = jcount + 1
            imagey = imagey + velocity_y + math.ceil(.5*jcount)
        'jump landing'
        if imagey >= 240:
            jumping = False
            imagey = 240
            jcount = 0

        'fire'
        if keys[pygame.K_DOWN]:
            bullets.append(Bullet(imagex, imagey, left))

        for event in pygame.event.get():

            'quit statements'
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        'bullet draw'
        screen.fill((200,200,200))
        for Bullet in bullets:
            Bullet.update()
        for Bullet in bullets:
            Bullet.draw()

        'player draw and refresh'
        if not left:
            screen.blit(imagel, (imagex,imagey))
        else:
            screen.blit(imager, (imagex,imagey))
        pygame.display.flip()


class Bullet:
    x = 0
    y = 0
    direction = False
    bulletimg = pygame.image.load('bulletimg.png')

    def __init__(self, i, j, left):
        self.x = i
        self.y = j
        if left:
            self.direction = True

    def update(self, x, y):
        if self.direction:
            self.x = x - 10
        else:
            self.x = x + 10
        if self.x > 2000 or self.x < 0:
            self.kill()

    def draw(self):
        screen.blit(self.bulletimg, (self.x, self.y))


main(self, screen)
