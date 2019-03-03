import speech_recognition as sr
from recognize_speech import recognize_speech
from write import write

recognizer = sr.Recognizer()
microphone = sr.Microphone()

while True:
    usr = input('file or microphone (x to exit): ').lower()
    if usr == 'file':
        fname = input('file name: ')
        try:
            speech = recognize_speech(sr, recognizer, microphone, fname)
            write(speech)
        except FileNotFoundError:
            print('file {} does not exist'.format(fname))
    elif usr == 'mic':
        speech = []
        while True:
            phrase = recognize_speech(sr, recognizer, microphone)
            if phrase:
                speech.append(phrase)
            write(speech)
    elif usr == 'x':
        exit()
    else:
        print('invalid input')
