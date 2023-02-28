import pyttsx3
import speech_recognition
from datetime import date, datetime

bot_ear = speech_recognition.Recognizer()
bot = pyttsx3.init()

while True:
	with speech_recognition.Microphone() as mic:
		print("Bot: I'm listening")
		bot.say("I'm listening")
		bot.runAndWait()
		audio = bot_ear.listen(mic)

	try:
		you = bot_ear.recognize_google(audio)
	except:
		you = "Can't recognize!"

	print("You: " + you)
	bot_brain = you

	if you == "":
		bot_brain = "I can't hear you, try again"
	elif "hello" in you:
		bot_brain = "hello Tom!"
	elif "today" in you:
		today = date.today()
		bot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		bot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		bot_brain = "Bye Tom!"
		print(bot_brain)
		bot.say(bot_brain)
		bot.runAndWait()
		break;
	else:
		bot_brain = "I'm fine thank you and you"

	print(bot_brain)
	bot.say(bot_brain)
	bot.runAndWait()