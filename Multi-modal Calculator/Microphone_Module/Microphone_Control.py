from Microphone_Module import Microphone_Abstraction, Microphone_Presentation


class MicControl:
    def voice_button_click(self, e, root):
        # # clears text box
        # e.delete(0, END)
        # changes root title to say in voice mode
        root.title("CSI 407 Project (Listening | Voice Mode)")
        # run voice module from abstraction
        Microphone_Abstraction.run_voice()
        try:
            # change title
            root.title("CSI 407 Project")
        except:
            print('Program exited successfully!')

    def get_voice_button(self, e, root, myFont):
        # retrieves voice button from presentation
        return Microphone_Presentation.MicPresentation().get_voice_button(e, root, myFont)

    def get_initial_prompt(self):
        # retrieves initial prompt functionality from abstraction
        return Microphone_Abstraction.initial_run_prompt()
