import csv
import datetime


def generate_unique_id(name, info):
    # Generate unique ID based on client name and additional information
    unique_id_digits = str(len(info) ** 8)
    unique_id = f'#{info[0]}{info[2]}{info[4]}{info[8]}#{unique_id_digits[:3]}#'
    return unique_id


def generate_algorithm(name, info):
    # Generate algorithm based on client name and additional information
    algorithm_digits = str((len(info) + 1) ** 17)[:3]
    algo = f'{name[0]}{name[2]}#{algorithm_digits}#{datetime.date.today()}'
    return algo


# Read data from CSV
with open("csv files/client_data_2.csv", 'r') as client_file:
    client_reader = csv.DictReader(client_file)
    clients = list(client_reader)

unique_id_set = set()  # Use a set for efficient membership testing

for client in clients:
    client_name = client.get('client_name')
    additional_info = client.get('additional_information')

    # Generate unique ID
    unique_id = generate_unique_id(client_name, additional_info)

    # Check for uniqueness and append a counter if necessary
    counter = 1
    while unique_id in unique_id_set:
        unique_id = f'{unique_id[:-1]}{counter}#'
        counter += 1
    print(unique_id_set.add(unique_id))


    # Generate algorithm
    algorithm = generate_algorithm(client_name, additional_info)

    # Process the generated unique ID and algorithm
    print(f'Client: {client_name}, Unique ID: {unique_id}, Algorithm: {algorithm}')
