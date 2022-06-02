
win_width = 700
a,b=0,0
from pygame import *
from random import randint
from time import sleep
finish = False



mixer.init()
mixer.music.load('gx.ogg')
mixer.music.play()
fire_sound = mixer.Sound('woo.ogg')
start = mixer.Sound('windows.ogg')
stop = mixer.Sound('popit.ogg')
ends = mixer.Sound('end1.ogg')
window = display.set_mode((700,500))
background = transform.scale(image.load('gaga.jpg'),(700,500))
end =  transform.scale(image.load('end.jpg'),(700,500))
clock = time.Clock()
game = True
display.set_caption('8 марта')
health = 10
damage=None
score = 0
max_bullets=10
bullets_count=max_bullets
speed = 0


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_speed,player_y,a,b):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image),(a,b))
        self.speed = player_speed
        self.rect =self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        global speed 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        global bullets_count
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x+=self.speed
        if keys[K_SPACE]:           
            self.Fire() 
            fire_sound.play()

    def Fire(self):
        global bullets_count
        bullet=Bullet('ks.png',self.rect.centerx-12,10,self.rect.top,10,10)
        bullets.add(bullet)
        bullets_count-=1

    
class Enemy(GameSprite):
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        self.rect.y+=self.speed
        global damage
        global score
        if self.rect.y >=500 or sprite.collide_rect(player,self):
            damage=True
            self.Colide()
    def Colide(self):
        self.rect.y=0
        self.rect.x=randint(50,600)
        self.speed=randint(3,5)

e1= Enemy('JOTARO1.png', randint(100,600),randint(3,5),0,150,150)
e2= Enemy('JOTARO1.png', randint(100,600),randint(3,5),0,150,150)
e3= Enemy('JOTARO1.png', randint(100,600),randint(3,5),0,150,150)
e4= Enemy('JOTARO1.png', randint(100,600),randint(3,5),0,150,150)
e5= Enemy('gg.png', randint(100,600),randint(3,5),0,75,75)

class Bullet(GameSprite):
    def update(self):
        global score
        self.rect.y -= self.speed
        if self.rect.y <=0:
            self.kill()
        if sprite.collide_rect(e1,self):
            self.kill()
            score+=1
            e1.Colide()
        if sprite.collide_rect(e2,self):
            self.kill()
            score+=1
            e2.Colide()
        if sprite.collide_rect(e3,self):
            self.kill()
            score+=1
            e3.Colide()
        if sprite.collide_rect(e4,self):
            self.kill()
            score+=1
            e4.Colide()
        if sprite.collide_rect(e5,self):
            self.kill()
            score+=1
            e5.Colide()
player = Player('ks.png',285,10,win_width-280,65,65)
bullets=sprite.Group()
font.init()
font1 = font.Font(None,36)
font2 = font.Font(None, 70)
win = font2.render('YOU WIN' , True, (255, 215, 0))
lose = font2.render('YOU LOSE', True, (0, 255, 0)) 
volna1 = font2.render('THE WORLD!!!', True, (255, 255, 0))
volna2 = font2.render('2 ВОЛНА', True, (255, 255, 0))


enemies= sprite.Group()
enemies.add(e1)
enemies.add(e2)
enemies.add(e3)
enemies.add(e4)
enemies.add(e5)
start.play()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:  
        window.blit(background,(0,0))
        player.update()
        player.reset()
        enemies.draw(window)
        bullets.draw(window)
        enemies.update()
        bullets.update()
        text_health = font1.render('Жизни:'+str(health),False,(255,255,255))
        window.blit(text_health,(0,30))
        text_score = font1.render('Очки:'+str(score),False,(255,255,255))
        window.blit(text_score,(0,0))
        text_bullets = font1.render('Пуль:'+str(bullets_count)+'/'+str(max_bullets),False,(255,255,255))
        window.blit(text_bullets,(0,60))
    if damage:
        health-=1
    if score == 100:
        finish = True
        window.blit(volna1, (200,250))
        mixer.music.pause()
        stop.play()
        sleep(1)
        finish = False
        mixer.music.unpause()
    if score == 1000:
        mixer.music.pause()
        finish = True
        window.blit(volna1, (200,250))
        stop.play()
        sleep(1)
        finish = False
        mixer.music.unpause()
    if score == 10000:
        finish = True
        window.blit(win, (180,250))
      
    if health==0:
        finish = True
        mixer.music.stop()
        ends.play()
        window.blit(end, (0,0))

    
    damage = False
    if bullets_count==0:
        bullets_count=max_bullets


             
            
    display.update()
    clock.tick(120)