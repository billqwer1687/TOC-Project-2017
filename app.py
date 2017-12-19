import sys
import imp
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '505050164:AAGxd3RICtZh9A36aTgnygxheiabZIQJRs0'
WEBHOOK_URL = 'https://df48770a.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'drink',
        'food',
	'play',
	'drinkname1',
        'drinkname2',
	'drinkname3',
	'drinkname4',
	'drinkname5',
	'foodname1',
	'foodname2',
        'foodname3',
	'foodname4',
	'foodname5',
	'zero',
	'mid',
	'high'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'drink',
            'conditions': 'is_going_to_drink'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'food',
            'conditions': 'is_going_to_food'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'play',
            'conditions': 'is_going_to_play'
        },
	{
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'drinkname1',
            'conditions': 'is_going_to_drinkname1'
        },
        {
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'drinkname2',
            'conditions': 'is_going_to_drinkname2'
        },
        {
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'drinkname3',
            'conditions': 'is_going_to_drinkname3'
        },
	{
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'drinkname4',
            'conditions': 'is_going_to_drinkname4'
        },
	{
            'trigger': 'advance',
            'source': 'drink',
            'dest': 'drinkname5',
            'conditions': 'is_going_to_drinkname5'
        },
	{
            'trigger': 'advance',
            'source': 'food',
            'dest': 'foodname1',
            'conditions': 'is_going_to_foodname1'
        },
        {
            'trigger': 'advance',
            'source': 'food',
            'dest': 'foodname2',
            'conditions': 'is_going_to_foodname2'
        },
        {
            'trigger': 'advance',
            'source': 'food',
            'dest': 'foodname3',
            'conditions': 'is_going_to_foodname3'
        },
	{
            'trigger': 'advance',
            'source': 'food',
            'dest': 'foodname4',
            'conditions': 'is_going_to_foodname4'
        },
	{
            'trigger': 'advance',
            'source': 'food',
            'dest': 'foodname5',
            'conditions': 'is_going_to_foodname5'
        },
	{
            'trigger': 'advance',
            'source': 'play',
            'dest': 'zero',
            'conditions': 'is_going_to_zero'
        },
	{
            'trigger': 'advance',
            'source': 'play',
            'dest': 'mid',
            'conditions': 'is_going_to_mid'
        },
	{
            'trigger': 'advance',
            'source': 'play',
            'dest': 'high',
            'conditions': 'is_going_to_high'
        },
        {
            'trigger': 'go_back',
            'source': [
                'drink',
                'food',
		'play',
		'drinkname1',
		'drinkname2',
                'drinkname3',
		'drinkname4',
		'drinkname5',
		'foodname1',
		'foodname2',
                'foodname3',
		'foodname4',
		'foodname5',
		'zero',
		'mid',
		'high'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
