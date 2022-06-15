import pyautogui
import win32gui
import win32con


class Sticker(object):
    '''貼圖、表情貼操作器'''

    def open_sticker_window(self):
        '''點開貼圖畫面'''
        with pyautogui.hold('ctrl'):
            pyautogui.press('e')

    def maximize_top_window(self):
        '''最大化最上層視窗'''
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

    def shot_top_window(self):
        '''截圖最上層視窗'''
        hwnd = win32gui.GetForegroundWindow()
        region = list(win32gui.GetWindowRect(hwnd))
        region[2] -= region[0]
        region[3] -= region[1]
        img = pyautogui.screenshot(region=region)
        img.save('dummy.png')
        return img

