from Input_Module import Input_Abstraction, Input_Presentation
from Calculator_Module import Calculator_Control


class InputControl():
    # create the respective button - get_button_0 will create a button labeled 0 which inputs 0 when clicked, and so on.
    def get_button_0(self,  e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 0)

    def get_button_1(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 1)

    def get_button_2(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 2)

    def get_button_3(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 3)

    def get_button_4(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 4)

    def get_button_5(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 5)

    def get_button_6(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 6)

    def get_button_7(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 7)

    def get_button_8(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 8)

    def get_button_9(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, 9)

    def get_button_plus(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, '+')

    def get_button_minus(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, '-')

    def get_button_mult(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, '*')

    def get_button_open_br(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, '(')

    def get_button_close_br(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, ')')

    def get_button_expo(self, e, root, myFont):
        return Input_Presentation.InputPresentation().button_builder(e, root, myFont, '^')

    # from abstraction, retrieve the listener logic
    def button_click_listener(self, e, num_input2):
        na = Input_Abstraction.InputAbstract()
        na.input_number(e, num_input2)

    def get_calc_control(self):
        # allows use of elements within Calc control module
        return Calculator_Control