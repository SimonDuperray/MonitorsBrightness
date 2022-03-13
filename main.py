import screen_brightness_control as sbc

def set_middle():
   for i in range(3):
      sbc.set_brightness(value=50, display=i)


def set_full():
   for i in range(3):
      sbc.set_brightness(value=100, display=i)


set_middle()
# set_full()