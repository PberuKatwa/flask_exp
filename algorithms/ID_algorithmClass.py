import datetime

class Algorithm:

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