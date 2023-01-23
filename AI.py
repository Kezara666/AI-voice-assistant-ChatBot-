import sinhalato


def AI():
  import os
  import openai
  import textTovoice
  from openai import openai_object
  import json

  import mictoText
  openai.api_key = "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"
  openai.organization = "org-DwRjKVY15AnxrdRJhRGmBr3G"
  openai.api_key = "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"

  start_sequence = "\nA:"
  restart_sequence = "\n\nQ: "

  #voice = mictoText.micTotext()
  voice=sinhalato.sinhala()

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"\n\nQ:{voice}\nA:",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
  )
  value = response.get("choices", "text")
  text = ''
  for obj in value:
    # use the get() method to access the text field
    text = obj.get('text')
    print(value)

  textTovoice.textv(text)

  try:
    AI()
  except:
    AI()




