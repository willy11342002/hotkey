from sticker import Sticker
import pyautogui
import keyboard


def main():
    sticker = Sticker()

    # 監聽快速鍵啟動程式
    keyboard.add_hotkey('ctrl + /', sticker.start)
    keyboard.add_hotkey('space', lambda: print(pyautogui.position()))
    keyboard.add_hotkey('f2', sticker.sticker_page)
    keyboard.add_hotkey('f3', sticker.emoji_page)
    keyboard.add_hotkey('tab', sticker.switch_page)
    keyboard.add_hotkey('enter', sticker.send_and_close)

    # 監聽選擇貼圖
    keyboard.add_hotkey('up', lambda: sticker.move_mouse('up'))
    keyboard.add_hotkey('down', lambda: sticker.move_mouse('down'))
    keyboard.add_hotkey('left', lambda: sticker.move_mouse('left'))
    keyboard.add_hotkey('right', lambda: sticker.move_mouse('right'))

    # 開始監聽
    keyboard.wait()


if __name__ == '__main__':
    main()
