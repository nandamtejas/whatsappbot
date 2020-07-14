from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse 
from utils import fetch_reply



app = Flask(__name__)

@app.route('/')
def hello_sms():
	link = requests.get("https://web.whatsapp.com/")
	return link.body
@app.route('/bot', methods=['POST'])
def sms_reply():
	incmbody = request.values.get('Body','').lower()
	msge = request.form.get('Body')
	phone_no = request.form.get('From')
	response = MessagingResponse()
	reply = fetch_reply(msge, phone_no)
	response.message(reply)

	return str(response)

if __name__ == '__main__':
	app.run(debug=True)