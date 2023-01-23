def sinhala():
    import speech_recognition as sr
    from googletrans import Translator
    translator = Translator()
    listner = sr.Recognizer()

    with sr.Microphone() as source:
        listner.adjust_for_ambient_noise(source)
        print("ඔබේ ගැටලුව යොමු කරන්න .....")
        command = None
        voice = listner.listen(source)
        command = listner.recognize_google(voice, language='si', )
        print(command)

        word = translator.translate(command)
        new_word = word.text
        print(new_word)
        return new_word

