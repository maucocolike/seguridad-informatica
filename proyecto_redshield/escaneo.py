import socket
from scapy.all import ARP, Ether, srp

def escanear_red(rango_ip="10.16.32.0/21"): #cambiar según la red local
    paquetes = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=rango_ip)
    resultado = srp(paquetes, timeout=2, verbose=0)[0]

    dispositivos = []
    for envio, respuesta in resultado:
        try:
            nombre = socket.gethostbyaddr(respuesta.psrc)[0]
        except socket.herror:
            nombre = "Desconocido"

        dispositivos.append({
            'ip': respuesta.psrc,
            'mac': respuesta.hwsrc,
            'host': nombre
        })

    return dispositivos
