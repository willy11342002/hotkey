from sticker import Sticker
import pyautogui
import keyboard


def main():
    sticker = Sticker()

    # 監聽快速鍵啟動程式
    keyboard.add_hotkey('ctrl + /', sticker.start)
    keyboard.add_hotkey('space', lambda: print(pyautogui.position()))

    # 監聽上方按鈕切換
    keyboard.add_hotkey('ctrl + 1', sticker.sticker_page)
    keyboard.add_hotkey('ctrl + 2', sticker.emoji_page)
    keyboard.add_hotkey('ctrl + up', lambda: sticker.upper_move('up'))
    keyboard.add_hotkey('ctrl + down', lambda: sticker.upper_move('down'))
    keyboard.add_hotkey('ctrl + left', lambda: sticker.upper_move('left'))
    keyboard.add_hotkey('ctrl + right', lambda: sticker.upper_move('right'))

    # 監聽下方按鈕切換
    keyboard.add_hotkey('tab', sticker.switch_page)
    keyboard.add_hotkey('ctrl + up', lambda: sticker.bottom_move('up'))
    keyboard.add_hotkey('ctrl + down', lambda: sticker.bottom_move('down'))
    keyboard.add_hotkey('ctrl + left', lambda: sticker.bottom_move('left'))
    keyboard.add_hotkey('ctrl + right', lambda: sticker.bottom_move('right'))
    keyboard.add_hotkey('enter', lambda: pyautogui.click() or pyautogui.press('esc'))

    # 開始監聽
    keyboard.wait()


if __name__ == '__main__':
    main()
