#### used as a helper to remove the loser from the data so that player gets fresh data until win or lose event

def updated_list(result, guess, a_index, b_index, current_list):
    # manage the changing list
    if result == "W":
        if guess == b_index:
            current_list.pop(a_index)
        else:
            current_list.pop(b_index)
    return current_list
