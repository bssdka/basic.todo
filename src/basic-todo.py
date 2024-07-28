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
widget = config['widget.SIZES']
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
        # Definition of function variables 
        # mw_btn - main_width_btn, mh_btn - main_height_btn, ss_btn - settings_size_btn, w_scrlframe - width_scrollframe,
        # h_scrollframe - height_scrollframe
        mw_btn, mh_btn, ss_btn = int(widget['width-main-btn']), int(widget['height-main-btn']), int(widget['size-settings-btn'])
        w_scrframe, h_scrollframe = int(widget['width-scrollframe']), int(widget['height-scrollframe'])

        # -----CREATINGE AND POSITIONING WIDGETS-----
        create_node_btn = ctk.CTkButton(self, width=mw_btn, height=mh_btn, text="CREATE", font=self.__font__,).grid(row=0, column=0, padx=25, pady=25)
        edit_node_btn = ctk.CTkButton(self, width=mw_btn, height=mh_btn, text="EDIT", font=self.__font__,).grid(row=0, column=1, pady=25)
        settings_btn = ctk.CTkButton(self, image=settings_image, width=ss_btn, height=ss_btn, text="", command=self.launch_settings).grid(row=0, column=2, padx=25, pady=25)

        scrollframe = ctk.CTkScrollableFrame(self, width=w_scrframe, height=h_scrollframe, fg_color='#4c4e52', label_anchor='e',).place(x=25, y=100)

        self.build_theme()
        self.launch_settings() # ---DEBUG---
        # self.toplevel_window = None

    def build_theme(self):
        for widget in self.winfo_children():
            if widget.winfo_class() == 'Frame':
                
                try:
                    if __theme__ == 'light': 
                        widget.configure(fg_color=f'#{theme['light-foreground-btn']}',
                                        hover_color=f'#{theme['light-hover-btn']}', text_color='#000000')
                        self.configure(fg_color=f'#{theme['light-foreground']}')
                    if __theme__ == 'dark':
                        widget.configure(fg_color=f'#{theme['dark-foreground-btn']}',
                                        hover_color=f'#{theme['dark-hover-btn']}', text_color='#ffffff')
                        self.configure(fg_color=f'#{theme['dark-foreground']}')
                except ValueError:
                    pass

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
    1) Решить проблему .configure у CTkScrollableFrame
    2) Поменять алгоритм установки темы
"""