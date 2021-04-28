from tkinter import *
import threading
from Microphone_Module import Microphone_Control


class MicPresentation:
    # creates voice button and returns it. Gives on click functionality for button.
    def get_voice_button(self, e, root, myFont):
        return Button(root, bg="#33C1FF", fg="white", text="SPEECH MODE", font=myFont, width=21, height=3,
                      command=lambda: threading.Thread(target=lambda: Microphone_Control.MicControl().voice_button_click(e, root)).start())