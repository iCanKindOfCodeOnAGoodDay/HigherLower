# this func is used by logic.py to prevent runtime error caused by invalid user input

def validate(value):
    while True:
        try:
            val = int(value)
            if val < 1 and val > 2:
                raise ValueError
            return value
        except ValueError:
            value = input("Enter a number: ")