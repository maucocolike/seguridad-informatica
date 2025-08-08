from flask import Flask, render_template, send_file
import pandas as pd
from fpdf import FPDF
import csv
from escaneo import escanear_red
from threading import Thread
from icmp_detector import iniciar_escucha

app = Flask(__name__)

def cargar_logs():
    try:
        with open("logs.csv", "r") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        return []

@app.route("/")
def index():
    dispositivos = escanear_red()
    registros = cargar_logs()
    return render_template("index.html", dispositivos=dispositivos, registros=registros)

if __name__ == "__main__":
    Thread(target=iniciar_escucha, daemon=True).start()  # Corre ICMP detector en segundo plano
    app.run(debug=True)
