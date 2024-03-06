import random

def until_4():
    while True:
        # random int between 1 and 9 (inclusive)
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        C = A*B
        print(f"A={A}, C={C}")
        if C == 4:
            print('\nSuccess!')
            print(f"A = {A}, B = {B}")
            break;
            
until_4()
