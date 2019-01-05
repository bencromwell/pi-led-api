from flask import Flask, request, make_response, abort
from ledapi import led
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

TOKEN = os.getenv('TOKEN')
LED_PIN = int(os.getenv('LED_PIN'))
TIMES_TO_BLINK = int(os.getenv('TIMES_TO_BLINK'))
SECONDS_TO_BLINK_ON = int(os.getenv('SECONDS_TO_BLINK_ON'))


@app.route('/warning-light/<token>', methods=['POST'])
def warning_light(token):
    if request.method == 'POST':
        if token == TOKEN:
            # @todo accept, return the response, then fork to run the LEDs
            led.go(LED_PIN, num_times=TIMES_TO_BLINK, seconds_on=SECONDS_TO_BLINK_ON)
            return make_response(('', 202))
        else:
            abort(401)
    else:
        abort(501)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
