import speech_recognition as sr
from recognize_speech import recognize_speech
from write import writeS
def file(fname,path):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    try:
        speech = recognize_speech(sr, recognizer, microphone, fname)
        return writeS(speech , path)
    except FileNotFoundError:
        return 'file {} does not exist'.format(fname)

def mic(path):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    speech = ''
    while True:
        try:
            phrase = recognize_speech(sr, recognizer, microphone)
            if phrase:
                speech += phrase + ' '
                print(phrase)
        except KeyboardInterrupt:
            if speech:
                writeS(speech, path)
            break

if __name__ == '__main__':
    while True:
        inp = input('f or m: ')
        if inp == 'f':
            file(input('file name: '))
        elif inp == 'm':
            mic()
        else:
            print('invalid')

    # to import from elsewhere, import filename
    # then run function file(fname) or mic()
