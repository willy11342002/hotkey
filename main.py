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

    # 監聽上方按鈕切換
    keyboard.add_hotkey('shift + up', lambda: sticker.upper_move('up'))
    keyboard.add_hotkey('shift + down', lambda: sticker.upper_move('down'))
    keyboard.add_hotkey('shift + left', lambda: sticker.upper_move('left'))
    keyboard.add_hotkey('shift + right', lambda: sticker.upper_move('right'))

    # 監聽下方按鈕切換
    keyboard.add_hotkey('shift + up', lambda: sticker.bottom_move('up'))
    keyboard.add_hotkey('shift + down', lambda: sticker.bottom_move('down'))
    keyboard.add_hotkey('shift + left', lambda: sticker.bottom_move('left'))
    keyboard.add_hotkey('shift + right', lambda: sticker.bottom_move('right'))

    # 開始監聽
    keyboard.wait()


if __name__ == '__main__':
    main()
