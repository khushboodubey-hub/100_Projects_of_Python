# display art 
from art import higher_lower, vs
from game_data import data
import random


def format_data(account):
    """format the account data into printable formate"""
    account_name =account["name"] 
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower count and return if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(higher_lower)
score = 0
game_should_continue = True
account_b = random.choice(data)

# make the game repeatable
while game_should_continue:
# generate a random account from the game data

# making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")

    # ask user for a guess.
    guess = input("Who has more follower? Type 'A' or 'B':")

    # clear the screen
    print("\n" * 20)
    print(higher_lower)

    #check if user is correct .
    # get follower count of each account
    A_follower_count = account_a["follower_count"]
    B_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, A_follower_count, B_follower_count )

    # use if statement to check if user is correct.
    # give user feedback on their guess

    if is_correct:
# score keeping
        score += 1
        print(f"you're right!, Currrent score : {score}")
    else:
        print(f"sorry, that's wrong, Final score : {score}")
        game_should_continue = False












