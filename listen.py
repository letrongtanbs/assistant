import speech_recognition

bot_ear = speech_recognition.Recognizer()
def listenU():
	with speech_recognition.Microphone() as mic:
		print("Bot: I'm listening")
		audio = bot_ear.listen(mic)
	try:
		you = bot_ear.recognize_google(audio)
	except:
		you = "Can' recognize!"

	print("You: " + you)
	return str(you)