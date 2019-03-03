import time
import speech_recognition as sr

def recognize(recognizer, audio):
    # try recognizing the speech in the recording
    try:
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable
        raise Exception('API unavailable')
    except sr.UnknownValueError:
        # speech was unintelligible
        response = 'Unable to recognize speech'
    return response

def recognize_speech(recognizer, audio_source):
    '''return a string of recognized speech from microphone audio'''
    with audio_source as source:
        # adjust recognizer for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # start recording
        audio = recognizer.listen(source, timeout=3)
    response = recognize(recognizer, audio)

if __name__ == '__main__':
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    usr = input('File or microphone (x to exit): ').lower()
    while True:
        if usr == 'file':
            fname = input('file name: ')
            try:
                f = open(fname)
                recognize_speech_from_file(f)
            except:
                raise FileNotFoundError('file {} does not exist'.format(fname))
        elif usr == 'mic':
            while True:
                speech = recognize_speech(recognizer, microphone)
                print(speech)
        elif usr == 'x':
            exit()
        else:
            print('invalid input')
