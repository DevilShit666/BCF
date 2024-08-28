import telebot


token = "7009651036:AAEEApjX_R-XCWCnOtCUKyfrXdphlCB82rY"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_all_accounts(message):
    bot.send_message(message.chat.id, text=f"{message.chat.id}")


def send_notify_level_up(udid, level, monster_id):
    bot.send_message(446809031, text=f"{udid} ({monster_id}) has reached {level} level")


def send_notify_new_account(udid, monster_id):
    bot.send_message(446809031, text=f"new account {udid} ({monster_id})")