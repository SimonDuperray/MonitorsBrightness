import screen_brightness_control as sbc, sys

def get_monitors():
   return len(sbc.list_monitors())

def set_bright():
   value = int(sys.argv[1])
   if value>=0 and value<=100:
      for i in range(get_monitors()):
         sbc.set_brightness(value=int(sys.argv[1]), display=i)
   else:
      print("[Error] Brightness value must be between 0 and 100")

set_bright()