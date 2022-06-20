import threading
import keyboard
import utils
import time


class Hotkey(threading.Thread):
    def __init__(self, hotkeys={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cf = utils.Dict.load_yaml('config.yaml')
        self.running = True
        self.hotkeys = hotkeys

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            for keys, func in self.hotkeys.items():
                if keyboard.is_pressed(keys):
                    func()
            time.sleep(self.cf.SLEEP_TIME)
