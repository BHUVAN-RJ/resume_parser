from flask import Flask,request, render_template
from otp_verification import OtpVerifier
import re

app = Flask(__name__)
phone = ""
phone_pattern = re.compile(r'^(\+91)\s*? *')
otp_verifier = OtpVerifier()

phone_number = re.compile(r'(\+91)?(-)?\s*?(91)?\s*?(\d{3})-?\s*?(\d{3})-?\s*?(\d{4})')
mail = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')

@app.route('/submit', methods=['POST'])
def send_otp():
    global phone

    phone = request.form['Phone']
    if bool(re.match(phone_pattern, phone)):
        otp_verifier.send_otp(phone_number=phone)
    else:
        phone = f'+91 {phone}'
        otp_verifier.send_otp(phone_number=phone)
    return render_template('verify.html')


@app.route('/verify', methods=['POST'])
def verify():
    entered_otp = request.form['OTP']
    otp_verification = otp_verifier.check_otp(entered_otp)
    if otp_verification:
        return render_template('successful.html')
    else:
        return render_template('failure.html')


@app.route('/', methods=['GET'])
def verification():
    return render_template('index.html')


app.run(debug=True)