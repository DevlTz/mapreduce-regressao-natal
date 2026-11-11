#!/usr/bin/env python3
import sys
from datetime import datetime
 
REF = datetime(2003, 1, 1)  # x = horas desde esta data
 
for linha in sys.stdin.buffer:
    c = linha.decode("latin-1").split(";")
    if len(c) < 10:
        continue  # (REGIAO, UF, ...)
    try:
        data = datetime.strptime(c[0].replace("/", "-"), "%Y-%m-%d")
        hora = int(c[1][:2])  # "00:00" ou "0000 UTC"
        y = float(c[9].replace(",", "."))  # temperatura máxima na hora anterior
    except ValueError:
        continue  # cabeçalho ou dado vazio
    if y == -9999:
        continue  # esse não passa - dado quebrado
 
    delta = datetime(data.year, data.month, data.day, hora) - REF
    x = delta.days * 24 + delta.seconds // 3600
    print("reg\t%d,%s" % (x, y))
