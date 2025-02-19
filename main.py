# Higher or lower game is a guessing game in which 2 random people are picked from game data file
# Different from solution due to code structure, no usage of global variables, which lead to a lot of parameters being passed
import game_data
import logic
import data_manager

def main():
    # current_list = game_data.data # make a copy of the game data.... # this doesn't work because it doesn't create a new list but it creates a reference to the origiion
    current_list = game_data.data.copy()
    points = 0
    a_index = logic.left(len(current_list))
    print("Lets start a new game!")
    while True: # Game Loop
        points += 1
        b_index = logic.right(a_index, len(current_list))
        a_followers, a_name = logic.save(a_index, current_list)
        b_followers, b_name = logic.save(b_index, current_list)
        guess = logic.ask(a_name, b_name)
        result = logic.compare(a_followers, b_followers, guess,  points, ) # program stops here if user loses
        # remove loser
        data_manager.updated_list(result, guess, a_index, b_index, current_list)
        # print(len(current_list))
        if len(current_list) == 0: # prevent out of bounds errors
            print("You beat every level! Game win!")
            break

##### function calls
if __name__ == "__main__":
    main()


