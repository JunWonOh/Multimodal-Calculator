from tkinter import *
from Function_Module import Function_Control


class FunctionPresentation:
    # create following buttons with listeners
    def get_button_clear(self, e, root, myFont):
        return Button(root, bg="black", fg="white", text="CLEAR", font=myFont, width=10, height=3,
                      command=lambda: Function_Control.FunctionControl().clear_button_listener(e))

    def get_button_equals(self, e, root, myFont):
        return Button(root, bg="black", fg="white", text="=", font=myFont, width=21, height=3,
                      command=lambda: Function_Control.FunctionControl().equals_button_listener(e))

    def get_button_delete(self, e, root, myFont):
        return Button(root, bg="grey", fg="white", text="↲ DEL", font=myFont, width=10, height=3,
                      command=lambda: Function_Control.FunctionControl().del_button_listener(e))
