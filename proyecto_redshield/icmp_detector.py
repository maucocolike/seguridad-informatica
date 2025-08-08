from scapy.all import sniff, IP, ICMP, get_if_addr, conf
from registro import registrar_evento

mi_ip = get_if_addr(conf.iface)  

def manejar_paquete(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:  
        ip_origen = pkt[IP].src
        if ip_origen != mi_ip:
            registrar_evento(ip_origen, "Ping sospechoso")

def iniciar_escucha():
    print("🔍 Monitoreando tráfico ICMP...")
    sniff(filter="icmp", prn=manejar_paquete, store=0)
