
import mailer


class SMS_Mailer(object):

    def __init__(self, _from):
        self.message = mailer.Message()
        self.message.From = _from
        self.sender = mailer.Mailer('sms.cellinkgy.com')

    def send_sms(self, recipients, subject, message):
        for recipient in recipients:
            self.message.To = self.build_email(recipient)
            self.message.Subject = subject
            self.message.Body = message
            self.sender.send(self.message)
            print "Message sent to " + self.message.To

    def build_email(self, number):
        if len(number) == 10:
            return number+"@sms.cellinkgy.com"
        if len(number) == 7:
            return "592"+number+"@sms.cellinkgy.com"
        raise NameError('IncorrectNumberFormat')

    # emails = ["5926171959@sms.cellinkgy.com","5926144859@sms.cellinkgy.com","5926240132@sms.cellinkgy.com","5926486149@sms.cellinkgy.com","5926516908@sms.cellinkgy.com"]
