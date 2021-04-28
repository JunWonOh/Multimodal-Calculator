from Input_Module import Input_Controller


class InputAbstract:
    def input_number(self, e, num_input):
        # ping controller for button_click function
        Input_Controller.InputControl().get_calc_control().button_click(e, num_input)