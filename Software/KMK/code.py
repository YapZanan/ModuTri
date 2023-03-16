import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
keyboard = KMKKeyboard()

layers = Layers()
tapdance = TapDance()

keyboard.modules = [layers, tapdance]

keyboard.col_pins = (board.GP4,)
keyboard.row_pins = (board.GP23, board.GP26, board.GP17,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB
rgb_ext = RGB(pixel_pin = board.GP0, num_pixels=4, hue_default=100)
keyboard.extensions.append(rgb_ext)

# Layers
Layer_Normal, Layer_Funct = 0, 1

To_Normal = KC.DF(Layer_Normal)
To_Funct = KC.MO(Layer_Funct)

  # NORMAL LAYER
  # .------.
  # |  FN  | --> Holding FN will activate the Function Layer
  # |------|
  # |   B  |
  # |------|
  # |   C  |
  # |------|

keyboard.keymap = [
    [To_Funct,
     KC.B,
     KC.C,],

    [KC.D,
     KC.E,
     KC.F,],
]

if __name__ == '__main__':
    keyboard.go()