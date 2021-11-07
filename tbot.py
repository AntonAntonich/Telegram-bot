import logging
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level = logging.INFO,
					filename='bot.log')

def start_bot(update: Updater, context: CallbackContext):
	print(update)
	myMessage = """Hello, {}. 
	I have only /start command""".format(update.message.chat.username)
	update.message.reply_text(myMessage)

def chat(update: Updater, context: CallbackContext):
	recived_message = update.message.text
	logging.info(recived_message)
	if recived_message == "Hello" or recived_message == "Привет":
		text = "Привет, {}".format(update.message.chat.username)
	elif recived_message == "Bye"  or  recived_message == "Пока":
		text = "Пока, {}".format(update.message.chat.username)
	else:
		text = """Сперва, давай поздороваемся. Напши мне Привет =)
		Или можем попрощаться. Тогда напиши Пока"""	
	update.message.reply_text(text)	

def main():
	updater = Updater('2118317735:AAFb0KsCqcNEzl_ajZf8BaTmJIoGYWhV9g0')
	updater.dispatcher.add_handler(CommandHandler("start", start_bot))
	updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	updater.start_polling()
	updater.idle()

if __name__ == "__main__":
	logging.info('Bot started !')
	main()		