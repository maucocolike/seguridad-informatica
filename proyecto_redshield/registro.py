import csv
from datetime import datetime

def registrar_evento(ip, tipo):
    with open("logs.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, tipo])
