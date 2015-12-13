import smtplib


def send_email(body):
    mail_user = 'SECRET'
    mail_pwd = 'SECRET'
    _from = 'SECRET'
    _to = 'SECRET'
    _subject = 'New Python jobs for you'
    _text = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (_from, ", ".join(_to), _subject, _text)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mail_user, mail_pwd)
        server.sendmail(_from, _to, message)
        server.close()
        print 'Successfully sent the mail'
    except:
        print "Failed to send mail"
