from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message("Your massage: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

#run python3 -m venv myvenv OR python -m venv myvenv on windows using gitbash
#run source myvenv/bin/activate OR myvenv/Scripts/activate on windows using gitbash
#run pip3 install flask twilio
#run server with command: python3 app.py OR python app.py on windows using gitbash