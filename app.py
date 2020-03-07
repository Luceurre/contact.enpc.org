from flask import Flask, request
import ssl
import smtplib

port = 465  # For SSL
password = 'aizahC6g'
host = 'boyer2.enpc.fr'
user = 'clubinfo@enpc.fr'

context = ssl.create_default_context()
server = smtplib.SMTP_SSL(host, port, context=context)
server.login(user, password)

app = Flask(__name__)

@app.route('/sendmail', methods=['POST'])
def send_mail():
    #server.sendmail(user, user, str(request.form))
    print(str(request.form['name']))

    return "Mail send sucessfully."


if __name__ == '__main__':
    app.run(host='0.0.0.0')
