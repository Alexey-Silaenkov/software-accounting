import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send_email:

    def send(self, my_email:str, password: str, enemy_email: str):



        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = my_email
        msg['To'] = enemy_email

        # Create the body of the message (a plain-text and an HTML version).
        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        html = """\
        <html>
        <head></head>
        <body>
            <p>Hi!<br>
            How are you?<br>
            Here is the <a href="http://www.python.org">link</a> you wanted.
            </p>
        </body>
        </html>
        """

        
        # htmlBody = "<html><body><br><img src=\"https://storage.googleapis.com/thl-blog-production/2017/10/a5d6fc4b-banneri-320x110.jpg\" alt=\"ACORP\">" + @" 
# <br><br>Здравствуйте!
# <br>Ваша заявка была обработана, и мы высылаем вам код активации.
# <br>                                                                                              
# <br>Код активации:       <b>" + kodemail + @"</b>
# <br>
# <br>Мы рады, что вы выбрали именно наш программный продукт и желаем Вам приятого пользования!</body></html>";

        


        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login(my_email, password)
        mail.sendmail(my_email, enemy_email, msg.as_string())
        mail.quit()



a = Send_email()
a.send("ychet.po", "Qq112233!" ,"silaenckov2014@yandex.ru")