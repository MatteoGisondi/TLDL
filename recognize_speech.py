def recognize_speech(recognizer, audio_source, fname=None):
    '''return a string of recognized speech from microphone audio'''
    if fname:
        audio_source = sr.AudioFile(fname)
    with audio_source as source:
        # adjust recognizer for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        if fname:
            audio = recognizer.record(source)
        else:
            audio = recognizer.listen(source)
    # try recognizing the speech in the recording
    try:
        # pocketsphinx is a requirement
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable
        raise Exception('API unavailable')
    except sr.UnknownValueError:
        # speech was unintelligible
        response = ''
    return response
