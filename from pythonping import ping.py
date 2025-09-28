from pythonping import ping
from datetime import datetime
import datetime as dt
import time

ip_destino = input('Introduzca IP o hostname: ')

i = 1
path = input('Ruta de destino: ')
current_dt = dt.date.today()
hora_fecha = str(current_dt)
current_datetime = datetime.now()
    # Realiza el ping y espera una respuesta (timeout por defecto)
    # Puedes ajustar el parámetro 'count' para el número de pings
while i >= 0:
    response = ping(ip_destino, count=100)
    t=response.rtt_avg_ms       
    print(f"Haciendo ping a {ip_destino}: Tiempo={t} ms")
    i += 1
    
    hora = current_datetime.strftime("%H-%M-%S")
    hora_actual = time.ctime(time.time())

    if t >= 5:
        hn_txt = open(path + "Log-" + ip_destino + "_" + hora_fecha + "_" + hora + ".txt", "a")   
        hn_txt.write(f"Tiempo: {t} - Latencia alta {hora_actual} \n")

        hn_txt.close()
