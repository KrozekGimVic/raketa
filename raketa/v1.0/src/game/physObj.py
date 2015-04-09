from game import gameover
from game.object import Object


class PhysObj(Object):
    def __init__(self, game, *args, **kwargs):
        super().__init__(game, *args, **kwargs)
        self.zabit = False

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        a = (self.width/2+other.width/2)**2
        b = (self.y+self.height/2-other.y-other.height/2)**2
        b += (self.x+self.width/2-other.x-other.width/2)**2
        if (a >= b):
            other.zabij()
            self.zabij()

    def zabij(self):
        if(self.tip == "Raketa"):
            if not gameover.shield:
                self.life()
            else:
                gameover.shield_zadet = True
                self.game.shield_hit_timer = self.game.shield_hit_timerbase
        else:
            self.brisanje()
            self.zabit = True
