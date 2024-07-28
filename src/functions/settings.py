# coding utf-8

import customtkinter as ctk
import configparser as cfg
from elevate import elevate
import subprocess
import sys
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

# Define values for rendering the correct theme for widgets 
if __theme__ == 'light': 
    __color__ = '#000000'
    __btn_change_theme__ = 'DARK THEME'
if __theme__ == 'dark': 
    __color__ = '#ffffff'
    __btn_change_theme__ = 'LIGHT THEME'


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__font__ = ctk.CTkFont(family=font['family'], size=int(font['size'])+4, weight=font['weight'])

        self.geometry(f'{meta['width_settings']}x{meta['height_settings']}')

        self.initUI()
    def initUI(self):
        # -----BUILD WIDGETS-----
        label_switch = ctk.CTkLabel(self, text='SWITCH\nTHEME', width=100, height=50, font=self.__font__, text_color=__color__).grid(row=0, column=0, padx=25, pady=25)
        light_theme_btn = ctk.CTkButton(self, text=__btn_change_theme__, width=200, height=50, font=self.__font__, text_color=__color__, command=self.change_theme).grid(row=0, column=1, padx=25, pady=25)

        # Init theme
        self.build_theme()


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


    def change_theme(self):
        # Change configuration file
        if __theme__ == 'light': config.set('DEFAULT', 'theme', 'dark')
        if __theme__ == 'dark': config.set('DEFAULT', 'theme', 'light')
        with open(f'{__path__}/config/basic.ini', 'w') as configfile:
            config.write(configfile)
        elevate(graphical=False)
        # -RESTART APP-
        subprocess.run([f'{__path__}/src/restart.sh'])
        raise SystemExit(0)
        
        
 

""" TODO
    1) Реализовать темы для виджетов
    2) Поменять switch на 2 кнопки
"""