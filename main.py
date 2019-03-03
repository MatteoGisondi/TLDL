import time
import speech_recognition as sr

def recognize_speech(recognizer, audio_source, fname=None):
    '''return a string of recognized speech from microphone audio'''
    if fname:
        audio_source = sr.AudioFile(fname)
    with audio_source as source:
        # adjust recognizer for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        if fname:
            audio = recognizer.record(source, duration=3)
        audio = recognizer.listen(source)
    # try recognizing the speech in the recording
    try:
        response = recognizer.recognize_sphinx(audio)
    except sr.RequestError:
        # API was unreachable
        raise Exception('API unavailable')
    except sr.UnknownValueError:
        # speech was unintelligible
        response = 'Unable to recognize speech'
    return response

if __name__ == '__main__':
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    usr = input('file or microphone (x to exit): ').lower()
    while True:
        if usr == 'file':
            file = input('file name: ')
            try:
                phrase = recognize_speech(recognizer, microphone, fname=file)
                print(phrase)
            except:
                print('file {} does not exist'.format(fname))
        elif usr == 'mic':
            speech = []
            while True:
                phrase = recognize_speech(recognizer, microphone)
                speech.append(phrase)
                print(*speech)
        elif usr == 'x':
            exit()
        else:
            print('invalid input')
