# coding utf-8

import customtkinter as ctk
from PIL import Image
import os

"""[INFO]
    Swap file. Images, data from github and so on will be uploaded here. 
"""

# -----GLOBAL VARIABLES-----
__path__ = os.getcwd()

def image_swap() -> vars:
    settings_50x50 = ctk.CTkImage(light_image=Image.open(f'{__path__}/img/settings-50x50-light.png'),
                            dark_image=Image.open(f'{__path__}/img/settings-50x50-dark.png'), size=(35, 35))

    return settings_50x50