import pyglet
from .screen import *
from . import gameover


class Gumb(pyglet.sprite.Sprite):
    def __init__(self, game, *args, name="Gumb", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.game = game
        self.hover = False

    def klik(self, x, y):
        if(self.x - self.width/2 <= x and self.x+self.width/2 >= x and self.y - self.height/2 <= y and self.y+self.height/2 >= y):
            if(self.name == "Exit"):
                window.close()
            elif(self.name == "Retry"):
                self.game.myInit()
            elif(self.name == "Main Menu"):
                self.game.start()
                gameover.pause = False
                gameover.options = False
                gameover.hiScores = False
                gameover.start = True
            elif(self.name == "Start"):
                self.game.myInit()
            elif(self.name == "Restart"):
                self.game.myInit()
                gameover.pause = False
            elif(self.name == "Resume"):
                gameover.pause = False
                gameover.afterPause = True
            elif(self.name == "Options"):
                gameover.start = False
                gameover.options = True
            elif(self.name == "Chose1"):
                self.game.slika = resources.raketa1
                self.slika_metek = resources.bull1
            elif(self.name == "Chose2"):
                print("raketa2")
                self.game.slika = resources.raketa2
                self.slika_metek = resources.bull2
            elif(self.name == "High Scores"):
                gameover.hiScores = True
                gameover.start = False
                self.game.draw()
            return(True)
        else:
            return(False)
