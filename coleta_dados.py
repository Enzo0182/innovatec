import time
import csv
import serial


porta = serial.Serial("COM3", 115200)
arquivo = open("dados.csv", "w", newline='')
writer = csv.writer(arquivo)


header = ["tempo_ms", "sensor_1L", "sensor_2L", "sensor_3L", "sensor_4L", "sensor_5L", "sensor_6L",
          "sensor_1R", "sensor_2R", "sensor_3R", "sensor_4R", "sensor_5R", "sensor_6R","gesto"]
writer.writerow(header)

inicio = time.time()
while True:



