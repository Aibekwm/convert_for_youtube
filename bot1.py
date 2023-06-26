import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(' Отправь мне ссылку на видео с YouTube.')

#
def convert_video(update: Update, context: CallbackContext) -> None:
 
    video_url = update.message.text.split(' ')[1]
    

    os.system(f'youtube-dl -x --audio-format mp3 {video_url}')
    
 
    audio_file = f'{video_url.split("=")[1]}.mp3'
    update.message.reply_audio(open(audio_file, 'rb'))
    

    os.remove(audio_file)


bot_token = '6219015528:AAEnurjpbDE-rlBQjyYb4Lqxy8pqLNKTS9Q'
updater = Updater(bot_token)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('convert', convert_video))

# Запуск бота
updater.start_polling()
updater.idle()
