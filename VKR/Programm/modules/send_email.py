import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send_email:
    image_ychpo = "https://s666sas.storage.yandex.net/rdisk/9031a3ef37ecad44c80a76c1cac1420520081c3ae331268557cb30fbac0cb344/65a11019/llUCkErYG6RasCml-r7qYjPnoS52r-U062B4_xPadJEFUyi0NUpY-NgraNVquOIzynkri8lMPMQIQG5ZfEcwsQ==?uid=0&filename=Ychpo.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&fsize=4331&hid=046916d0fd23514f1bad862311982ca4&media_type=image&tknv=v2&etag=8045ac143fba7086cc390051edc36213&rtoken=lehyJH1N2uke&force_default=no&ycrid=na-e18914137366099807fe1ead7e6f27fc-downloader1h&ts=60ebcdfe17840&s=34bd560e01ae65a6b981df4be0bf4440e283301bae9a54a68ecdb8495eebf3f2&pb=U2FsdGVkX18uu65tVIiajIwImzRZurH1ORhZrKT4Bgsth4cl2ZDRWqXyeNeKyiy8XFvONJR88hPU9cMGlT_E1CXu_uPPPOgqsIbf1u9QBw8"
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
        <html><body><br><img src=\"{self.image_ychpo}"> 
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
        <html><body><br><img src=\"{self.image_ychpo}" alt=\"Ychpo\"> 
        <br><br>Здравствуйте!
        <br>Вам выслан пароль для вашей учетной записи.
        <br>                                                                                              
        <br>Новый пароль:  
        <p style="border:2px solid #555; border-radius:5px; width: 200px; text-align:center;  margin:20px; padding:20px;" > {kod} </p>  
        <br>
        <br>Мы рады, что вы выбрали именно наш программный продукт и желаем Вам приятого пользования!</body></html>
        """
        return html
    
        # Создание HTML для отправки кода подтверждения возврата пароля
    
    # Создание HTML для отправки сообщения об ошибке
    def errorHtml(self, user: str, error_value: str):
        html = f"""
        <html><body><br><img src=\"{self.image_ychpo}" alt=\"Ychpo\"> 
        <br><br>Здравствуйте!
        <br>Пользователь {user} прислал сообщение об ошибке:
        <br>                                                                                              
        <p style="border:2px solid #555; border-radius:5px; width: 200px; text-align:center;  margin:20px; padding:20px;" > {error_value} </p>  
        <br>
        """
        return html

# a = Send_email()
# a.send("ychet.po", "swfi ciqc lani rhvm" ,"silaenckov2014@yandex.ru", a.kluchHtml("GTF7-JDHA-0956-KSI7"))