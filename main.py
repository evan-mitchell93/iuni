from flask import Flask, jsonify, render_template, request
from datetime import datetime
import pytz
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
    #render main page and send a list of all timezones
    return render_template("timezone.html", content = pytz.all_timezones )

@app.route('/get_time', methods=['GET'])
def getTime():
   tz = request.args.get('tz', '')
   print(tz)
   response = jsonify(datetime.now(pytz.timezone(tz)).strftime("%I:%M %p"))
   response.headers.add("Access-Control-Allow-Origin", "*")
   return response


if __name__ == '__main__':
    app.run()