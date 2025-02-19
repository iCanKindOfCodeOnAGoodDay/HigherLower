import random
import main
import validation

############# this final contains all the logic and function used in our Game

# display information about both options
def ask(name1, name2):
    print("who has more followers",  str(name1) + " or",  str(name2) + "?")
    print("Just type 1 or 2")
    guess = validation.validate(input("Guess: "))
    return guess

# stops program
def lose(p):
    print("\nNope!")
    print("You Lose! You had " + str(p) + " points\n")
    main.main() # call to main used to restart the game

def win(p):
    print("\nThat is correct!")
    print("You've got ", str(p) + " points\n")
    p +=1
    return p

# needed to match guess to data
def get_guess_index(guess, n, n2):
    if guess == "1":
        guess_index = n
    else:
        guess_index = n2
    return guess_index

def left(list_length):
     index = random.randint(0, list_length - 1)
     return index

# compare to this at this index
def right(first_number, list_length):
    n = random.randint(0, list_length - 1)
    while n == first_number:
        n = random.randint(0, list_length - 1)
    return n

# can be used for both first and second data saving
def save(index, current_list):
    count = int(current_list[index]["follower_count"])
    name = current_list[index]["name"]
    return count, name

# see if guess was correct
def compare(first, second, guess, p):
    if guess == "1":
        # if user guessed 'A', they are correct
        if first > second:
            win(p)
            return "W"
        else:
            lose(p)
    elif guess == "2":
        if first < second:
            win(p)
            return "W"
        else:
            lose(p)
            return "L"
