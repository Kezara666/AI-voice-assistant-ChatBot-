

def micTotext():
    import speech_recognition as sr
    # create a Recognizer object
    r = sr.Recognizer()

    # create a microphone object
    mic = sr.Microphone()

    # start listening to the microphone
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_data = r.listen(source)

    # recognize the speech in the audio data
    text = r.recognize_google(audio_data)

    # print the recognized text
    print(text)
    return text