import pygame
import time as t
def birinci_sınıf_birinci_soru():
    if (True):
        print("Bu soru ritmik sayma ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = window_y/2
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def mesaj(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Kumbarandaki 100 tl yi saymak için 10 tl den başlıyor ve onar ritmik olarak sayıyorsun.", red)
            write2("Dördüncü saymada kaç tl saymış olursun?", red)
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            KırkX = 40
            KırkY = 90
            otuz = pygame.image.load('30.png')
            otuz = pygame.transform.scale(otuz, (50,50))
            window.blit(otuz, (200, 300))
            kırk = pygame.image.load('40.png')
            kırk = pygame.transform.scale(kırk, (50,50))
            window.blit(kırk, (KırkX, KırkY))
            elli = pygame.image.load('50.png')
            elli = pygame.transform.scale(elli, (50,50))
            window.blit(elli, (600, 420))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            kumbara = pygame.image.load('kumbara.png')
            kumbara = pygame.transform.scale(kumbara, (80,80))
            window.blit(kumbara, (40, 420))
            answer = (((x - KırkX)** 2)+((y - KırkY)** 2)**1/2)
            if ((answer == 1894) or (answer == 3244) or (answer == 5494) or (answer == 4114) or (answer == 1864) or (answer == 514)):
                window.blit(kırk, (KırkX, 420))
                window.blit(doğru, (KırkX + speed, 420))
                window.blit(character_1, (2,30))
                mesaj("Soruyu doğru yaptın :D", red)
            elif((answer == 19744) or (answer == 251584) or (answer == 13924) or (answer == 280804)):
                window.blit(yanlış, (360, 150))
                mesaj("Tekrar denemelisin", red)
            pygame.display.update() 
        pygame.quit()
    else:
        print(" ")
def birinci_sınıf_birinci_soruX():
    if (True):
        print("Bu soru ritmik sayma ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = window_y/2
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def mesaj(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Arkadaşın bilyeleri saymak için 12 den başlıyor ve ikişer ritmik olarak sayıyor.", red)
            write2("Arkadaşın üçüncü saymada kaç bilye saymış olur?", red)
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            KırkX = 40
            KırkY = 90
            otuz = pygame.image.load('12.png')
            otuz = pygame.transform.scale(otuz, (50,50))
            window.blit(otuz, (200, 300))
            kırk = pygame.image.load('16.png')
            kırk = pygame.transform.scale(kırk, (50,50))
            window.blit(kırk, (KırkX, KırkY))
            elli = pygame.image.load('15.PNG')
            elli = pygame.transform.scale(elli, (50,50))
            window.blit(elli, (600, 420))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            answer = (((x - KırkX)** 2)+((y - KırkY)** 2)**1/2)
            if ((answer == 5494) or (answer == 4114) or (answer == 1864) or (answer == 3244)):
                window.blit(doğru, (250, 75))
                mesaj("Soruyu doğru yaptın :D", red)
            elif((answer == 19744) or (answer == 251584) or (answer == 13924) or (answer == 280804) or (answer == 288454) or (answer == 23794) or (answer == 17974) or (answer == 13954) or (answer == 259234) or (answer == 231814)):
                window.blit(yanlış, (250,75))
                mesaj("Tekrar denemelisin", red)
            pygame.display.update() 
        pygame.quit()
    else:
        print(" ")
def birinci_sınıf_birinci_soruXX():
    if (True):
        print("Bu soru ritmik sayma ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = window_y/2
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def mesaj(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Bir arkadaşın geriye doğru beşer ritmik saymak istiyor ve saymaya 30 dan başlıyor.", red)
            write2("Üçüncü saymada arkadaşın hangi sayıyı söyler?", red)
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            otuz = pygame.image.load('40.png')
            otuz = pygame.transform.scale(otuz, (50,50))
            window.blit(otuz, (200, 300))
            kırk = pygame.image.load('15.PNG')
            kırk = pygame.transform.scale(kırk, (50,50))
            window.blit(kırk, (40, 90))
            elli = pygame.image.load('20.png')
            elli = pygame.transform.scale(elli, (50,50))
            window.blit(elli, (600, 420))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            answer = (((x - 600)** 2)+((y - 420)** 2)**1/2)
            if ((answer == 10564) or (answer == 7414) or (answer == 5164) or (answer == 9544) or (answer == 11794) or (answer == 17974)):
                window.blit(doğru, (250, 75))
                mesaj("Soruyu doğru yaptın :D", red)
            elif((answer == 250534) or (answer == 244684) or (answer == 216904) or (answer == 222754) or (answer == x) or (answer == 422404) or (answer == 433654) or (answer == 445804) or (answer == 410824) or (answer == 398674) or (answer == 387424)):
                window.blit(yanlış, (250, 75))
                mesaj("Tekrar denemelisin", red)
            pygame.display.update() 
        pygame.quit()
    else:
        print(" ")
def birinci_sınıf_ikinci_soru():
    if (True):
        print("Bu soru toplama ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            write("Karenin arkasında saklanan sayı nedir? ", red)
            oniki = pygame.image.load('12.png')
            oniki = pygame.transform.scale(oniki,(50,50))
            window.blit(oniki, (100,300))
            artı = pygame.image.load('artı_işareti.png')
            artı = pygame.transform.scale(artı,(50,50))
            window.blit(artı, (200,300))
            esit = pygame.image.load('eşittir_işareti.png')
            esit = pygame.transform.scale(esit,(50,50))
            window.blit(esit, (400,300))
            pygame.draw.rect(window, red, (300,300,width,height))    
            dört = pygame.image.load('4.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (300,500))
            üç = pygame.image.load('3.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (50,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            beş = pygame.image.load('5.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,500))
            onaltı = pygame.image.load('16.png')
            onaltı = pygame.transform.scale(onaltı,(50,50))
            window.blit(onaltı, (500,300))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")

def birinci_sınıf_ikinci_soruX():
    if (True):
        print("Bu soru toplama ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            write("Karenin arkasında saklanan sayı nedir? ", red)
            oniki = pygame.image.load('8.png')
            oniki = pygame.transform.scale(oniki,(50,50))
            window.blit(oniki, (100,300))
            artı = pygame.image.load('artı_işareti.png')
            artı = pygame.transform.scale(artı,(50,50))
            window.blit(artı, (200,300))
            esit = pygame.image.load('eşittir_işareti.png')
            esit = pygame.transform.scale(esit,(50,50))
            window.blit(esit, (400,300))
            pygame.draw.rect(window, red, (500,300,width,height))
            dört = pygame.image.load('20.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (300,500))
            üç = pygame.image.load('15.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (50,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            beş = pygame.image.load('30.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,500))
            onaltı = pygame.image.load('12.png')
            onaltı = pygame.transform.scale(onaltı,(50,50))
            window.blit(onaltı, (300,300))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")


def birinci_sınıf_ikinci_soruXX():
    if (True):
        print("Bu soru toplama ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            write("Karenin arkasında saklanan sayı nedir? ", red)
            oniki = pygame.image.load('20.png')
            oniki = pygame.transform.scale(oniki,(50,50))
            window.blit(oniki, (300,300))
            artı = pygame.image.load('artı_işareti.png')
            artı = pygame.transform.scale(artı,(50,50))
            window.blit(artı, (200,300))
            esit = pygame.image.load('eşittir_işareti.png')
            esit = pygame.transform.scale(esit,(50,50))
            window.blit(esit, (400,300))
            pygame.draw.rect(window, red, (100,300,width,height))    
            dört = pygame.image.load('15.PNG')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (300,500))
            üç = pygame.image.load('16.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (50,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            beş = pygame.image.load('12.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,500))
            onaltı = pygame.image.load('35.png')
            onaltı = pygame.transform.scale(onaltı,(50,50))
            window.blit(onaltı, (500,300))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")
        
def birinci_sınıf_ucuncu_soru():
    if (True):
        print("Bu oyun ise çıkarma ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed       
            background = pygame.image.load('Ocean.png').convert()
            window.blit(background, [0,0])
            character_1 = pygame.image.load('yunus.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            write("Sepettimde 10 elma var 4 tanesi arkadaşlarıma dağıttım. Kaç elmam kaldı?", red)
            sepet = pygame.image.load('Elmalar2.PNG')
            sepet = pygame.transform.scale(sepet,(80,80))
            window.blit(sepet, (40,340))
            sepet2 = pygame.image.load('Elmalar2.PNG')
            sepet2 = pygame.transform.scale(sepet2,(80,80))
            window.blit(sepet2, (40,260))
            sepet3 = pygame.image.load('ikili_elma.png')
            sepet3 = pygame.transform.scale(sepet3,(80,40))
            window.blit(sepet3, (40,220))
            eksi = pygame.image.load('Eksi_işareti.PNG')
            eksi = pygame.transform.scale(eksi,(80,10))
            window.blit(eksi, (190,325))
            esit = pygame.image.load('eşittir_işareti.png')
            esit = pygame.transform.scale(esit,(80,25))
            window.blit(esit, (400,325))
            elmalar = pygame.image.load('Elmalar2.PNG')
            elmalar = pygame.transform.scale(elmalar,(80,80))
            window.blit(elmalar, (300,300))              
            dört = pygame.image.load('5.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (550,500))
            üç = pygame.image.load('4.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (50,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            beş = pygame.image.load('6.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (300,500))
            onaltı = pygame.image.load('soru_işareti.PNG')
            onaltı = pygame.transform.scale(onaltı,(80,80))
            window.blit(onaltı, (500,300))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")



def birinci_sınıf_ucuncu_soruX():
    if (True):
            print("Bu soru çıkarma ile ilgili.")
            t.sleep(2)
            pygame.init()
            window_x = 724
            window_y = 600
            window = pygame.display.set_mode((window_x,window_y))
            pygame.display.set_caption("First_Game")
            limit = window_x
            speed = 30
            x = window_x/2
            y = 100
            width = 50
            height = 50
            white = (255,255,255)
            clock = pygame.time.Clock()
            white = (255,255,255)
            black = (0,0,0)
            red = (255,0,0)
            font = pygame.font.SysFont(None, 25)
            run = True
            def blitme(self):
                self.window.blit(self.image, self.rect)
            def write(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [20,20])
            def write2(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [20,45])
            def write3(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [20,60])
            def doğru_yaptın(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [300,100])
            while (run):
                pygame.time.delay(100)
                for user_events in pygame.event.get():
                    if user_events.type == pygame.QUIT:
                        run = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and x > speed:  #keyboard
                    x = x - speed
                if keys[pygame.K_v] and x > speed:
                    x = x - speed    
                if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                    x = x + speed
                if keys[pygame.K_SPACE] and x < (600 - width - speed):
                    x = x + speed    
                if keys[pygame.K_UP] and y > 10: #keyboard
                    y = y - speed
                if keys[pygame.K_n] and y > 10:
                    y = y - speed    
                if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                    y = y + speed
                if keys[pygame.K_b] and y < (500 - height - speed):
                    y = y + speed        
                background = pygame.image.load('ocean.png').convert()
                window.blit(background, [0,0])
                character_1 = pygame.image.load('yunus.png')
                character_1 = pygame.transform.scale(character_1,(180,180))
                window.blit(character_1, (x,y))
                write("Karenin arkasında saklanan sayı nedir? ", red)
                oniki = pygame.image.load('50.png')
                oniki = pygame.transform.scale(oniki,(50,50))
                window.blit(oniki, (100,300))
                artı = pygame.image.load('Eksi_işareti.png')
                artı = pygame.transform.scale(artı,(80,10))
                window.blit(artı, (180,320))
                esit = pygame.image.load('eşittir_işareti.png')
                esit = pygame.transform.scale(esit,(50,25))
                window.blit(esit, (400,310))
                pygame.draw.rect(window, red, (300,300,width,height))    
                dört = pygame.image.load('35.png')
                dört = pygame.transform.scale(dört,(80,80))
                window.blit(dört, (300,500))
                üç = pygame.image.load('30.png')
                üç = pygame.transform.scale(üç,(80,80))
                window.blit(üç, (50,500))
                doğru = pygame.image.load('doğru.png')
                doğru = pygame.transform.scale(doğru, (50,50))
                yanlış = pygame.image.load('çarpı işareti.png')
                yanlış = pygame.transform.scale(yanlış, (50,50))
                beş = pygame.image.load('40.png')
                beş = pygame.transform.scale(beş,(80,80))
                window.blit(beş, (550,500))
                onaltı = pygame.image.load('15.png')
                onaltı = pygame.transform.scale(onaltı,(50,50))
                window.blit(onaltı, (500,300))
                answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
                if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                    window.blit(doğru, (360, 150))
                    write2("Soruyu doğru yaptın :D", red)
                elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                    window.blit(yanlış, (360, 150))
                    write2("Tekrar denemelisin", red)  
                pygame.display.update()
            pygame.quit()
    else:
        print(" ")
    
def birinci_sınıf_ucuncu_soruXX():
    if (True):
            print("Bu soru çıkarma ile ilgili.")
            t.sleep(2)
            pygame.init()
            window_x = 724
            window_y = 600
            window = pygame.display.set_mode((window_x,window_y))
            pygame.display.set_caption("First_Game")
            limit = window_x
            speed = 30
            x = window_x/2
            y = 100
            width = 50
            height = 50
            white = (255,255,255)
            clock = pygame.time.Clock()
            white = (255,255,255)
            black = (0,0,0)
            red = (255,0,0)
            font = pygame.font.SysFont(None, 25)
            run = True
            def blitme(self):
                self.window.blit(self.image, self.rect)
            def write(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [20,20])
            def write2(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [20,45])
            def write3(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [20,60])
            def doğru_yaptın(msg,color):
                screen_text = font.render(msg,True,color)
                window.blit(screen_text, [300,100])
            while (run):
                pygame.time.delay(100)
                for user_events in pygame.event.get():
                    if user_events.type == pygame.QUIT:
                        run = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and x > speed:  #keyboard
                    x = x - speed
                if keys[pygame.K_v] and x > speed:
                    x = x - speed    
                if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                    x = x + speed
                if keys[pygame.K_SPACE] and x < (600 - width - speed):
                    x = x + speed    
                if keys[pygame.K_UP] and y > 10: #keyboard
                    y = y - speed
                if keys[pygame.K_n] and y > 10:
                    y = y - speed    
                if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                    y = y + speed
                if keys[pygame.K_b] and y < (500 - height - speed):
                    y = y + speed        
                background = pygame.image.load('ocean.png').convert()
                window.blit(background, [0,0])
                character_1 = pygame.image.load('yunus.png')
                character_1 = pygame.transform.scale(character_1,(180,180))
                window.blit(character_1, (x,y))
                write("Karenin arkasında saklanan sayı nedir? ", red)
                oniki = pygame.image.load('30.png')
                oniki = pygame.transform.scale(oniki,(50,50))
                window.blit(oniki, (300,300))
                artı = pygame.image.load('Eksi_işareti.png')
                artı = pygame.transform.scale(artı,(80,10))
                window.blit(artı, (180,320))
                esit = pygame.image.load('eşittir_işareti.png')
                esit = pygame.transform.scale(esit,(50,25))
                window.blit(esit, (400,310))
                pygame.draw.rect(window, red, (100,300,width,height))    
                dört = pygame.image.load('45.png')
                dört = pygame.transform.scale(dört,(80,80))
                window.blit(dört, (300,500))
                üç = pygame.image.load('40.png')
                üç = pygame.transform.scale(üç,(80,80))
                window.blit(üç, (50,500))
                doğru = pygame.image.load('doğru.png')
                doğru = pygame.transform.scale(doğru, (50,50))
                yanlış = pygame.image.load('çarpı işareti.png')
                yanlış = pygame.transform.scale(yanlış, (50,50))
                beş = pygame.image.load('50.png')
                beş = pygame.transform.scale(beş,(80,80))
                window.blit(beş, (550,500))
                onaltı = pygame.image.load('15.PNG')
                onaltı = pygame.transform.scale(onaltı,(50,50))
                window.blit(onaltı, (500,300))
                answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
                if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                    window.blit(doğru, (360, 150))
                    write2("Soruyu doğru yaptın :D", red)
                elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                    window.blit(yanlış, (360, 150))
                    write2("Tekrar denemelisin", red)  
                pygame.display.update()
            pygame.quit()
    else:
        print(" ")
    

def birinci_sınıf_dorduncu_soru():
    if (True):
        print("Bu soru ise saatler ile ilgili. ")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 300
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y >= 100: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y >= 100:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed                         
            background = pygame.image.load('Ocean.png').convert()
            window.blit(background, [0,0])
            elmalar = pygame.image.load('dalgalar.png')
            elmalar = pygame.transform.scale(elmalar,(800,40))
            window.blit(elmalar, (0,120))           
            dört = pygame.image.load('SaatAltOtuz.png')
            dört = pygame.transform.scale(dört,(150,150))
            window.blit(dört, (25,300))
            üç = pygame.image.load('saat1.png')
            üç = pygame.transform.scale(üç,(150,150))
            window.blit(üç, (300,425))
            beş = pygame.image.load('Saat2.PNG')
            beş = pygame.transform.scale(beş,(150,150))
            window.blit(beş, (550,300))
            character_1 = pygame.image.load('yunus.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            write("Saat 6.30'da bir saatin akrep ve yelkovanı nasıl görünür? ", red)
            sepet = pygame.image.load('Sun.png')
            sepet = pygame.transform.scale(sepet,(100,100))
            window.blit(sepet, (600,0))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 400)** 2)**1/2)
            if (((x == 30) and ((y == 310) or ((y == 340) or (y == 280) or (y == 250) or (y == 220))) or ((x == 60) and ((y == 310) or (y == 340) or (y == 280) or (y == 250) or (y == 220))))):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            elif (((x == 300) and (y == 400)) or ((x == 540) and (y == 280))):
                window.blit(yanlış, (360, 150))
                write2("Tekrar denemelisin", red)
            pygame.display.update() 
        pygame.quit()
    else:
        print(" ")

def birinci_sınıf_dorduncu_soruX():
    if (True):
        print("Bu soru ise saatler ile ilgili. ")
        
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 300
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 50)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,75])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        def saat1(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [350,480])
        def saat2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [585,350])
        def saat3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [25,300])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y >= 100: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y >= 100:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed                         
            background = pygame.image.load('Ocean.png').convert()
            window.blit(background, [0,0])
            elmalar = pygame.image.load('dalgalar.png')
            elmalar = pygame.transform.scale(elmalar,(800,40))
            window.blit(elmalar, (0,120))        
            saat1("3.30", red)
            saat2("3.00", red)
            saat3("2.30", red)
            character_1 = pygame.image.load('yunus.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            write("Bu saat kaçtır?", red)
            sepet = pygame.image.load('sarı_saat.png')
            sepet = pygame.transform.scale(sepet,(175,175))
            window.blit(sepet, (550,0))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 400)** 2)**1/2)
            if (((x == 30) and ((y == 310) or ((y == 340) or (y == 280) or (y == 250) or (y == 220))) or ((x == 60) and ((y == 310) or (y == 340) or (y == 280) or (y == 250) or (y == 220))))):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            elif (((x == 300) and (y == 400)) or ((x == 540) and (y == 280))):
                window.blit(yanlış, (360, 150))
                write2("Tekrar denemelisin", red)
            pygame.display.update() 
        pygame.quit()
    else:
        print(" ")


def birinci_sınıf_dorduncu_soruXX():
    if (True):
        print("Bu soru ise saatler ile ilgili. ")
        
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 300
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 50)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,75])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        def saat1(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [350,480])
        def saat2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [585,350])
        def saat3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [25,300])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y >= 100: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y >= 100:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed                         
            background = pygame.image.load('Ocean.png').convert()
            window.blit(background, [0,0])
            elmalar = pygame.image.load('dalgalar.png')
            elmalar = pygame.transform.scale(elmalar,(800,40))
            window.blit(elmalar, (0,120))        
            saat1("2.45", red)
            saat2("2.50", red)
            saat3("2.40", red)
            character_1 = pygame.image.load('yunus.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            write("Bu saat kaçtır?", red)
            sepet = pygame.image.load('genel_saat.png')
            sepet = pygame.transform.scale(sepet,(175,175))
            window.blit(sepet, (550,0))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 400)** 2)**1/2)
            if (((x == 30) and ((y == 310) or ((y == 340) or (y == 280) or (y == 250) or (y == 220))) or ((x == 60) and ((y == 310) or (y == 340) or (y == 280) or (y == 250) or (y == 220))))):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            elif (((x == 300) and (y == 400)) or ((x == 540) and (y == 280))):
                window.blit(yanlış, (360, 150))
                write2("Tekrar denemelisin", red)
            pygame.display.update() 
        pygame.quit()
    else:
        print(" ")



def birinci_sınıf_besinci_soru():
    if (True):
        print("Sana sormak istediğim bu soru şekiller ve örüntüler ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 250
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        blue = (48, 105, 152)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            sepet = pygame.image.load('soru_işareti_2.png')
            sepet = pygame.transform.scale(sepet,(50,50))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            background = pygame.image.load('Uzay.PNG').convert()
            window.blit(background, [0,0])
            pygame.draw.rect(window, white, (50,120,50,50))
            pygame.draw.circle(window, white, (165,145), 30)
            pygame.draw.rect(window, white, (230,120,100,50))
            window.blit(sepet, (360,120))
            pygame.draw.circle(window, white, (480,145), 30)
            pygame.draw.rect(window, white, (560,120,100,50))
            write("Soru işaretinin arkasında kalan şekil örüntüye göre nedir? ", red)
            pygame.draw.rect(window, white, (100,450,50,50))
            pygame.draw.circle(window, white, (350,500), 30)
            pygame.draw.rect(window, white, (550,450,100,50))
            character_1 = pygame.image.load('UFO2.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (250, 45))
                write2("Soruyu doğru yaptın :D", red)
                pygame.draw.rect(window, white, (360,120,50,50))
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (250, 45))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")

def birinci_sınıf_besinci_soruX():
    if (True):
        print("Sana sormak istediğim bu soru şekiller ve örüntüler ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 272
        y = 70
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        blue = (48, 105, 152)
        font = pygame.font.SysFont(None, 35)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            sepet = pygame.image.load('soru_işareti_2.png')
            sepet = pygame.transform.scale(sepet,(50,50))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            background = pygame.image.load('Uzay.PNG').convert()
            window.blit(background, [0,0])
            write("Aşağıdakilerden hangisinin kenarları birbirine eşittir?", red)
            dikdortgen = pygame.image.load('dikdörtgen.png')
            dikdörtgen = pygame.transform.scale(dikdortgen,(100,80))
            window.blit(dikdörtgen, [550,450])
            kare = pygame.image.load('kutu.png')
            kutu = pygame.transform.scale(kare,(100,100))
            window.blit(kutu, [100,450])
            ucgen = pygame.image.load('dik_ucgen.png')
            dik = pygame.transform.scale(ucgen,(100,80))
            window.blit(dik, [350,500])
            character_1 = pygame.image.load('UFO2.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (250, 75))
                write2("Soruyu doğru yaptın :D", red)
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (250, 75))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")

def birinci_sınıf_besinci_soruXX():
    if (True):
        print("Sana sormak istediğim bu soru şekiller ve örüntüler ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 250
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        blue = (48, 105, 152)
        font = pygame.font.SysFont(None, 35)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            sepet = pygame.image.load('soru_işareti_2.png')
            sepet = pygame.transform.scale(sepet,(50,50))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            background = pygame.image.load('Uzay.PNG').convert()
            window.blit(background, [0,0])
            write("Aşağıdakilerden hangisinin kenarı yoktur?", red)
            pygame.draw.rect(window, white, (350,500,50,50))
            pygame.draw.circle(window, white, (100,450), 30)
            pygame.draw.rect(window, white, (550,450,100,50))
            character_1 = pygame.image.load('UFO2.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (250, 75))
                write2("Soruyu doğru yaptın :D", red)
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (250, 75))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")


def ikinci_sınıf_birinci_soru():
    if (True):
        print("Sana sormak istediğim ilk soru çarpma işlemleri ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])           
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('AsfaltYol.PNG').convert()
            window.blit(background, [0,0])
            artı = pygame.image.load('carpma1.jpg')
            artı = pygame.transform.scale(artı,(300,230))
            window.blit(artı, (25,90))
            write("Bulmacanın sonucuna doğru ulaşmak için araba hangi istasyona gitmeli? ", red)
            dört = pygame.image.load('benzin istasyonu.PNG')
            dört = pygame.transform.scale(dört,(120,120))
            window.blit(dört, (565,470))
            üç = pygame.image.load('benzin_istasyonu_2.PNG')
            üç = pygame.transform.scale(üç,(120,120))
            window.blit(üç, (50,450))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            benzin3 = pygame.image.load('benzin_istasyonu3.PNG')
            benzin3 = pygame.transform.scale(benzin3, (120,120))
            benzin3 = window.blit(benzin3, (575,75))
            beş = pygame.image.load('5.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (565,390))
            onaltı = pygame.image.load('15.PNG')
            onaltı = pygame.transform.scale(onaltı,(50,50))
            window.blit(onaltı, (50,400))
            sekiz = pygame.image.load('8.PNG')
            sekiz = pygame.transform.scale(sekiz,(50,50))
            window.blit(sekiz, (645,25))
            character_1 = pygame.image.load('BumbleBee.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            if (((x == 2) and (y == 430)) or ((x == 2) and (y == 400))):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")

def ikinci_sınıf_birinci_soruX():
    if (True):
        print("Sana sormak istediğim ilk soru çarpma işlemleri ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])           
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('AsfaltYol.PNG').convert()
            window.blit(background, [0,0])
            artı = pygame.image.load('carpma2.jpg')
            artı = pygame.transform.scale(artı,(300,230))
            window.blit(artı, (25,90))
            write("Bulmacanın sonucuna doğru ulaşmak için araba hangi istasyona gitmeli? ", red)
            dört = pygame.image.load('benzin istasyonu.PNG')
            dört = pygame.transform.scale(dört,(120,120))
            window.blit(dört, (565,470))
            üç = pygame.image.load('benzin_istasyonu_2.PNG')
            üç = pygame.transform.scale(üç,(120,120))
            window.blit(üç, (575,75))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            benzin3 = pygame.image.load('benzin_istasyonu3.PNG')
            benzin3 = pygame.transform.scale(benzin3, (120,120))
            benzin3 = window.blit(benzin3, (50,450))
            beş = pygame.image.load('5.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (565,390))
            onaltı = pygame.image.load('15.PNG')
            onaltı = pygame.transform.scale(onaltı,(50,50))
            window.blit(onaltı, (645,25))
            sekiz = pygame.image.load('8.PNG')
            sekiz = pygame.transform.scale(sekiz,(50,50))
            window.blit(sekiz, (50,400))
            character_1 = pygame.image.load('BumbleBee.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            if (((x == 2) and (y == 430)) or ((x == 2) and (y == 400))):
                window.blit(doğru, (360, 150))
                write2("Soruyu doğru yaptın :D", red)
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")

def ikinci_sınıf_birinci_soruXX():
    if (True):
        print("Sana sormak istediğim ilk soru çarpma işlemleri ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = window_x/2
        y = 100
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 30)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,65])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,60])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,150])           
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('AsfaltYol.PNG').convert()
            window.blit(background, [0,0])
            write("Araba, 7'nin 5 katının yazılı olduğu istasyona gitmelidir.", red)
            write2("Buna göre araba hangi istasyona gitmelidir.", red)
            dört = pygame.image.load('benzin istasyonu.PNG')
            dört = pygame.transform.scale(dört,(120,120))
            window.blit(dört, (50,450))
            üç = pygame.image.load('benzin_istasyonu_2.PNG')
            üç = pygame.transform.scale(üç,(120,120))
            window.blit(üç, (575,75))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            benzin3 = pygame.image.load('benzin_istasyonu3.PNG')
            benzin3 = pygame.transform.scale(benzin3, (120,120))
            benzin3 = window.blit(benzin3, (565,470))
            beş = pygame.image.load('30.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (565,390))
            onaltı = pygame.image.load('45.PNG')
            onaltı = pygame.transform.scale(onaltı,(50,50))
            window.blit(onaltı, (645,25))
            sekiz = pygame.image.load('35.PNG')
            sekiz = pygame.transform.scale(sekiz,(50,50))
            window.blit(sekiz, (50,400))
            character_1 = pygame.image.load('BumbleBee.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            if (((x == 2) and (y == 430)) or ((x == 2) and (y == 400))):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")



def ikinci_sınıf_ikinci_soru():
    if (True):
        print("Bu soru toplama ve bölme içeren bir soru tipi.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('Ocean.png').convert()
            window.blit(background, [0,0])
            write("Bayram harçlığı olarak 57 tl aldığını düşün.", red)
            write2("En yakın arkadaşın ise senin paranın 3 fazlasının yarısını aldı.", red)
            write3("En yakın arkadaşın harçlık olarak kaç Tl aldı?", red)    
            dört = pygame.image.load('20.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (550,500))
            üç = pygame.image.load('30.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('60.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (50,500))
            character_1 = pygame.image.load('yunus.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")
def ikinci_sınıf_ikinci_soruX():
    if (True):
        print("Bu soru toplama ve bölme içeren bir soru tipi.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('Ocean.png').convert()
            window.blit(background, [0,0])
            write("20 tane oyuncağın olduğunu düşün.", red)
            write2("Arkadaşının oyuncaklarının sayısı senin oyuncaklarının dört fazlasının yarısıdır.", red)
            write3("Arkadaşının kaç oyuncağı vardır?", red)    
            dört = pygame.image.load('6.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (550,500))
            üç = pygame.image.load('12.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('8.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (50,500))
            character_1 = pygame.image.load('yunus.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")

def ikinci_sınıf_ikinci_soruXX():
    if (True):
        print("Bu soru toplama ve bölme içeren bir soru tipi.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('Ocean.png').convert()
            window.blit(background, [0,0])
            write("35 tane kitabın olduğunu düşün.", red)
            write2("5 tanesini arkadaşlarına hediye ediyorsun. Sonra, kalan kitapların yarısı bağışlıyorsun.", red)
            write3("Geriye kaç kitabın kalır?", red)    
            dört = pygame.image.load('20.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (550,500))
            üç = pygame.image.load('15.PNG')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('12.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (50,500))
            character_1 = pygame.image.load('yunus.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()
        pygame.quit()
    else:
        print(" ")


def ikinci_sınıf_ucuncu_soru():
    if (True):
        print("Bu soru ise uzunluk hesaplama ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])   
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Ailen sana oyuncak ve kıyafetlerini koyman için yeni bir dolap almak istiyor.", red)
            write2("Dolabın uzun kenarı 75 cm ve dolabın kısa kenarı uzun kenarından 35 cm kısa olmalı.", red)
            write3("Ailenin sana alıcağı dolabın kısa kenarı kaç cm olbilir?", red)                    
            dört = pygame.image.load('35.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (550,510))
            üç = pygame.image.load('40.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,510))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('45.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (50,510))
            beş = pygame.image.load('dolap.PNG')
            beş = pygame.transform.scale(beş,(100,150))
            window.blit(beş, (10,350))          
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()                
        pygame.quit()
    else:
        print(" ")

def ikinci_sınıf_ucuncu_soruX():
    if (True):
        print("Bu soru ise uzunluk hesaplama ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        green = (0,255,0)
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])   
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Bir diktörtgen düşün.", red)
            write2("Bu dikdörtgenin kısa kenarı 5cm. Uzun kenardı da kısa kenarının 3 katıdır.", red)
            write3("Bu dikdörtgenin uzun kenarı kaç cm olabilir.", red)                    
            dört = pygame.image.load('8.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (550,510))
            üç = pygame.image.load('15.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,510))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('5.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (50,510))
            pygame.draw.rect(window,green,(10,350,50,150))         
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()                
        pygame.quit()
    else:
        print(" ")

def ikinci_sınıf_ucuncu_soruXX():
    if (True):
        print("Bu soru ise uzunluk hesaplama ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        green = (0,255,0)
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])   
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Bir diktörtgen hayal et.", red)
            write2("Bu dikdörtgenin uzun kenarı 65 cm'dir. Kısa kenar uzun kenarın 20 eksiğidir", red)
            write3("Kısa kenar kaç santim olabilir.", red)                    
            dört = pygame.image.load('30.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (550,510))
            üç = pygame.image.load('40.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,510))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('15.PNG')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (50,510))
            pygame.draw.rect(window,red,(10,300,120,195))         
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((answer2 == 16374) or (answer2 == 101949) or (answer2 == 58149) or (answer2 == 3234) or (answer2 == 2454) or (answer2 == 5004) or (answer2 == 8364) or (answer2 == 5784) or (answer2 == 12744) or (answer2 == 18924) or (answer2 == 5814) or (answer2 == 10194)):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif ((answer2 == 91254) or (answer2 == 74274) or (answer2 == 76824) or (answer2 == 93804) or (answer2 == 61014) or (answer2 == 47374) or (answer2 == 35574) or (answer2 == 47394) or (answer2 == 49944)or (answer2 == 63564)): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()                
        pygame.quit()
    else:
        print(" ")


def ikinci_sınıf_dorduncu_soru():
    if (True):
        print("Bu soru kesirler ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100]) 
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed            
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Ailen, arkadaşların ile berabersin ve 8 dilimlik bir pizzan var.", red)
            write2("Bu sekiz dilimlik pizanın 2 dilimini ailene, 3 dilimini arkadaşlarına veriyorsun.", red)
            write3("Geriye kalan pizza dilimlerinin sayısı kesir olarak nasıl gösterilir?", red)                    
            dört = pygame.image.load('5bölü8.PNG')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (300,500))
            üç = pygame.image.load('3bölüsekiz.PNG')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (100,450))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))            
            beş = pygame.image.load('2bölü8.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,450))
            beş = pygame.image.load('pizza1.png')
            beş = pygame.transform.scale(beş,(150,150))
            window.blit(beş, (10,200))            
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()       
        pygame.quit()
    else:
        print(" ")

def ikinci_sınıf_dorduncu_soruX():
    if (True):
        print("Bu soru kesirler ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100]) 
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed            
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("Aşağıdaki şekillerden hangisi çeyrek parçalara ayrılmamıştır?", red)                    
            dört = pygame.image.load('1bolu4.PNG')
            dört = pygame.transform.scale(dört,(100,100))
            window.blit(dört, (300,475))
            üç = pygame.image.load('kırmızı_ucgen.PNG')
            üç = pygame.transform.scale(üç,(100,100))
            window.blit(üç, (100,450))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))            
            beş = pygame.image.load('2bolu8.PNG')
            beş = pygame.transform.scale(beş,(100,100))
            window.blit(beş, (550,450))       
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()       
        pygame.quit()
    else:
        print(" ")
        
def ikinci_sınıf_dorduncu_soruXX():
    if (True):
        print("Bu soru kesirler ile ilgili.")
        t.sleep(2)
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 442
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100]) 
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed            
            background = pygame.image.load('GökYüzü.png').convert()
            window.blit(background, [0,0])
            write("12 tane elma çeyrek gruplara ayrılırsa bir grupta kaç elma olur?", red)         
            üç = pygame.image.load('üçlü_elmalar.png')
            üç = pygame.transform.scale(üç,(175,100))
            window.blit(üç, (10,100))
            beş = pygame.image.load('üçlü_elmalar.png')
            beş = pygame.transform.scale(beş,(175,100))
            window.blit(beş, (180,100))
            dört = pygame.image.load('üçlü_elmalar.png')
            dört = pygame.transform.scale(dört,(175,100))
            window.blit(dört, (10,200))
            dörtt = pygame.image.load('üçlü_elmalar.png')
            dörtl = pygame.transform.scale(dörtt,(175,100))
            window.blit(dörtl, (180,200))
            
            dört = pygame.image.load('4.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (300,500))
            üç = pygame.image.load('3.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (100,450))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))            
            beş = pygame.image.load('6.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,450))          
            character_1 = pygame.image.load('butterfly.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((x == 52) and (y == 400) or ((x == 52) and (y == 370))):
                window.blit(doğru, (600, 100))
                write2("Soruyu doğru yaptın :D", red)
            elif (((x == 232) and (y == 430) or ((x == 502) and (y == 370)))): 
                window.blit(yanlış, (600, 100))
                write2("Tekrar denemelisin", red)  
            pygame.display.update()       
        pygame.quit()
    else:
        print(" ")

        
def ikinci_sınıf_besinci_soru():
    if (True):
        print("Bu soru ise para hesaplama ile ilgili.")
        t.sleep(2)
        import pygame
        import random 
        import time 
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('Uzay.PNG').convert()
            window.blit(background, [0,0])
            write("Arkadaşın her hafta 5 tl biriktiriyor.", red)
            write2("Arkadaşının 3 hafta sonunda kaç tl si olur?", red)   
            dört = pygame.image.load('15.PNG')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (100,450))
            üç = pygame.image.load('30.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('8.PNG')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,450))
            character_1 = pygame.image.load('UFO2.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()   
        pygame.quit()
    else:
        print(" ")

def ikinci_sınıf_besinci_soruX():
    if (True):
        print("Bu soru ise para hesaplama ile ilgili.")
        t.sleep(2)
        import pygame
        import random 
        import time 
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('Uzay.PNG').convert()
            window.blit(background, [0,0])
            write("30 tl ile tanesi 5 tl olan kalemlerden en fazla kaç tane alabilirsin?", red) 
            dört = pygame.image.load('6.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (100,450))
            üç = pygame.image.load('5.PNG')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('8.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,450))
            character_1 = pygame.image.load('UFO2.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()   
        pygame.quit()
    else:
        print(" ")


def ikinci_sınıf_besinci_soruXX():
    if (True):
        print("Bu soru ise para hesaplama ile ilgili.")
        t.sleep(2)
        import pygame
        import random 
        import time 
        pygame.init()
        window_x = 724
        window_y = 600
        window = pygame.display.set_mode((window_x,window_y))
        pygame.display.set_caption("First_Game")
        limit = window_x
        speed = 30
        x = 242
        y = 130
        width = 50
        height = 50
        white = (255,255,255)
        clock = pygame.time.Clock()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        font = pygame.font.SysFont(None, 25)
        run = True
        def blitme(self):
            self.window.blit(self.image, self.rect)
        def write(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,20])
        def write2(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,45])
        def write3(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [20,70])
        def doğru_yaptın(msg,color):
            screen_text = font.render(msg,True,color)
            window.blit(screen_text, [300,100])
        while (run):
            pygame.time.delay(100)
            for user_events in pygame.event.get():
                if user_events.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > speed:  #keyboard
                x = x - speed
            if keys[pygame.K_v] and x > speed:
                x = x - speed    
            if keys[pygame.K_RIGHT] and x < (600 - width - speed): #keyboard
                x = x + speed
            if keys[pygame.K_SPACE] and x < (600 - width - speed):
                x = x + speed    
            if keys[pygame.K_UP] and y > 10: #keyboard
                y = y - speed
            if keys[pygame.K_n] and y > 10:
                y = y - speed    
            if keys[pygame.K_DOWN] and y < (500 - height - speed): #keyboard
                y = y + speed
            if keys[pygame.K_b] and y < (500 - height - speed):
                y = y + speed        
            background = pygame.image.load('Uzay.PNG').convert()
            window.blit(background, [0,0])
            write("Arkadaşın her ay 20 tl biriktiriyor.", red)
            write2("3 ay biriktirdiği parasının yarısını harcarsa geriye kaç tl si kalır?", red)   
            dört = pygame.image.load('30.png')
            dört = pygame.transform.scale(dört,(80,80))
            window.blit(dört, (100,450))
            üç = pygame.image.load('40.png')
            üç = pygame.transform.scale(üç,(80,80))
            window.blit(üç, (300,500))
            doğru = pygame.image.load('doğru.png')
            doğru = pygame.transform.scale(doğru, (50,50))
            beş = pygame.image.load('20.png')
            beş = pygame.transform.scale(beş,(80,80))
            window.blit(beş, (550,450))
            character_1 = pygame.image.load('UFO2.png')
            character_1 = pygame.transform.scale(character_1,(180,180))
            window.blit(character_1, (x,y))
            yanlış = pygame.image.load('çarpı işareti.png')
            yanlış = pygame.transform.scale(yanlış, (50,50))
            answer2 = (((x - 300)** 2)+((y - 500)** 2)**1/2)
            if ((x == 32) and (y == 400) or ((x == 32) and (y == 430))):
                window.blit(doğru, (360, 150))
                doğru_yaptın("Soruyu doğru yaptın :D", red)
            elif (((x == 242) and (y == 400) or ((x == 242) and (y == 430)) or (((x == 272) and (y == 400)) or (((x == 272) and (y == 430))))) or ((x == 482) and (y == 400) or ((x == 512) and (y == 400)) or (((x == 482) and (y == 430)) or (((x == 512) and (y == 430)))))): 
                window.blit(yanlış, (360, 150))
                doğru_yaptın("Tekrar denemelisin", red)  
            pygame.display.update()   
        pygame.quit()
    else:
        print(" ")

#birinci_sınıf_birinci_soru()   #ritmik sayma 1 (en iyi) ss alındı
#birinci_sınıf_birinci_soruX()  #ritmik sayma 2 ss alındı
#birinci_sınıf_birinci_soruXX() #ritmik sayma 3 (zor) ss alındı
        
#birinci_sınıf_ikinci_soru()    #toplama 1 ss alındı 
#birinci_sınıf_ikinci_soruX()   #toplama 2 ss alındı
#birinci_sınıf_ikinci_soruXX()  #toplama 3 ss alındı

#birinci_sınıf_ucuncu_soru()    #çıkarma 1 (elmalı) ss alındı
#birinci_sınıf_ucuncu_soruX()   #çıkarma 2 ss alındı
#birinci_sınıf_ucuncu_soruXX()  #çıkarma 3 ss alındı
        
#birinci_sınıf_dorduncu_soru()  #saat problemi 1 (zor) ss alındı
#birinci_sınıf_dorduncu_soruX() #saat problemi 2 (en iyi) ss alındı
#birinci_sınıf_dorduncu_soruXX()#saat problemi 3 ss alındı
        
birinci_sınıf_besinci_soru()   #örüntü 1 (en iyi) ss alındı
#birinci_sınıf_besinci_soruX()  #geometri 1 ss alındı
#birinci_sınıf_besinci_soruXX() #geometri 2 ss alındı
        
#ikinci_sınıf_birinci_soru()    #çarpma ve çarpma ss alındı
#ikinci_sınıf_birinci_soruX()   #çarpma ve toplama (en iyi) ss alındı
#ikinci_sınıf_birinci_soruXX()  #çarpma ss alındı

#ikinci_sınıf_ikinci_soru()     #bölme ve çıkarma 1 (en iyi) ss alındı
#ikinci_sınıf_ikinci_soruX()    #bölme ve çıkarma 2 ss alındı
#ikinci_sınıf_ikinci_soruXX()   #bölme ve çıkarma 3 ss alındı

#ikinci_sınıf_ucuncu_soru()     #uzunluk hesaplama 1 (en iyi, dolap) ss alındı
#ikinci_sınıf_ucuncu_soruX()    #uzunluk hesaplama 2 ss alındı
#ikinci_sınıf_ucuncu_soruXX()   #uzunluk hesaplama 3 ss alındı
        
#ikinci_sınıf_dorduncu_soru()   #kesirler 1  (zor) ss alındı
#ikinci_sınıf_dorduncu_soruX()  #kesirler 2 (en iyi) ss alındı
#ikinci_sınıf_dorduncu_soruXX() #kesirler 3 ss alındı
        
#ikinci_sınıf_besinci_soru()    #para hesaplama 1 ss alındı
#ikinci_sınıf_besinci_soruX()   #para hesaplama 2 ss alındı
#ikinci_sınıf_besinci_soruXX()  #para hesaplama 3 ss alındı
        
