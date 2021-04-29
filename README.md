# Multimodal-Calculator
Voice recognition/Button Calculator created using various Python libraries and the PAC design pattern

![Screenshot](https://github.com/JunWonOh/Multimodal-Calculator/blob/master/Multi-modal%20Calculator/screenshots/01.jpg)

## Running the program
To run the program, double click on the provided .exe file. The user will be greeted by the TTS, asking if they want to enter voice mode. Say ‘yes’ to enter, otherwise, say nothing/anything else in order to enter the main interface. The voice assistant will prompt the user, guiding them to use the voice mode.

## Description of all software packages used
1.	```threading``` – allows CPU to concurrently run another function while running the GUI. This was imported to avoid issues with the GUI freezing while Speech Mode is in use.
2.	```tkinter``` – a python library to create interactive GUIs. Everything visual in the project is attributed to this software package – the main window, buttons, text boxes, and on-click listeners.
3.	```speech_recognition``` – a built in python library to incorporate speech-to-text APIs from Microsoft, Google, IBM, Sphinx, and more. Allows for the program to record user input and convert it into text.
4.	```gTTS``` – a python library to allow for text-to-speech.
5.	```os``` – allows for control of the operating system. Used in the program to delete .mp3 files as they are created, to minimize space usage.
6.	```playsound``` – allows for the program to play .mp3 files.
7.	```pyinstaller``` – allows for conversion of .py files into executables.
