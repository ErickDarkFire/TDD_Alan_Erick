"""
Alan Alejandro Rodriguez Avalos
Erick Eduardo Rodriguez Gomez 

Exercise4
"""
import csv

def load_csv_data(test_input):
    with open('kata4.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['input'] == test_input:
                return (row['input'],row['expected_result'])

def search(st):
    city_names = ['Paris', 'Budapest', 'Skopje', 'Rotterdam', 'Valencia', 'Vancouver', 'Amsterdam', 'Vienna', 'Sydney', 'New York City', 'London', 'Bangkok', 'Hong Kong', 'Dubai', 'Rome', 'Istanbul']

    results = []
    if st == "*":
        return city_names
    elif len(st) < 2:
        return "No results"
    elif len(st) >= 2:
        for city in city_names:
            if city.lower().startswith(st.lower()) or city.lower().count(st.lower()) > 0:
                results.append(city)
        return results