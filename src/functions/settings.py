# coding utf-8

import customtkinter as ctk
import configparser as cfg
import os

# -----GLOBAL VARIABLES-----
__path__ = os.getcwd()

# -----READ BASIC.INI-----
config = cfg.ConfigParser()
config.read(f'{__path__}/config/basic.ini')
meta = config['DEFAULT']
theme = config['system.THEME']
font = config['FONT']
__theme__ = meta['theme'] # global variable


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__font__ = ctk.CTkFont(family=font['family'], size=int(font['size'])+4, weight=font['weight'])

        self.geometry(f'{meta['width_settings']}x{meta['height_settings']}')
        # I don't know why function self.configure(fg_color) not working, but it works here. wtf...
        if __theme__ == 'light': 
            self.configure(fg_color=f'#{theme['light-foreground']}') 
            self.__color__ = '#000000'
        if __theme__ == 'dark': 
            self.configure(fg_color=f'#{theme['dark-foreground']}')
            self.__color__ = '#ffffff'

        self.initUI()
    def initUI(self):
        # -----BUILD WIDGETS-----
        label_switch = ctk.CTkLabel(self, text='SWITCH\nTHEME', width=150, height=50, font=self.__font__, text_color=self.__color__).grid(row=0, column=0, pady=25)
        theme_switch = ctk.CTkSwitch(self, switch_width=75, switch_height=40, text="").grid(row=0, column=1, padx=0, pady=25)

        self.build_theme()


    def build_theme(self):
        for widget in self.winfo_children():
            index = str(widget).find('button')
            if index != -1:
                if __theme__ == 'light': 
                    widget.configure(fg_color=f'#{theme['light-foreground-btn']}',
                                hover_color=f'#{theme['light-hover-btn']}', text_color='#000000')
                if __theme__ == 'dark':
                    widget.configure(fg_color=f'#{theme['dark-foreground-btn']}',
                                hover_color=f'#{theme['dark-hover-btn']}', text_color='#ffffff')
            
""" TODO
    1) Реализовать темы для виджетов
    2) Поменять switch на 2 кнопки
"""