from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pyowm import OWM
from pyowm.utils.config import get_default_config

app = Flask(__name__)
config_dict = get_default_config()
config_dict['language'] = 'en'

owm = OWM('fcdb2136605493641a45858f52a39d97', config_dict)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/sms", methods=['POST'])
def sms_reply():

    msg = request.form.get('Body')
    mgr = owm.weather_manager()
    resp = MessagingResponse()

    try:
        observation = mgr.weather_at_place(msg)
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

        responce = ("In " + str(msg) + " temperature " + str(t1) + " °C" + "\n" + 
            "Max temperature " + str(t3) + " °C" +"\n" + 
            "Min temperature " + str(t4) + " °C" + "\n" + 
            "Feels like " + str(t2) + " °C" + "\n" +
            "Wind " + str(wi) + " m/s" + "\n" + 
            "Atmospheric Pressure " + str(pr) + " ft" + "\n" + 
            "Humidity " + str(humi) + " %" + "\n" + 
            "Visibility distance " + str(vd) + "  m" + "\n" +
            "Overview " + str(st) + "\n\n" + str(dt))

    
    except Exception:
        responce = "City wasn't found :'("

    resp.message("{}".format(responce))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

#run python3 -m venv myvenv OR python -m venv myvenv on windows using gitbash
#run source myvenv/bin/activate OR myvenv/Scripts/activate on windows using gitbash
#run pip3 install flask twilio
#run server with command: python3 app.py OR python app.py on windows using gitbash

#run pip3 install gunicorn
#create Procfile with line web gunicorn app:app
#create runtime.txt with line python-3.x.x
#run pip3 freeze > requirements.txt