from sticker import Sticker
from hotkey import Hotkey
from tray import SysTray
import pyautogui
pyautogui.FAILSAFE = False


class App(object):
    def __init__(self):
        self.state = True
        self.sticker = Sticker()
        self.tray = SysTray(
            title='LINE貼圖操作小工具',
            state=self.state,
            activate=self.activate,
            deactivate=self.deactivate
        )

        self.dic_hotkey = {
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
        }

    def activate(self):
        '''開始監聽程式'''
        self.hotkey = Hotkey(self.dic_hotkey)
        self.hotkey.start()

    def deactivate(self):
        '''暫停監聽程式'''
        self.hotkey.stop()

    def run(self):
        '''主要進入點'''
        self.tray.run()


if __name__ == '__main__':
    app = App()
    app.run()
