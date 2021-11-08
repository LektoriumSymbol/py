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

#run python3 -m venv myvenv
#run source myvenv/bin/activate
#run pip3 install flask twilio
#run server with command: python3 app.py