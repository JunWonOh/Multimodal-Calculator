from tkinter import *
from Calculator_Module import Calculator_Abstraction
from Input_Module import Input_Controller
from Microphone_Module import Microphone_Control
from Function_Module import Function_Control


# retrieves initial prompt functionality from Microphone module
def access_initial_prompt():
    return Microphone_Control.MicControl().get_initial_prompt()


# retrieves voice on click functionality from Microphone module
def access_voice_button_click(e, root):
    return Microphone_Control.MicControl().voice_button_click(e, root)


# retrieves voice mode button from Microphone module
def access_voice_button(e, root, myFont):
    return Microphone_Control.MicControl().get_voice_button(e, root, myFont)


# retrieves input controller
def access_input_controller():
    return Input_Controller.InputControl()


# retrieves function controller
def access_function_control():
    return Function_Control.FunctionControl()


# from the calculator's abstraction, retrieve calculator for computing expressions
def access_calculator():
    return Calculator_Abstraction.Calculator()


# button click logic - when pressed, replace text with the current string in text box minus + 1 char
def button_click(e, text_input):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(text_input))


# replace text in text box with text
def set_text(e, text):
    e.insert(0, str(text))


