# print("* * * This is your weather bot * * *")
#    pip install pyowm
#    pip install pyTelegramBotAPI
from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot

bot = telebot.TeleBot("2122884968:AAHU44s4jE_YhTzKRVJ4boXixLeS9UiOfic")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    # bot.reply_to(message, message.text)
    # bot.send_message(message.chat.id, message.text)

    #print(message)

    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    owm = OWM('fcdb2136605493641a45858f52a39d97', config_dict)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(message.text)
        w = observation.weather

        t = w.temperature("celsius")
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']

        wi = w.wind()['speed']
        humi = w.humidity
        cl = w.clouds
        st = w.status
        dt = w.detailed_status
        ti = w.reference_time('iso')
        pr = w.pressure['press']
        vd = w.visibility_distance

        responce = ("В городе " + str(message.text) + " температура " + str(t1) + " °C" + "\n" + 
            "Максимальная температура " + str(t3) + " °C" +"\n" + 
            "Минимальная температура " + str(t4) + " °C" + "\n" + 
            "Ощцщается как" + str(t2) + " °C" + "\n" +
            "Скорость ветра " + str(wi) + " м/с" + "\n" + 
            "Давление " + str(pr) + " мм.рт.ст" + "\n" + 
            "Влажность " + str(humi) + " %" + "\n" + 
            "Видимость " + str(vd) + "  метров" + "\n" +
            "Описание " + str(st) + "\n\n" + str(dt))

        bot.send_message(message.chat.id, responce)
    
    except Exception:
        bot.send_message(message.chat.id, "Город не найден :'(")
    

bot.polling(none_stop = True)
