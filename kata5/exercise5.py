"""
Alan Alejandro Rodriguez Avalos
Erick Eduardo Rodriguez Gomez 

Exercise5
"""
import csv

def load_csv_data(test_input):
    with open('kata5.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['input'] == test_input:
                return (row['input'],row['expected_result'])

def scan(prices):
    pass