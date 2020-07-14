from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse 
from utils import fetch_reply



app = Flask(__name__)


@app.route('/bot', methods=['POST'])

def sms_reply():
	incmbody = request.values.get('Body','').lower()
	msge = request.form.get('Body')
	phone_no = request.form.get('From')
	response = MessagingResponse()
	reply = fetch_reply(msge, phone_no)

	if incmbody in ('hi', 'hii', 'hey', 'hello'):
		response.message('Hi there! Whatsup')
	if incmbody in ("i'm good", 'nothing much', 'how are you', 'fine'):
		response.message("Do you want to listem joke?")
	if incmbody == 'no':
		response.message('Please give me a chance')
	else:
		response.message(reply)

	return str(response)

if __name__ == '__main__':
	app.run(debug=True)