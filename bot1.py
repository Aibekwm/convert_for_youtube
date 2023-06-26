import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне ссылку на видео с YouTube.')

# Обработчик команды /convert
def convert_video(update: Update, context: CallbackContext) -> None:
    # Получение ссылки на видео с YouTube из сообщения пользователя
    video_url = update.message.text.split(' ')[1]
    
    # Конвертация видео в аудио формат с помощью youtube-dl
    os.system(f'youtube-dl -x --audio-format mp3 {video_url}')
    
    # Отправка аудиофайла пользователю
    audio_file = f'{video_url.split("=")[1]}.mp3'
    update.message.reply_audio(open(audio_file, 'rb'))
    
    # Удаление временного аудиофайла
    os.remove(audio_file)

# Установка параметров
bot_token = '6219015528:AAEnurjpbDE-rlBQjyYb4Lqxy8pqLNKTS9Q'
updater = Updater(bot_token)

# Добавление обработчиков команд
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('convert', convert_video))

# Запуск бота
updater.start_polling()
updater.idle()
