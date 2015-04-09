import pyglet
import random

from game import gameover
from game import gumb
from game import highScores
from game import menu
from game import meteor
from game import powerup
from game import raketa
from game import resources
from game.screen import *


class Game:
    def start(self):
        self.stevec = 0
        self.highScores = highScores.HighScores(self)

        # ozadje
        self.bg = pyglet.sprite.Sprite(
            resources.BG,
            x=0,
            y=0,
        )

        # LHE pred začetkom
        self.LHE = pyglet.sprite.Sprite(
            resources.LHE,
            x=-25,
            y=0,
        )
        self.LHE.opacity = 0

        # trajanje timerja za LightHex Entertaintment na začetku
        # !!! sam zacasno, pol dej timerbase na 5 !!!
        self.LHE_timerbase = 5
        self.LHE_timer = self.LHE_timerbase

        # trajanje timerja za use powerupe in powerdowne
        self.pu_timerbase = 7
        self.freeze_timer = self.pu_timerbase
        self.shield_timer = self.pu_timerbase
        self.Hmetki_timer = self.pu_timerbase
        self.strel_timer = self.pu_timerbase
        self.speed_timer = self.pu_timerbase
        self.Pmetki_timer = self.pu_timerbase
        self.slow_timer = self.pu_timerbase
        # self.Hmeteorji_timer = self.pu_timerbase

        self.dodaj_timerbase = 1
        self.dodaj_timer = self.dodaj_timerbase
        self.dodaj_scale = 0.997
        self.meteorji_list = []
        self.powerup_list = []
        self.metek_list = []
        self.main_batch = pyglet.graphics.Batch()
        self.menuStart_list = []
        self.menuStart = menu.Menu()

        napis = pyglet.text.Label(
            text="ime",
            font_size=50,
            x=250,
            y=500,
            bold=True,
            color=(250, 250, 0, 255),
            anchor_x="center",
        )
        napis.rotation = 50
        self.menuStart.labels.append(napis)
        tmp = resources.GN
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menuStart.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Start",
                batch=self.menuStart.buttonsBatch,
                x=window.width/2,
                y=window.height/2,
            )
        )
        self.menuStart.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="High Scores",
                batch=self.menuStart.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 80,
            )
        )
        self.menuStart.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Options",
                batch=self.menuStart.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 160,
            )
        )
        self.menuStart.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name='Exit',
                batch=self.menuStart.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 240))

        for i in self.menuStart.buttons[:]:
            napis = pyglet.text.Label(
                text=i.name,
                font_size=20,
                x=i.x,
                y=i.y,
                bold=True,
                color=(250, 250, 0, 150),
                anchor_x='center',
                anchor_y='center',
            )
            self.menuStart.labels.append(napis)

        """HIGH SCORES MENU"""
        self.menuHighScores = menu.Menu()
        napis = pyglet.text.Label(
            text="High Scores",
            font_size=50,
            x=50,
            y=500,
            bold=True,
            color=(250, 250, 0, 255),
        )
        napis.rotation = 50
        self.menuHighScores.labels.append(napis)
        for i in self.highScores.getScores():
            self.menuHighScores.labels.append(i)
        tmp = resources.GN
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menuHighScores.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Main Menu",
                batch=self.menuHighScores.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 240,
            )
        )
        for i in self.menuHighScores.buttons[:]:
            napis = pyglet.text.Label(
                text=i.name,
                font_size=20,
                x=i.x,
                y=i.y,
                bold=True,
                color=(250, 250, 0, 150),
                anchor_x="center",
                anchor_y="center")
            self.menuHighScores.labels.append(napis)

        # options menu
        self.menuOptions = menu.Menu()
        napis = pyglet.text.Label(
            text="Options",
            font_size=50,
            x=120,
            y=500,
            bold=True,
            color=(250, 250, 0, 255)
            )
        napis.rotation = 50
        self.menuOptions.labels.append(napis)
        tmp1 = resources.GNp
        tmp1.anchor_x = tmp1.width/2
        tmp1.anchor_y = tmp1.height/2
        self.menuOptions.buttons.append(
            gumb.Gumb(
                self,
                tmp1,
                name="Hangar",
                batch=self.menuOptions.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 80))
        self.menuOptions.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Instructions",
                batch=self.menuOptions.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 160))
        self.menuOptions.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Main Menu",
                batch=self.menuOptions.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 240))

        for i in self.menuOptions.buttons[:]:

            napis = pyglet.text.Label(
                text=i.name,
                font_size=20,
                x=i.x,
                y=i.y,
                bold=True,
                color=(250, 250, 0, 150),
                anchor_x="center",
                anchor_y="center"
            )
            self.menuOptions.labels.append(napis)

        self.menuPause = menu.Menu()
        napis = pyglet.text.Label(
            text="Pause",
            font_size=50,
            x=150,
            y=500,
            bold=True,
            color=(250, 250, 0, 255)
        )
        napis.rotation = 50
        self.menuPause.labels.append(napis)
        tmp = resources.GN
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menuPause.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Resume",
                batch=self.menuPause.buttonsBatch,
                x=window.width/2,
                y=window.height/2))
        self.menuPause.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Restart",
                batch=self.menuPause.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 80
            )
        )
        self.menuPause.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Main Menu",
                batch=self.menuPause.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 160
            )
        )
        for i in self.menuPause.buttons[:]:
            napis = pyglet.text.Label(
                text=i.name,
                font_size=20,
                x=i.x,
                y=i.y,
                bold=True,
                color=(250, 250, 0, 150),
                anchor_x="center",
                anchor_y="center",
            )
            self.menuPause.labels.append(napis)
        self.nastavi_raketo()

    def nastavi_raketo(self):
        if gameover.raketa == 1:
            self.slika = resources.raketa1
            self.slika_metek = resources.bull1
        else:
            self.slika = resources.raketa2
            self.slika_metek = resources.bull2

        self.raketa = raketa.Raketa(self, self.slika, batch=self.main_batch)
        window.push_handlers(self.raketa.key_handler)

    def myInit(self):
        self.metki = False
        self.vy_base_max = -350
        self.vy_base = -150
        self.vy_scale = 1.005
        self.hp = 2

        self.dol = 0
        gameover.start = False
        self.main_batch = pyglet.graphics.Batch()
        self.meteorji_list = []
        self.metek_list = []
        self.menuEnd_list = []
        self.menuPause_list = []

        self.menuEnd = menu.Menu()
        napis = pyglet.text.Label(
            text="Game over",
            font_size=45,
            x=250,
            y=550,
            bold=True,
            color=(250, 250, 0, 255),
            anchor_x="center",
            anchor_y="center",
            )
        napis.rotation = 50
        self.menuEnd.labels.append(napis)
        for i in self.highScores.getScores():
            self.menuEnd.labels.append(i)
        tmp = resources.GNp
        tmp.anchor_x = tmp.width/2
        tmp.anchor_y = tmp.height/2
        self.menuEnd.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Retry",
                batch=self.menuEnd.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 160,
            )
        )
        self.menuEnd.buttons.append(
            gumb.Gumb(
                self,
                tmp,
                name="Main Menu",
                batch=self.menuEnd.buttonsBatch,
                x=window.width/2,
                y=window.height/2 - 240,
            )
        )
        for i in self.menuEnd.buttons[:]:
            napis = pyglet.text.Label(
                text=i.name,
                font_size=20,
                x=i.x,
                y=i.y,
                bold=True,
                color=(250, 250, 0, 150),
                anchor_x="center",
                anchor_y="center",
            )
            self.menuEnd.labels.append(napis)

        self.nastavi_raketo()

        gameover.game_over = False
        gameover.freeze = False
        gameover.shield = False
        gameover.Hmetki = False
        gameover.strel = False
        gameover.speed = False
        gameover.Pmetki = False
        gameover.slow = False

        self.score = 0
        self.score_label = pyglet.text.Label(
            text=str(self.score),
            font_size=30,
            x=0,
            y=0,
            bold=True,
            color=(250, 250, 0, 255),
        )
        self.score_timer = 1

        self.life_raketa = pyglet.sprite.Sprite(
            resources.raketa1,
            x=500,
            y=0,
        )
        self.life_raketa.scale = 0.5

    def __init__(self):
        self.start()

    def fade(self):
        if self.LHE.opacity < 255:
            self.LHE.opacity += 1

    def draw(self):
        if (not gameover.hiScores and
                not gameover.game_over and
                not gameover.start and
                not gameover.pause and
                not gameover.options and
                not gameover.LHEstart):
            self.main_batch.draw()
            self.score_label.draw()
            self.life_raketa.x = 500
            for i in range(0, self.hp):
                self.life_raketa.x -= 50 * self.life_raketa.scale
                self.life_raketa.draw()
        elif gameover.LHEstart:
            self.LHE.draw()
        else:
            self.bg.draw()
            if gameover.options:
                self.menuOptions.draw()
                for e in self.menuOptions.labels[:]:
                    e.draw()
            elif gameover.start:
                self.menuStart.draw()
                for e in self.menuStart.labels[:]:
                    e.draw()
            elif gameover.pause:
                self.menuPause.draw()
                for e in self.menuPause.labels[:]:
                    e.draw()
            elif gameover.hiScores:
                self.menuHighScores.draw()
                for e in self.menuHighScores.labels[:]:
                    e.draw()
            elif gameover.game_over:
                self.menuEnd.draw()
                for e in self.menuEnd.labels[:]:
                    e.draw()

    def mouse_press(self, x, y):
        if(gameover.options):
            self.menuOptions.preveriKlike(x, y)
        elif(gameover.start):
            self.menuStart.preveriKlike(x, y)
        elif(gameover.game_over):
            self.menuEnd.preveriKlike(x, y)
        elif(gameover.pause):
            self.menuPause.preveriKlike(x, y)
        elif(gameover.hiScores):
            self.menuHighScores.preveriKlike(x, y)

    def check_menu_hover(self, menu, x, y):
        for i in menu.buttons[:]:
            if(x >= i.x-i.width/2 and
                x <= i.width/2+i.x and
                y >= i.y-i.height/2 and
               y <= i.height/2+i.y):
                if(i.hover is False):
                    i.hover = True
                    menu.sprememba = True
                break
            else:
                if(i.hover is True):
                    i.hover = False
                    menu.sprememba = True

    def mouse_motion(self, x, y, dx, dy):
        if(gameover.start):
            self.check_menu_hover(self.menuStart, x, y)
        if(gameover.pause):
            self.check_menu_hover(self.menuPause, x, y)
        if(gameover.game_over):
            self.check_menu_hover(self.menuEnd, x, y)
        if(gameover.hiScores):
            self.check_menu_hover(self.menuHighScores, x, y)
        if(gameover.options):
            self.check_menu_hover(self.menuOptions, x, y)

    def update(self, dt):
        if(not gameover.game_over and
           not gameover.start and
           not gameover.afterPause and
           not gameover.pause and
           not gameover.options and
           not gameover.hiScores and
           not gameover.LHEstart):
            # window.set_exclusive_mouse()
            self.raketa.update(dt)
            for d in self.raketa.dodatki[:]:
                d.x = self.raketa.x
                d.y = self.raketa.y
            for p in self.powerup_list[:]:
                p.update(dt)
            for i in self.metek_list[:]:
                i.update(dt)
            for m in self.meteorji_list[:]:
                for i in self.metek_list[:]:
                    m.collision(i)
            for p in self.powerup_list[:]:
                    p.collision(self.raketa)
            if(not gameover.freeze):
                self.dodaj_timer -= dt
                while(self.dodaj_timer <= 0):
                    if(self.dodaj_timerbase < 0.01):
                        self.dodaj()
                        self.dodaj_timer += 0.01
                    else:
                        self.dodaj()
                        self.dodaj_timerbase *= self.dodaj_scale
                        self.dodaj_timer += self.dodaj_timerbase
                self.scorePU = self.score/300
                if self.scorePU > self.stevec:
                    self.stevec += 1
                    self.dodajPU()
                for m in self.meteorji_list[:]:
                    m.update(dt)
                for m in self.meteorji_list[:]:
                    m.collision(self.raketa)
            else:
                self.freeze_timer -= dt
                # freeze timer
                if(self.freeze_timer <= 0):
                    gameover.freeze = False
                    self.freeze_timer = self.pu_timerbase
            # shield timer
            if gameover.shield:
                self.shield_timer -= dt
                if(self.shield_timer <= 0):
                    scit_index = self.raketa.dodatki.index(self.raketa.scit)
                    self.raketa.dodatki[scit_index].delete()
                    self.raketa.dodatki.pop(scit_index)
                    gameover.shield = False
                    self.shield_timer = self.pu_timerbase

            # Hmetki timer
            if gameover.Hmetki:
                self.Hmetki_timer -= dt
                if(self.Hmetki_timer <= 0):
                    gameover.Hmetki = False
                    self.Hmetki_timer = self.pu_timerbase
                    self.raketa.timer_base = 1/5
            # speed timer
            if gameover.speed:
                self.speed_timer -= dt
                if(self.speed_timer <= 0):
                    gameover.speed = False
                    self.speed_timer = self.pu_timerbase
                    self.raketa.vx = 200
            # strel timer
            if gameover.strel:
                self.strel_timer -= dt
                if(self.strel_timer <= 0):
                    gameover.strel = False
                    self.strel_timer = self.pu_timerbase
                    self.metki = False
            # Pmetki timer
            if gameover.Pmetki:
                self.Pmetki_timer -= dt
                if(self.Pmetki_timer <= 0):
                    gameover.Pmetki = False
                    self.Pmetki_timer = self.pu_timerbase
                    self.raketa.timer_base = 1/5
            # slow timer
            if gameover.slow:
                self.slow_timer -= dt
                if(self.slow_timer <= 0):
                    gameover.slow = False
                    self.slow_timer = self.pu_timerbase
                    self.raketa.vx = 200

            self.score_label.text = str(self.score)
            self.score_timerbase = 1
            if(self.score_timer > 0):
                self.score_timer -= dt
            else:
                self.score_timer = self.score_timerbase
                self.score += 10

        else:
            window.set_exclusive_mouse(exclusive=False)
            self.dodaj_timerbase = 1
            self.dodaj_timer = self.dodaj_timerbase
            if(gameover.pause):
                gameover.timer = gameover.baseTimer
            elif(gameover.afterPause):
                gameover.timer -= dt
                if(gameover.timer <= 0):
                    gameover.afterPause = False
        # printa score
        if(gameover.game_over):
            napis = pyglet.text.Label(
                text=str(self.score),
                font_size=30,
                x=250,
                y=500,
                bold=True,
                color=(250, 250, 0, 150),
                anchor_x="center",
                anchor_y="center",
            )
            self.menuEnd.labels.append(napis)

        # LHE start timer
        if gameover.LHEstart:
            self.fade()
            self.LHE_timer -= dt
            if(self.LHE_timer <= 0):
                gameover.LHEstart = False
                self.LHE_timer = self.LHE_timerbase
                gameover.start = True

    def dodaj(self):

        x = random.randint(0, 2)
        if(x == 1):
            tmp = meteor.Meteor(
                self,
                resources.meteor2,
                batch=self.main_batch,
            )
            tmp.velikost = "v"
            tmp.x = random.randint(0, window.width-tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            self.meteorji_list.append(tmp)
        if(x == 2):
            tmp = meteor.Meteor(self, resources.meteor1, batch=self.main_batch)
            tmp.velikost = "m"
            tmp.x = random.randint(0, window.width-tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            self.meteorji_list.append(tmp)

        p = random.randint(0, 10000)
        if(p >= 116 and p <= 120):
            tmp = powerup.Powerup(self,
                                  img=resources.pu1,
                                  power="xLife",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
        elif(p >= 916 and p <= 920):
            tmp = powerup.Powerup(self,
                                  img=resources.pu2,
                                  power="Bomb",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
        elif(p >= 516 and p <= 520):
            tmp = powerup.Powerup(self,
                                  img=resources.metki,
                                  power="Strel",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
        elif(p >= 716 and p <= 720):
            tmp = powerup.Powerup(self,
                                  img=resources.speed,
                                  power="Speed",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
        elif(p >= 316 and p <= 320):
            tmp = powerup.Powerup(self,
                                  img=resources.Hmetki,
                                  power="Hmetki",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)

        elif(p >= 400 and p <= 401):
            tmp = powerup.Powerup(self,
                                  img=resources.Freeze,
                                  power="Freeze",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)

        elif(p >= 216 and p <= 220):
            tmp = powerup.Powerup(self,
                                  img=resources.Shield,
                                  power="Shield",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            self.powerup_list.append(tmp)

        elif(p >= 251 and p <= 275):
            tmp = powerup.Powerup(self,
                                  img=resources.Pmetki,
                                  power="Pmetki",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)

        elif(p >= 51 and p <= 75):
            tmp = powerup.Powerup(self,
                                  img=resources.slow,
                                  power="slow",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)

        elif(p >= 151 and p <= 175):
            tmp = powerup.Powerup(self,
                                  img=resources.Hmeteorji,
                                  power="Hmeteorji",
                                  batch=self.main_batch,
                                  )
            tmp.x = random.randint(0, window.width - tmp.width)
            tmp.y = window.height
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)

    def dodajPU(self, x=random.randint(0, window.width - 32), y=window.height):
        p = random.randint(0, 100)
        if(p >= 26 and p <= 37):
            tmp = powerup.Powerup(self,
                                  img=resources.pu1,
                                  power="xLife",
                                  batch=self.main_batch,
                                  )
            tmp.x = x
            tmp.y = y
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
        elif(p >= 51 and p <= 65):
            tmp = powerup.Powerup(self,
                                  img=resources.metki,
                                  power="Strel",
                                  batch=self.main_batch,
                                  )
            tmp.x = x
            tmp.y = y
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
        elif(p >= 66 and p <= 80):
            tmp = powerup.Powerup(self,
                                  img=resources.speed,
                                  power="Speed",
                                  batch=self.main_batch,
                                  )
            tmp.x = x
            tmp.y = y
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
        elif(p >= 81 and p <= 95):
            tmp = powerup.Powerup(self,
                                  img=resources.Hmetki,
                                  power="Hmetki",
                                  batch=self.main_batch,
                                  )
            tmp.x = x
            tmp.y = y
            tmp.vy = self.vy_base + random.randint(-50, 50)
            self.vy_base = self.vy_base*self.vy_scale
            if(self.vy_base < self.vy_base_max):
                self.vy_base = self.vy_base_max
                self.vy_scale = 1
            # print(tmp.vy)
            self.powerup_list.append(tmp)
