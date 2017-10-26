from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
 
def echo(bot, update):
   """Metodo usato per rispondere ad un messagio con un testo identico a quello ricevuto"""
   update.message.reply_text(update.message.text)
 
def main():
   """Main del nostro programma"""
   updater = Updater("IL_TUO_TOKEN") # Creazione dell'updater, usato per ricevere aggiornamenti sugli input dell'utente
   dp = updater.dispatcher # Creazione del dispatcher, a cui verranno assegnati i metodi di risposta
 
 
   dp.add_handler(MessageHandler(Filters.text, echo)) # Qualsiasi messaggio ricevuto verrá gestito attraverso il metodo echo
 
   updater.start_polling() # Inzio del polling
 
   updater.idle() # Il bot viene arrestato quando Ctrl-C è stato premuto o il bot riceve un SIGINT, SIGTERM o SIGABRT.
 
 
if __name__ == '__main__':
   main()