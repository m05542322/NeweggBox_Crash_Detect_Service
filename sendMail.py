import smtplib
from email.mime.text import MIMEText

def sendMail(message):

    SMTPserver = '10.16.11.68'
    sender = 'NeweggBox Crash Detect Service'
    email_destination = ['tim.h.huang@newegg.com']
    email_message = message
    subject="NeweggBox Service Crash Alert"

    # typical values for text_subtype are plain, html, xml
    #text_subtype = 'html'
    
    try:
        #msg = MIMEText(email_message, text_subtype)
        msg = MIMEText(email_message)
        msg['Subject'] = subject
        msg['From'] = sender # some SMTP servers will do this automatically, not all
        msg['To'] = ",".join([str(item) for item in email_destination]) # needs to be a string : "a@b.com, b@b.com, c@b.com"

        conn = smtplib.SMTP()
        conn.connect(SMTPserver, 25)
     
        try:
            conn.sendmail(sender, email_destination, msg.as_string())
            print "Email sent success"
        finally:
            conn.close()

    except Exception, exc:
        print "Email sent failed"
        print exc
