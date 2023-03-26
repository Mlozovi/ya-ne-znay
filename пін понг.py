from pygame import *



class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > win_height - 400:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 530:
            self.rect.x += self.speed
   
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 480:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 530:
            self.rect.x += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 800
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("fon.png"), (win_width, win_height))



game = True
finish = False
clock = time.Clock()
FPS = 60


racket1 = Player('messi.png', 300, 200, 4, 75, 75)
racket2 = Player('suuuu.png', 300, 600, 4, 75, 75)
ball = GameSprite('myach.png', 200, 200, 5, 50, 50)

mixer.init()
mixer.music.load('fonmusik.ogg')
mixer.music.play()
gol = mixer.Sound('gol.ogg')
 

font.init()
font = font.Font(None, 35)
lose1 = font.render('rew', True, (180, 0, 0))
lose2 = font.render('r3w', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= 1
            speed_y *= -1

    

        if ball.rect.x > win_width-50 or ball.rect.x < 0:
            speed_x *= -1


        if ball.rect.y > 800:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True


        if ball.rect.y < 0:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

        display.update()
        clock.tick(FPS)

    



