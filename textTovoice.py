def textv(t):
    import pyttsx3

    # create a Text-to-Speech engine object
    engine = pyttsx3.init()

    # define the text to convert to speech
    text = t
    # use the say() method to generate audio output
    engine.say(text)

    # run the speech synthesis
    engine.runAndWait()

