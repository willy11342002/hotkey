from sticker import Sticker
import keyboard
import win32gui
import win32con
import time


sticker = Sticker()
time.sleep(3)
sticker.open_sticker_window()
time.sleep(1)
sticker.maximize_top_window()
time.sleep(1)
sticker.shot_top_window()

# while True:
#     try:
#         position = pyautogui.locateOnScreen('icons/test.png', confidence=0.7)
#         position = pyautogui.center(position)
#         print(position)
#         break
#     except TypeError as e:
#         continue

# time.sleep(2)

# hwnd = win32gui.FindWindow(None, '宗錦')

# window_rect = win32gui.GetWindowRect(window_handle)
# print(window_rect)

# def main():
#     keyboard.add_hotkey('windows + z', sticker.open_sticker_window)
#     keyboard.wait()


# if __name__ == '__main__':
#     main()
