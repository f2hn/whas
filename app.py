from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app =  Flask(__name__)

@app.route("/")
def helo():
        return("helo")

app.route("/sms", methods=["POST"])
def y():
        msg = request.form.get('Body')
        resp = MessagingResponse()
        resp.message("test :{}".format(msg))
        return str(resp)

if __name__ == ("__main__"):
        app.run(debug=True)
