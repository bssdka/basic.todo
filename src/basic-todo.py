# coding utf-8

import customtkinter as ctk
import configparser as cfg
import platform
import os

# Import functions of your code
import swap

# -----GLOBAL VARIABLES-----
__path__ = os.getcwd()
__system__ = platform.system()

# -----READ BASIC.INI-----
config = cfg.ConfigParser()
config.read(f'{__path__}/config/basic.ini')
meta = config['DEFAULT']
debug = config['DEBUGGING']
widget = config['widget.SIZES']
font = config['FONT']

# -----REFER TO OUR FUNCTIONS-----
settings_image = swap.image_swap()


class MainWindow(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__()
        self.geometry(f'{meta['width']}x{meta['height']}')
        self.__font__ = ctk.CTkFont(family=font['family'], size=int(font['size']), weight=font['weight'])

        self.initUI()
    def initUI(self):
        # Definition of function variables (mw_btn - main_width_btn, mh_btn - main_height_btn, ss_btn - settings_size_btn )
        mw_btn, mh_btn, ss_btn = int(widget['width_main_btn']), int(widget['height_main_btn']), int(widget['size_settings_btn'])

        # -----CREATINGE AND POSITIONING WIDGETS-----
        create_node_btn = ctk.CTkButton(self, width=mw_btn, height=mh_btn, text="CREATE", font=self.__font__,
                                        ).grid(row=0, column=0, padx=25, pady=25)
        edit_node_btn = ctk.CTkButton(self, width=mw_btn, height=mh_btn, text="EDIT", font=self.__font__,
                                        ).grid(row=0, column=1, pady=25)
        settings_btn = ctk.CTkButton(self, image=settings_image, width=ss_btn, height=ss_btn, text="").grid(row=0, column=2, padx=25, pady=25)



# -----LAUNCH APPLICATION-----
if __name__ == '__main__':
    app = MainWindow()

    # -----CONFIGURATION APP-----
    app.title(f'{meta['title']} {meta['version']}')
    ctk.set_appearance_mode(debug['debug_appearance_mode'])
    # ctk.set_default_color_theme(f'{__path__}/config/theme.json')

    app.mainloop()