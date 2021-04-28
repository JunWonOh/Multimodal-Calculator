from Input_Module import Input_Controller
from tkinter import *


class InputPresentation:
    def button_builder(self, e, root, myFont, number):
        nc = Input_Controller.InputControl()
        # create a button, white font, labeled by number, function set to button_click_listener in Input_Controller
        return Button(root, bg="black", fg="white", text=str(number),
                      font=myFont, width=10, height=3,
                      command=lambda: nc.button_click_listener(e, str(number)))