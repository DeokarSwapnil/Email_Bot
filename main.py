import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login('Sender_gmail', 'Email_pass')
    email = EmailMessage()
    email['From'] = 'Sender_gmail'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dude': 'nil.deokar144@gmail.com',
    'a': 'nil.deokar144@gmail.com',
    'b': 'nil.deokar144@gmail.com',
    'c': 'nil.deokar144@gmail.com',
    'd': 'nil.deokar144@gmail.com'
}


def email_info():
    talk('To whom  you have to send mail')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('email sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        email_info()


email_info()