import telebot

bot = telebot.TeleBot("<your token here>")

#/start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello World da Realeza!")

#/help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Caro " + message.from_user.first_name + ", como poderia eu ajudá-lo?\nDigite /commands para conhecer os comandos")

#/saudacao
@bot.message_handler(commands=['saudacao'])
def cmdSaudacao(message):
    bot.reply_to(message, 'Saudações, nobre humano ' + message.from_user.first_name + '!')

#/thinking
@bot.message_handler(commands=['thinking'])
def teste(message):
    bot.reply_to(message, "Hmmmm")

#/commands
@bot.message_handler(commands=['commands'])
def commands(message):
    listaComandos = "/start : Acorda o bot real\n/help : Pede ajuda ao bot real\n/thinking : Faz o bot real pensar\n/saudacao : Cumprimenta a pessoa"
    bot.send_message(message.chat.id, listaComandos)

#ve quando a pessoa manda um 'oi' ou 'ola' ou 'hi'
def saudacoes(message):
    if (message.content_type == 'text'):
        if (message.text.lower() == 'hi'):
            return True

#envia a msg se saudacoes() retornar True
@bot.message_handler(func=saudacoes)
def send_msg(message):
    bot.reply_to(message, message.text + ' ' +  message.from_user.last_name)

bot.polling()