import random

def create_secret_number(length: int) -> list[int]:
    secret_number = []
    for i in range(length):
        new_num = random.choice(range(10))
        secret_number.append(new_num)
    return secret_number
print(create_secret_number(4))
