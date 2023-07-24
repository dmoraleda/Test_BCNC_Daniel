# Biblioteca pyshark.
import pyshark

def buscar_coincidencias(captura_archivo, protocolo, puerto_destino, ip_destino):
    coincidencias = []
    captura = pyshark.FileCapture(captura_archivo)

    # Función que recibe los parámetros y lee la captura de red.
    for paquete in captura:
        if 'ip' in paquete and 'tcp' in paquete:
            ip_destino_actual = paquete.ip.dst
            puerto_destino_actual = paquete.tcp.dstport
            protocolo_actual = paquete.highest_layer

            if (ip_destino_actual == ip_destino and
                    int(puerto_destino_actual) == int(puerto_destino) and
                    protocolo_actual == protocolo):
                # Información a extraer relevante del paquete y se almacena en un listado de diccionario.
                informacion = {
                    'ip_origen': paquete.ip.src,
                    'ip_destino': ip_destino_actual,
                    'puerto_origen': paquete.tcp.srcport,
                    'puerto_destino': puerto_destino_actual,
                    'protocolo': protocolo_actual,
                }
                coincidencias.append(informacion)

    return coincidencias

# Uso del método:
archivo_captura = 'captura_de_red/evidencia.pcap'
protocolo_buscado = 'TCP'
puerto_destino_buscado = 80
ip_destino_buscada = '192.168.240.2'

