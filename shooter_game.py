from pygame import *
import random
 
from random import random, randrange, randint
from time import time as timer
 
font.init()
fontschemto = font.SysFont('Colibri', 39)
mixer.init()
 
dontlost = 0

b = 0
 
 
 
window = display.set_mode((700, 500))
 
display.set_caption('Шутер покруче CS-GO')
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
 
 
FPS = 60
 
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, x, y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x, y))
       
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
       
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
   
 
 
 
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT] and self.rect.x < 615:
            self.rect.x += 5
        if keys_pressed[K_LEFT] and keys_pressed[K_RSHIFT] and self.rect.x > 5:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and keys_pressed[K_RSHIFT] and self.rect.x < 631:
            self.rect.x += 10
    def fire(self):
        bullet007 = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -10)
        bullets.add(bullet007)    
    def fire_plus(self):
        bullet008 = Bullet('bullet.png', self.rect.left, self.rect.top, 15, 20, -7)
        bullet009 = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -7)
        bullet0010 = Bullet('bullet.png', self.rect.right, self.rect.top, 15, 20, -7)
        bullets_plus.add(bullet008) 
        bullets_plus.add(bullet009) 
        bullets_plus.add(bullet0010) 

    
 
 
 
 
lost = 0
 
 
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(5, 625)
            self.rect.y = 0
            lost = lost + 1
 
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
 
class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(50, 650)
            self.rect.y = 0
 
class Gift(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(50, 650) 
            self.rect.y = 0
            
 

      
    def reset_1(self):
        global b
        b = randint(1, 3)
        if b == 2:
            self.image = transform.scale(image.load('pixil-frame-0 (18).png'), (50, 50))
            window.blit(self.image, (self.rect.x, self.rect.y))
            
        else:
            self.image = transform.scale(image.load('pixil-frame-0 (19).png'), (50, 50))
            window.blit(self.image, (self.rect.x, self.rect.y))
        
class Bullet_plus(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
 
 
 
schet_bullet = 10
  
mixer.init()
money = mixer.Sound('fire.ogg')

 
player = Player('rocket.png', 325, 400, 80, 100, 3)
vragi = sprite.Group()
text_lose = fontschemto.render('Пропущенно:' + str(lost), 1, (255, 255, 255))
bullets = sprite.Group()
bullets_plus = sprite.Group()
 
 
asteroid = Asteroid('asteroid.png', randint(30, 670), -50, 50, 50, randint(4, randint(4, 6)))
  
text_bullet_plus = fontschemto.render('Пропущенно:' + str(lost), 1, (255, 255, 255))
text_bullet_minus = fontschemto.render('Сбито:' + str(dontlost), 1, (255, 255, 255))
gift_speed_bullet = Gift('pixil-frame-0 (19).png', randint(30, 670), -50, 50, 50, 5)

 
 
schetchik_pul = 0
fgh = False


asd = False
 
 
 
for i in range(randint(2, 4)):
    vrag = Enemy('ufo.png', randint(30, 670), -50, 80, 50, randint(1, randint(1, 2)))
    vragi.add(vrag)
 
 
 
win = fontschemto.render('YOU ARE WINNER!', True, (255, 215, 0))
wind = fontschemto.render('YOU ARE LOSER!', True, (255, 215, 0))


 
 
 
 
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
 
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if schetchik_pul < 8 and fgh == False:
                    schetchik_pul += 1
                    
                    if sprite.collide_rect(player, gift_speed_bullet) and b == 2:
                        if asd == False:
                            player.fire_plus()
                            money.play()
                            wert = timer()
                            asd = True
                    else:
                        player.fire()
                        money.play()
                if schetchik_pul >= 8 and fgh == False:
                    vremy = timer()
                    fgh = True
                          
    if not finish:
        window.blit(background,(0, 0))
       
     
        player.update()
        vragi.update()
        bullets.update()
        
        player.reset()
        vragi.draw(window)
        bullets.draw(window)
        
 
        asteroid.update()
        asteroid.reset()
       
           
 
 
       
        gift_speed_bullet.update()
        gift_speed_bullet.reset()
        if gift_speed_bullet.rect.y > 498:
            gift_speed_bullet.reset_1()

        
        




        

        bullets_plus.update()
        bullets_plus.draw(window)

        if fgh == True:
            ghj = timer()
            if ghj - vremy < 3:
                text_perezaradka = fontschemto.render('Падажжите, ПЕРЕЗАРЯДКА!', 1, (255, 255, 255))
                window.blit(text_perezaradka,(180, 200))
            else:
                schetchik_pul = 0
                fgh = False

        if asd == True:
            qwer = timer()
            if qwer - wert < 10:
                for e in event.get():
                    if e.type == KEYDOWN:
                        if e.key == K_SPACE:
                            player.fire_plus()
                            money.play()
            else:
                asd = False


        

                

        prprpr = sprite.groupcollide(vragi, bullets, True, True)
        prpr = sprite.groupcollide(vragi, bullets_plus, True, True)
   

 
 
 
               
 
 
        for i in prprpr:
            dontlost += 1
            vrag = Enemy('ufo.png', randint(30, 670), -50, 80, 50, randint(1, randint(1, randint(1, 2))))
            vragi.add(vrag)
        

  
        
        for i in prpr:
            dontlost += 1
            vrag = Enemy('ufo.png', randint(30, 670), -50, 80, 50, randint(1, randint(1, randint(1, 2))))
            vragi.add(vrag)
        if sprite.collide_rect(player, asteroid) or lost >= 10:
            window.blit(wind, (200, 200))
            finish = True
       
        if dontlost >= 30:
            window.blit(win, (200, 270))
            finish = True
 
 
 
 
        text_lose = fontschemto.render('Пропущенно:' + str(lost), 1, (255, 255, 255))
        text_dontlose = fontschemto.render('Сбито:' + str(dontlost), 1, (255, 255, 255))
        window.blit(text_lose,(5, 10))
        window.blit(text_dontlose,(5, 40))
 
       
           
 
 
 
 
 
        display.update()
    time.delay(10)
 

