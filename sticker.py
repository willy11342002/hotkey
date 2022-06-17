import pyautogui
import win32gui
import win32con


class Sticker(object):
    '''貼圖、表情貼操作器'''
    mainwindow = win32gui.FindWindow('Qt5152QWindowIcon', 'LINE')
    target_class = 'Qt5152QWindowIcon'
    page = None

    def start(self):
        '''開啟貼圖視窗'''
        hwnd = win32gui.GetForegroundWindow()
        # 檢查LINE主視窗不啟用(需要聊天室窗才啟用)
        if self.get_page_title() != 'Chat':
            return
        # 開啟視窗並最大化
        self.open_sticker_window()
        while True:
            if win32gui.GetForegroundWindow() != hwnd:
                break
        self.maximize_top_window()
        self.emoji_page()

    def get_page_title(self):
        '''讀取最上層視窗，回傳以下內容["Line", "Sticker", "Chat", False]'''
        hwnd = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd).strip()
        cls = win32gui.GetClassName(hwnd)
        if hwnd == self.mainwindow:
            return 'Line'
        elif title == 'LINE':
            return 'Sticker'
        elif cls == self.target_class:
            return 'Chat'
        else:
            return False

    def open_sticker_window(self):
        '''點開貼圖畫面'''
        if self.get_page_title() != 'Chat':
            return
        pyautogui.hotkey('ctrl', 'e')

    def maximize_top_window(self):
        '''最大化最上層視窗'''
        if self.get_page_title() != 'Sticker':
            return

        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        self.to_upper_first()

    def sticker_page(self):
        '''切換到貼圖頁'''
        if self.get_page_title() != 'Sticker':
            return

        pyautogui.moveTo((900, 65))
        pyautogui.click()
        self.to_upper_first()
        self.page = 'sticker'

    def emoji_page(self):
        '''切換到表情貼頁'''
        if self.get_page_title() != 'Sticker':
            return

        pyautogui.moveTo((1015, 65))
        pyautogui.click()
        self.to_upper_first()
        self.page = 'emoji'

    def switch_page(self):
        '''切換選擇上方貼圖集/下方貼圖內容'''
        if self.get_page_title() != 'Sticker':
            return
        
        if pyautogui.position().y >= 400:
            self.to_upper_first()
        else:
            self.to_bottom_first()

    def to_upper_first(self):
        '''滑鼠移動到上方第一個物件'''
        pyautogui.moveTo((44, 140))

    def to_bottom_first(self):
        '''滑鼠移動到下方第一個物件'''
        if self.page == 'sticker':
            pyautogui.moveTo((80, 520))
        else:
            pyautogui.moveTo((75, 480))

    def move_mouse(self, direct):
        '''選擇貼圖/表情貼'''
        if self.get_page_title() != 'Sticker':
            return

        curr_position = pyautogui.position()
        position = [curr_position.x, curr_position.y]
        if curr_position.y <= 400:
            move_speed = 75
        elif self.page == 'emoji':
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

        pyautogui.moveTo(position, _pause=False)
        if curr_position.y <= 400:
            pyautogui.click()

    def send_and_close(self):
        '''發送貼圖並關閉貼圖視窗'''
        if self.get_page_title() != 'Sticker':
            return

        if pyautogui.position().y <= 400:
            return

        pyautogui.click()
        pyautogui.press('esc')
