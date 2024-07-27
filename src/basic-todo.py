# coding utf-8

import customtkinter as ctk
import configparser as cfg
import platform
import os

#__Author__: bssdka
#__License__: BSD 2-Clause License

# -----GLOBAL VARIABLES-----
__path__ = os.getcwd()
__system__ = platform.system()
print(__system__)

# -----READ BASIC.INI-----
config = cfg.ConfigParser()
config.read(f'{__path__}/config/basic.ini')
meta = config['DEFAULT']
debug = config['DEBUGGING']
widgets = config['widget.SIZES']

class MainWindow(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__()
        # Configuration appearance mode
        # ctk.set_appearance_mode('system')
        ctk.set_appearance_mode(debug['debug_appearance_mode'])

        self.initUI()
    def initUI(self):
        pass



# -----LAUNCH APPLICATION-----
if __name__ == '__main__':
    app = MainWindow()

    # -----CONFIGURATION APP-----
    app.configure(width=meta['width'], height=meta['height'])
    app.title(f'{meta['title']} {meta['version']}')

    app.mainloop()