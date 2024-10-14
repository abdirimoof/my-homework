# from transliterate import to_cyrillic,to_latin
# import telebot
# TOKEN = '7395976500:AAFeetMNOuLG6tOd05Kb9VqEl0Oc6n2k5gQ'
# bot = telebot.TeleBot(TOKEN, parse_mode=None)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#         javob = "ASSALOMU ALEKUM. XUSH KELIBSIZ"
#         javob += '\n Matn kiriting: ' 
#         bot.reply_to(message,javob )
        
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     msg = message.text
#     if msg.isascii():
#        javob = print(to_cyrillic(msg))
#     else:
#         javob = print(to_latin(msg))
#         bot.reply_to(message, javob(msg))

# bot.polling()




import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = '7395976500:AAFeetMNOuLG6tOd05Kb9VqEl0Oc6n2k5gQ'  # <-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)


# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda s: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()








# 7395976500:AAFeetMNOuLG6tOd05Kb9VqEl0Oc6n2k5gQ
# matn = input('Matn kiriting: ')

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
