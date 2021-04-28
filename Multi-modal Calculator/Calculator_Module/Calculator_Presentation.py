from tkinter import *
import tkinter.font as font
from Calculator_Module import Calculator_Control

# initialize the root
root = Tk()
# title of the window
root.title("CSI 407 Project")
# color of the window
root.configure(bg="#606060")
# disable resizing
root.resizable(False, False)

# the font of the buttons
myFont = font.Font(size=15, family="Ubuntu")
# The font of the text box
myFont2 = font.Font(size=25, family="Ubuntu")

# the text box
e = Entry(root, width=26, borderwidth=2, font=myFont2)
# at max, there can be 4 columns in the grid
e.grid(row=0, column=0, columnspan=4)

# asks user if they want to enter voice mode on init.
Calculator_Control.access_initial_prompt()


# behaves like EXIT_ON_CLOSE functionality on java swing, which is often included in Presentation
def close_window_click():
    print('Quitting Program..')
    root.quit()
    root.destroy()


class Presentation:

    cc = Calculator_Control.access_input_controller()
    cc_fc = Calculator_Control.access_function_control()

    # buttons arranged by rows and columns. get button functions are called to retrieve them
    # from different modules
    cc_fc.get_button_clear(e, root, myFont).grid(row=6, column=0)
    cc.get_button_0(e, root, myFont).grid(row=6, column=1)
    cc_fc.get_button_equals(e, root, myFont).grid(row=6, column=2, columnspan=2)

    cc.get_button_1(e, root, myFont).grid(row=5, column=0)
    cc.get_button_2(e, root, myFont).grid(row=5, column=1)
    cc.get_button_3(e, root, myFont).grid(row=5, column=2)
    cc.get_button_plus(e, root, myFont).grid(row=5, column=3)

    cc.get_button_4(e, root, myFont).grid(row=4, column=0)
    cc.get_button_5(e, root, myFont).grid(row=4, column=1)
    cc.get_button_6(e, root, myFont).grid(row=4, column=2)
    cc.get_button_minus(e, root, myFont).grid(row=4, column=3)

    cc.get_button_7(e, root, myFont).grid(row=3, column=0)
    cc.get_button_8(e, root, myFont).grid(row=3, column=1)
    cc.get_button_9(e, root, myFont).grid(row=3, column=2)
    cc.get_button_mult(e, root, myFont).grid(row=3, column=3)

    cc.get_button_open_br(e, root, myFont).grid(row=2, column=0)
    cc.get_button_close_br(e, root, myFont).grid(row=2, column=1)
    cc.get_button_expo(e, root, myFont).grid(row=2, column=2)
    cc_fc.get_button_delete(e, root, myFont).grid(row=2, column=3)

    # formats voice button
    Calculator_Control.access_voice_button(e, root, myFont).grid(row=1, column=0, columnspan=2)

    # gives additional functionality to close button
    root.wm_protocol("WM_DELETE_WINDOW", close_window_click)
    root.mainloop()




