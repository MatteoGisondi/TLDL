def recognize_speech(sr, recognizer, audio_source, fname=None):
    '''return a string of recognized speech from microphone audio'''
    if fname:
        audio_source = sr.AudioFile('.\\audio_files\\' + fname)
    with audio_source as source:
        # adjust recognizer for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        if fname:
            audio = recognizer.record(source)
        else:
            audio = recognizer.listen(source)
    # try recognizing the speech in the recording
    use_sphinx = False
    try:
        if use_sphinx:
            response = recognizer.recognize_sphinx(audio)
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable
        raise Exception('API unavailable')
    except sr.UnknownValueError:
        # speech was unintelligible
        response = ''
    return response
