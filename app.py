from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse 
from utils import fetch_reply



app = Flask(__name__)

@app.route('/')
def hello_sms():
	return "Hi, this is whatsapp bot."
@app.route('/bot', methods=['POST'])
def sms_reply():
	incmbody = request.values.get('Body','').lower()
	msge = request.form.get('Body')
	phone_no = request.form.get('From')
	response = MessagingResponse()
	reply1 = fetch_reply(msge, phone_no)
	responded = False
	if  incmbody in ('hi', 'hey', 'hello'):
		text = "Hi I'm whatsapp chatbot"
		response.message(text)
		responded = True
	elif incmbody in ('bye', 'goodbye'):
		response.message("Goodbye!")
		responded = True
	else:
		response.message(reply1)
		responded = True
	
	if not responded:
		response.message("Sorry, I'have a problem")
	return str(response)

if __name__ == '__main__':
	app.run(debug=True)