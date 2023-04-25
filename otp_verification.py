import re

from twilio.rest import Client
import random
import time


class OtpVerifier:
    def __init__(self):
        self.client = Client('AC8245296ff225857167385ceb729da84f', '186ec3b805d942edbe0d0fbaf7557bf6')
        self.otp = self.generate_otp()
        self.time_timer = 10
        otp = self.otp
        self.msg = str(f'Your OTP for Skillz Account Verification is :{otp} and is valid for 10 minutes.')
        self.minuteString = "10"
        self.secondString = "00"

    @staticmethod
    def generate_otp():
        return random.randrange(100000, 1000000)

    def resend_otp(self, number_of_resend):
        if number_of_resend < 6:
            self.send_otp(self.send_otp)
        else:
            return str("You have maximum number of OTPs for Today. Try again Tomorrow.")

    def send_otp(self, phone_number):
        self.client.messages.create(to=phone_number, from_="+15856362567", body=self.msg)

    def check_otp(self, user_input):
        otp = self.otp
        try:
            if str(user_input) == str(otp):
                self.otp = "done"
                return True
            else:
                return False
        except:
            return False

    def is_phone(self, field):
        phone = re.compile(r'(\+91)?(-)?\s*?(91)?\s*?(\d{3})-?\s*?(\d{3})-?\s*?(\d{4})')
        if re.match(phone, field):
            return True
        else:
            return False

    def is_mail(self, field):
        mail = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
        if re.match(mail, field):
            return True
        else:
            return False

    #
    # import time
    #
    # # define the countdown func.
    # def countdown(t):
    #
    #
    #
    #     print('Fire in the hole!!')
    #
    # # input time in seconds
    # t = input("Enter the time in seconds: ")
    #
    # # function call
    # def run_timer(self):
    #     while self.time_timer:
    #         mins, secs = divmod(self.time_timer, 60)
    #         timer = '{:02d}:{:02d}'.format(mins, secs)
    #         print(timer, end="\r")
    #         time.sleep(1)
    #         self.time_timer -= 1


