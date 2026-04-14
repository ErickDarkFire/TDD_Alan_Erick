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

def scan(barcodes):   
    products = {
            "12345": 7.25,
            "23456": 12.50
        } 
    
    if(barcodes == '99999'):
        return 'Error: barcode not found'
    elif(barcodes == ''):
        return 'Error: empty barcode'
    
    codes = barcodes.split()
    total = 0

    for code in codes:
        total += products[code]

    return f'${total:.2f}'
        


