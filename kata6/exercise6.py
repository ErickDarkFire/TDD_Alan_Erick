"""
Alan Alejandro Rodriguez Avalos
Erick Eduardo Rodriguez Gomez 

Exercise6
"""
import csv
from datetime import datetime
from pathlib import Path

def load_csv_data(test_input):
    with open('kata6.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['input'] == test_input:
                return (row['input'],row['expected_result'])
"""
Como se va a leer el input:
D - Llamada a la funcion deposit para hacer un deposito y registrarlo en el archivo
W - Llamada a la funcion withdraw para hacer un retiro y registrarlo en el archivo
P - Llamada a la funcion printStatement de los movimientos hasta el momento

En cada test case va a haber una lista con todos los movimientos, en cada elemento 
al incio va a haber una letra indicando que opcion se debe hacer
"""
class Banking:
    movements = []

    def deposit(amount):
        ruta = Path("kata6/table.txt")
        ahora = datetime.now().strftime("%d/%m/%Y")
        saldo_anterior = 0.0

        if ruta.exists() and ruta.stat().st_size > 0:
            with open(ruta, "r") as f:
                lineas = f.readlines()
                if lineas:
                    ultima_linea = lineas[-1].strip()
                    datos = ultima_linea.split(',')
                    saldo_anterior = float(datos[2])
        nuevo_saldo = saldo_anterior + amount
        with open(ruta, "a") as f:
            f.write(f"{ahora},{amount:.2f},{nuevo_saldo:.2f}\n")
        
    def withdraw(amount):
        ruta = Path("kata6/table.txt")
        ahora = datetime.now().strftime("%d/%m/%Y")
        saldo_anterior = 0.0

        if ruta.exists() and ruta.stat().st_size > 0:
            with open(ruta, "r") as f:
                lineas = f.readlines()
                if lineas:
                    ultima_linea = lineas[-1].strip()
                    datos = ultima_linea.split(',')
                    saldo_anterior = float(datos[2])
        nuevo_saldo = saldo_anterior - amount
        with open(ruta, "a") as f:
            f.write(f"{ahora},{-amount:.2f},{nuevo_saldo:.2f}\n")

    def printStatement():
        ruta = Path("kata6/table.txt")        
        print("    DATE    |   AMOUNT   |   BALANCE ")
        
        if not ruta.exists() or ruta.stat().st_size == 0:
            print("No hay movimientos registrados.")
            return

        with open(ruta, "r") as f:
            lineas = f.readlines()
            
            for linea in reversed(lineas):
                datos = linea.strip().split(',')
                if len(datos) == 3:
                    fecha, amount, saldo = datos
                    monto = float(amount)
                    sal = float(saldo)
                    print(f"{fecha:<11}|{monto:>12.2f}|{sal:>12.2f}")

"""
Probando las funciones, ejemplo
Banking.deposit(100)
Banking.withdraw(50)
Banking.printStatement()
"""