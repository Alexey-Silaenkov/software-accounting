import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send_email:

    # Отправка сообщения на электронную почту
    def send(self, my_email:str, password: str, enemy_email: str, html: str):

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "YCHPO"
        msg['From'] = my_email
        msg['To'] = enemy_email

        part = MIMEText(html, 'html')

        msg.attach(part)

        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()

        mail.starttls()

        mail.login(my_email, password)
        mail.sendmail(my_email, enemy_email, msg.as_string())
        mail.quit()

    # Создание HTML для отправки кода лицензионного ключа
    def kluchHtml(self, kluch: str):
        html = f"""
        <html><body><br><img src=\"https://storage.googleapis.com/thl-blog-production/2017/10/a5d6fc4b-banneri-320x110.jpg\" alt=\"ACORP\"> 
        <br><br>Здравствуйте!
        <br>Ваша заявка была обработана, и мы высылаем вам код активации.
        <br>                                                                                              
        <br>Код активации: 
        <p style="border:2px solid #555; border-radius:5px; width: 200px; text-align:center;  margin:20px; padding:20px;" > {kluch} </p>  
        <br>
        <br>Мы рады, что вы выбрали именно наш программный продукт и желаем Вам приятого пользования!</body></html>
        """
        return html

    # Создание HTML для отправки кода подтверждения возврата пароля
    def codPasseordHtml(self, kod: str):
        html = f"""
        <html><body><br><img src=\"https://storage.googleapis.com/thl-blog-production/2017/10/a5d6fc4b-banneri-320x110.jpg\" alt=\"ACORP\"> 
        <br><br>Здравствуйте!
        <br>Вам выслан код подтверждения для восстановления пароля.
        <br>                                                                                              
        <br>Код активации:  
        <p style="border:2px solid #555; border-radius:5px; width: 200px; text-align:center;  margin:20px; padding:20px;" > {kod} </p>  
        <br>
        <br>Мы рады, что вы выбрали именно наш программный продукт и желаем Вам приятого пользования!</body></html>
        """
        return html
    
        # Создание HTML для отправки кода подтверждения возврата пароля
    
    # Создание HTML для отправки сообщения об ошибке
    def errorHtml(self, user: str, error_value: str):
        html = f"""
        <html><body><br><img src=\"https://storage.googleapis.com/thl-blog-production/2017/10/a5d6fc4b-banneri-320x110.jpg\" alt=\"ACORP\"> 
        <br><br>Здравствуйте!
        <br>Пользователь {user} прислал сообщение об ошибке:
        <br>                                                                                              
        <p style="border:2px solid #555; border-radius:5px; width: 200px; text-align:center;  margin:20px; padding:20px;" > {error_value} </p>  
        <br>
        """
        return html

a = Send_email()
a.send("ychet.po", "swfi ciqc lani rhvm" ,"silaenckov2014@yandex.ru", a.kluchHtml("GTF7-JDHA-0956-KSI7"))