import pyttsx3

bot = pyttsx3.init()
def sayU(you):
    bot_brain = you
    bot.say(bot_brain)
    bot.runAndWait()