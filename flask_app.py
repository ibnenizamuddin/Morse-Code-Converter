from flask import Flask, render_template, request, session, sessions, jsonify, current_app, send_file
from morsecode import Text_MorseCode_Converter
app = Flask(__name__)
app.secret_key = '123$morse'


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/result')
def submit():
    messagefromfield = request.args.get('value')
    returnvalue = Text_MorseCode_Converter(str(messagefromfield))
    return jsonify(morsecode=returnvalue)


if __name__ == '__main__':
    app.run(debug=True)
