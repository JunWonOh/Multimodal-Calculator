from Function_Module import Function_Control
from tkinter import *


class FunctionAbstraction:
    def button_delete(self, e):
        cc = Function_Control.FunctionControl().get_calc_control_class()
        # get the current text in textbox
        current = e.get()
        # clear the text box
        e.delete(0, END)
        # remove the last character from current
        cc.set_text(e, current[:-1])

    def button_clear(self, e):
        # delete contents of text_box
        e.delete(0, END)

    def button_calculate(self, e):
        cc = Function_Control.FunctionControl().get_calc_control_class()
        # get the text from the textbox
        current = e.get()
        run = cc.access_calculator()
        try:
            # run calculate on given text on textbox
            solution = run.calculate(current)
            # clear the text box
            e.delete(0, END)
            # replace with new solutoin
            cc.set_text(e, int(solution))
        except:
            # if formatted incorrectly, error.
            print("Cannot Calculate: INCORRECT FORMATTING")