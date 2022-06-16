import pyautogui
import win32gui
import win32con
import time


class Sticker(object):
    '''貼圖、表情貼操作器'''
    mainwindow = win32gui.FindWindow('Qt5152QWindowIcon', 'LINE')
    target_class = 'Qt5152QWindowIcon'
    page = None

    def start(self):
        '''開啟貼圖視窗'''
        # 檢查LINE主視窗不啟用(需要聊天室窗才啟用)
        hwnd = win32gui.GetForegroundWindow()
        if hwnd == self.mainwindow:
            return
        # 開啟視窗並最大化
        self.open_sticker_window()
        while True:
            if win32gui.GetForegroundWindow() != hwnd:
                break
        self.maximize_top_window()
        self.emoji_page()

    def check_window_is_line(self):
        '''檢查是否是LINE相關的視窗'''
        hwnd = win32gui.GetForegroundWindow()
        cls = win32gui.GetClassName(hwnd)
        return cls == self.target_class

    def open_sticker_window(self):
        '''點開貼圖畫面'''
        if not self.check_window_is_line():
            return

        with pyautogui.hold('ctrl'):
            pyautogui.press('e')

    def maximize_top_window(self):
        '''最大化最上層視窗'''
        if not self.check_window_is_line():
            return

        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        self.to_upper_first()

    def shot_top_window(self):
        '''截圖最上層視窗'''
        if not self.check_window_is_line():
            return

        hwnd = win32gui.GetForegroundWindow()
        region = list(win32gui.GetWindowRect(hwnd))
        region[2] -= region[0]
        region[3] -= region[1]
        img = pyautogui.screenshot(region=region)
        img.save('dummy.png')
        return img

    def sticker_page(self):
        '''切換到貼圖頁'''
        if not self.check_window_is_line():
            return

        pyautogui.moveTo((900, 65))
        pyautogui.click()
        self.to_upper_first()
        self.page = 'sticker'

    def emoji_page(self):
        '''切換到表情貼頁'''
        if not self.check_window_is_line():
            return

        pyautogui.moveTo((1015, 65))
        pyautogui.click()
        self.to_upper_first()
        self.page = 'emoji'

    def switch_page(self):
        if not self.check_window_is_line():
            return
        
        if pyautogui.position().y >= 400:
            self.to_upper_first()
        else:
            self.to_bottom_first()

    def to_upper_first(self):
        pyautogui.moveTo((44, 140))

    def to_bottom_first(self):
        if self.page == 'sticker':
            pyautogui.moveTo((80, 520))
        else:
            pyautogui.moveTo((75, 480))

    def upper_move(self, direct):
        '''選擇上方貼圖/表情貼'''
        if not self.check_window_is_line():
            return

        curr_position = pyautogui.position()
        position = [curr_position.x, curr_position.y]
        move_speed = 75
        if direct == 'up':
            position[1] -= move_speed
        elif direct == 'down':
            position[1] += move_speed
        elif direct == 'left':
            position[0] -= move_speed
        elif direct == 'right':
            position[0] += move_speed
        else:
            return

        if position[0] <= 40:
            return
        if position[0] >= pyautogui.size()[0] - 40:
            return
        if position[1] >= 400:
            return

        pyautogui.moveTo(position, _pause=False)
        pyautogui.click()

    def bottom_move(self, direct):
        if not self.check_window_is_line():
            return

        curr_position = pyautogui.position()
        position = [curr_position.x, curr_position.y]
        if self.page == 'emoji':
            move_speed = 96
        else:
            move_speed = 175

        if direct == 'up':
            position[1] -= move_speed
        elif direct == 'down':
            position[1] += move_speed
        elif direct == 'left':
            position[0] -= move_speed
        elif direct == 'right':
            position[0] += move_speed
        else:
            return

        if position[0] <= 40:
            return
        if position[0] >= pyautogui.size()[0] - 40:
            return
        if position[1] <= 400:
            return

        pyautogui.moveTo(position, _pause=False)

    def send_and_close(self):
        if not self.check_window_is_line():
            return

        if pyautogui.position().y <= 400:
            return

        pyautogui.click()
        pyautogui.press('esc')
