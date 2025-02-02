# coding utf-8

import customtkinter as ctk
import configparser as cfg
import platform
import os

# Import functions of your code
from functions import swap, settings


# -----GLOBAL VARIABLES-----
__path__ = os.getcwd()
__system__ = platform.system()

# -----READ BASIC.INI-----
config = cfg.ConfigParser()
config.read(f'{__path__}/config/basic.ini')
meta = config['DEFAULT']
theme = config['system.THEME']
font = config['FONT']
__theme__ = meta['theme'] # global variable

# -----REFER TO OUR FUNCTIONS-----
settings_image = swap.image_swap()


class MainWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f'{meta['width']}x{meta['height']}')
        self.__font__ = ctk.CTkFont(family=font['family'], size=int(font['size']), weight=font['weight'])

        self.initUI()
    def initUI(self):

        # -----CREATINGE AND POSITIONING WIDGETS-----
        create_node_btn = ctk.CTkButton(self, width=100, height=50, text="CREATE", font=self.__font__,).grid(row=0, column=0, padx=25, pady=25)
        edit_node_btn = ctk.CTkButton(self, width=100, height=50, text="EDIT", font=self.__font__,).grid(row=0, column=1, pady=25)
        settings_btn = ctk.CTkButton(self, image=settings_image, width=50, height=50, text="", command=self.launch_settings).grid(row=0, column=2, padx=25, pady=25)

        scrollframe = ctk.CTkScrollableFrame(self, width=275, height=450, fg_color='#4c4e52', label_anchor='e',).place(x=25, y=100)

        self.build_theme()
        self.launch_settings() # ---DEBUG---
        # self.toplevel_window = None

    def build_theme(self):
        for widget in self.winfo_children():
            if widget.winfo_class() == 'Frame':
                index = str(widget).find('button')
                if index != -1:
                    if __theme__ == 'light': 
                        widget.configure(fg_color=f'#{theme['light-foreground-btn']}',
                                            hover_color=f'#{theme['light-hover-btn']}', text_color='#000000')
                        self.configure(fg_color=f'#{theme['light-foreground']}')
                    if __theme__ == 'dark':
                        widget.configure(fg_color=f'#{theme['dark-foreground-btn']}',
                                            hover_color=f'#{theme['dark-hover-btn']}', text_color='#ffffff')
                        self.configure(fg_color=f'#{theme['dark-foreground']}')
                    

    def launch_settings(self):
        # if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
        #     self.toplevel_window = settings.SettingsWindow(self)
        # else:
        #     self.toplevel_window.focus()
        toplevel_window = settings.SettingsWindow(self)



# -----LAUNCH APPLICATION-----
if __name__ == '__main__':
    app = MainWindow()

    # -----CONFIGURATION APP-----
    app.title(f'{meta['title']} {meta['version']}')

    app.mainloop()


""" TODO
    1) Решить проблему .configure у CTkScrollableFrame not working
    2) Поменять алгоритм установки темы
"""