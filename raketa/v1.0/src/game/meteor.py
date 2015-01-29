from random import randint

from game import resources
from game.physObj import PhysObj


class Meteor(PhysObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tip = "Meteor"

    def update(self, dt):
        super().update(dt)

    def collision(self, other):
        super().collision(other)

    def zabij(self):
        if self.velikost == "v":
            x = randint(1, 100)
            if x < 20:
                self.split()
            if x == 99:
                self.split(True)

        super().zabij()
        if self.game.raketa.zabit:
            self.game.meteorji_list = []

        #Za score.
        if not self.game.raketa.zabit:
            if self.zabit and self.velikost == "m":
                self.game.score += 20
            elif self.zabit and self.velikost == "v":
                self.game.score += 30
        self.game.raketa.zabit = False

    def split(self, x=False):
        if x:
            pass
        else:
            for i in range(2):
                tmp = Meteor(
                    self.game,
                    resources.meteor1,
                    batch=self.game.main_batch
                )
                tmp.velikost = "m"
                tmp.y = self.y + (2 - i) * 30
                tmp.x = self.x + (i - 1) * 30
                tmp.vy = self.vy
                self.game.meteorji_list.append(tmp)
