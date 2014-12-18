import pyglet

from game.seznami import *
from game.igra import *
from game.screen import *


@window.event
def on_draw():
    window.clear()
    play.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    play.mouse_press(x, y)


@window.event
def on_mouse_motion(x, y, dx, dy):
    play.mouse_motion(x, y, dx, dy)


def update(dt):
    play.update(dt)


def dodaj(dt):
    play.dodaj()


if(__name__ == '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
