from utils.pykeyboard import HotkeyListener
from utils.pysystray import SysTray
from sticker import Sticker
import pyautogui
pyautogui.FAILSAFE = False


class App(object):
    def __init__(self):
        self.sticker = Sticker()
        self.tray = SysTray('快速鍵小工具', [
            {
                'title': '中鍵',
                'activate': self.middle_activate,
                'deactivate': self.middle_deactivate,
            },
            {
                'title': 'LINE',
                'activate': self.line_activate,
                'deactivate': self.line_deactivate,
            },
        ])


    # 監聽中鍵快速鍵
    def middle_activate(self):
        self.middle_hotkey = HotkeyListener({
            'win + alt': pyautogui.middleClick
        })
        self.middle_hotkey.start()
    def middle_deactivate(self):
        self.middle_hotkey.stop()

    # 監聽LINE貼圖快速鍵
    def line_activate(self):
        self.line_hotkey = HotkeyListener({
            # 監聽快速鍵啟動程式
            'ctrl + /': self.sticker.start,
            'space': lambda: print(pyautogui.position()),
            'f2': self.sticker.sticker_page,
            'f3': self.sticker.emoji_page,
            'tab': self.sticker.switch_page,
            'enter': self.sticker.send_and_close,

            # 監聽選擇貼圖
            'up': lambda: self.sticker.move_mouse('up'),
            'down': lambda: self.sticker.move_mouse('down'),
            'left': lambda: self.sticker.move_mouse('left'),
            'right': lambda: self.sticker.move_mouse('right'),
        })
        self.line_hotkey.start()
    def line_deactivate(self):
        self.line_hotkey.stop()

    def run(self):
        '''主要進入點'''
        self.tray.run()


if __name__ == '__main__':
    app = App()
    app.run()
