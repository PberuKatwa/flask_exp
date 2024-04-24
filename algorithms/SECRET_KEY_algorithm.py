import secrets
import string
import datetime


def name_algorithm(name):
    algorithm_digits = str(pow(len(name), 17))
    algorithm_digits_1 = algorithm_digits[:8]
    algo = (name[0] + name[-1] + '#' + algorithm_digits_1 + '#' +
            str(datetime.date.today()) + '#')
    algo_2 = algo + string.digits + string.punctuation + string.ascii_letters

    secret_key_2 = ''
    for character in range(0, 30):
        secret_key_2 = secret_key_2 + secrets.choice(algo_2)

    lower_case = sum(2 for character in secret_key_2 if character.islower())
    upper_case = sum(1 for character in secret_key_2 if character.isupper())
    digit_check = sum(1 for character in secret_key_2 if character.isdigit())

    if lower_case>1 and upper_case>1 and digit_check>2:
        sec_test = secret_key_2

    print(lower_case)

    return sec_test


algorithm_a = name_algorithm('pberu')
algorithm_b = name_algorithm('flask katwa secret key')

print('SECRET_KEY > '+algorithm_a)
print('SECRET_KEY > '+algorithm_b)


