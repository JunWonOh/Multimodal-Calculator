from Function_Module import Function_Abstraction, Function_Presentation
from Calculator_Module import Calculator_Control


class FunctionControl:
    # retrieve said buttons
    def get_button_delete(self, e, root, myFont):
        return Function_Presentation.FunctionPresentation().get_button_delete(e, root, myFont)

    def get_button_clear(self, e, root, myFont):
        return Function_Presentation.FunctionPresentation().get_button_clear(e, root, myFont)

    def get_button_equals(self, e, root, myFont):
        return Function_Presentation.FunctionPresentation().get_button_equals(e, root, myFont)
    # retrieve button logic
    def del_button_listener(self, e):
        Function_Abstraction.FunctionAbstraction().button_delete(e)

    def clear_button_listener(self, e):
        Function_Abstraction.FunctionAbstraction().button_clear(e)

    def equals_button_listener(self, e):
        Function_Abstraction.FunctionAbstraction().button_calculate(e)

    def get_calc_control_class(self):
        return Calculator_Control
