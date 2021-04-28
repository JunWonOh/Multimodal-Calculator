import speech_recognition as sr
import playsound
import os
from gtts import gTTS
from Calculator_Module import Calculator_Control


# NOTE: PYTHON DOES NOT SUPPORT PRIVATE METHODS, CONVENTION IS TO USE "_" (UNDERSCORE)
# BEFORE METHOD NAME TO SAY OTHER CLASSES SHOULD NOT ACCESS THEM


def _get_grammar(equation):
    # replace x with y (where x is a easy to mispronounce word, y is the correct word)
    equation = equation.replace("exponent", "^")
    equation = equation.replace("open bracket", "(")
    equation = equation.replace("close bracket", ")")
    equation = equation.replace("plus", "+")
    equation = equation.replace("one", "1")
    equation = equation.replace("for", "4")
    equation = equation.replace("too", "2")
    equation = equation.replace("tree", "3")
    try:
        index = equation.index("all")
        # for example x plus y all minus z becomes (x+y)-z
        equation = "(" + equation[:index] + ")" + equation[index:]
        equation = equation.replace("all", "")
    except:
        pass
    equation = equation.replace("x", "*")
    equation = equation.replace(" ", "")
    return equation


def _prompt_user():
    # ask user for equation TTS
    tts = gTTS('Tell me an equation', lang='en')
    print('TTS: Tell me an equation: ')
    # save it and play it
    tts.save("recording.mp3")
    playsound.playsound("recording.mp3")
    # remove it to save space
    os.remove("recording.mp3")


def _repeat_user(equation):
    # repeat the equation back
    tts = gTTS('You said: {}'.format(equation), lang='en')
    print('TTS: You said: {}'.format(equation))
    tts.save("recording.mp3")
    playsound.playsound("recording.mp3")
    os.remove("recording.mp3")


def _say_solution(solution):
    # say the solution
    tts = gTTS('The answer is: {}'.format(int(solution)), lang='en')
    print('TTS: The answer is: {}'.format(int(solution)))
    tts.save("recording.mp3")
    playsound.playsound("recording.mp3")
    os.remove("recording.mp3")


def _say_error_message():
    # tell user that formatting is incorrect. ask to try again
    tts = gTTS('Sorry, cannot compute that. Try again?', lang='en')
    print('TTS: Sorry, cannot compute that. Try again?')
    tts.save("recording.mp3")
    playsound.playsound("recording.mp3")
    os.remove("recording.mp3")
    # take input
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        audio2 = r2.listen(source)
        reply2 = r2.recognize_google(audio2)
        # if input is yes
        if reply2 == 'yes':
            # restart the query
            run_voice()
        else:
            # if anything but yes (even nothing), exit
            print('Exited Speech Mode')


# see _say_error_message
def _ask_again():
    tts = gTTS('Try again?', lang='en')
    print('TTS: Try again?')
    tts.save("recording.mp3")
    playsound.playsound("recording.mp3")
    os.remove("recording.mp3")
    r3 = sr.Recognizer()
    with sr.Microphone() as source:
        audio3 = r3.listen(source)
        reply3 = r3.recognize_google(audio3)
        if reply3 == 'yes':
            run_voice()
        else:
            print('Exited Speech Mode')


# runs upon initialization of the program
def initial_run_prompt():
    # greet user, ask if they want to enter speech
    tts = gTTS('Welcome to the multi-modal calculator. Enter Speech Mode?', lang='en')
    print('TTS: Welcome to the multi-modal calculator. Enter Speech Mode?')
    # save as mp3, play it, then delete it
    tts.save("recording.mp3")
    playsound.playsound("recording.mp3")
    os.remove("recording.mp3")
    # take voice input
    r4 = sr.Recognizer()
    with sr.Microphone() as source:
        audio4 = r4.listen(source)
        reply4 = r4.recognize_google(audio4)
        print(reply4)
        # if user says yes
        if reply4 == 'yes':
            # start module query
            run_voice()
        else:
            # otherwise, exit
            print('Exited Speech Mode')


def run_voice():
    r = sr.Recognizer()

    run = Calculator_Control.access_calculator()
    with sr.Microphone() as source:
        # call _prompt_user() function (see above)
        _prompt_user()
        audio = r.listen(source)

        try:
            # use google's speech API to get user input
            equation = r.recognize_google(audio)
            # format the answer
            equation = equation.lower()
            equation = _get_grammar(equation)
            # repeat what the user said
            _repeat_user(equation)
            # use calculator module to calculate user input
            solution = run.calculate(equation)
            # say solution
            _say_solution(solution)
            # ask if they want to try again
            _ask_again()
        except:
            # if cannot be computed, error
            _say_error_message()