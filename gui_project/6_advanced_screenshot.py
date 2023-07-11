# pip install keyboard
import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2023년 7월 11일 15시 38분 30초 -> _20230711_153830
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) #ex) image_20230711_153830.png

keyboard.add_hotkey("F9", screenshot) # F9 키를 누르면 스크린 샷 저장

keyboard.wait("esc") # esc키를 누를 때 까지 위 프로그램 수행