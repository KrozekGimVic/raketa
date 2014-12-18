import pyglet
import os, errno


class HighScores:

    def __init__(self, game):
        self.game = game

    def getScores(self):
        try:
            with open("highScores.txt", "r") as f:
                i = 0
                self.scores = []
                for vrstica in f.readlines():
                    i += 1
                    ime, tocke = vrstica.split()
                    lala = ime
                    if len(ime) > 15:
                        lala = ime[0:15]
                    ime = '{0}. {1}'.format(i, lala)
                    self.scores.append(
                        pyglet.text.Label(
                            text=ime,
                            font_size=15,
                            bold=True,
                            x=25,
                            y=430-25*i,
                            color=(250, 250, 0, 255),
                        )
                    )
                    self.scores.append(
                        pyglet.text.Label(
                            text='. . . . . . . . .',
                            font_size=15,
                            bold=True,
                            x=230,
                            y=430-25*i,
                            color=(250, 250, 0, 255),
                        )
                    )
                    self.scores.append(
                        pyglet.text.Label(
                            text=tocke,
                            font_size=15,
                            bold=True,
                            x=350,
                            y=430-25*i,
                            color=(250, 250, 0, 255),
                        )
                    )
        except FileNotFoundError:
            with open("highScores.txt", "w") as f:
                pass
            self.getScores()
        return self.scores

    def enterName(self):
        pass
        """with open("highScores.txt", "r") as f:
            self.hScores=[]
            x=True
            for i in f.readlines():
                ime, tocke=i.split()
                if int(tocke)<self.game.score and x:
                    self.hScores.append(["_", str(self.game.score)])
                    x=False
                self.hScores.append([ime, str(tocke)])
            y=self.hScores[0:10]
            self.hScores=y
        try:
            os.remove("highScores.txt")
        except OSError:
            pass
        with open("highScores.txt", "a") as f:
            f.write('\n'.join(' '.join(y) for y in self.hScores))
"""
