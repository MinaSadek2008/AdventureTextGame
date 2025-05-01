import time
import random

def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)

def start_adventure(score=0):
    has_knife = False
    player_name = input("What is your name? ")
    
    print_pause(f"Welcome, {player_name}!")
    print_pause("You open your eyes.")
    print_pause("You are on a beach.")
    print_pause("The sea is next to you.")
    print_pause("You don’t know how you got here.")
    print_pause("Maybe the water brought you to this island.")
    print_pause("You are alone.")
    print_pause("You must find a way to leave.")
    print_pause("\nLevel 1 – The Beach")
    
    while True:
        choice_1 = input("You see two things:\n1. A jungle path\n2. A broken boat\nWhat do you want to do? (1 or 2): ")
        if choice_1 == '1':
            score += 10
            jungle(score, has_knife)
            break
        elif choice_1 == '2':
            score -= 5
            print_pause("You try to use the boat. It breaks and sinks.")
            print_pause("You swim back to the beach.")
            print_pause("You haven’t found a solution.")
            print_pause("You are forced to enter the jungle to find a solution to escape from this island.")
            jungle(score, has_knife)
            break
        else:
            print_pause("Invalid choice. Please choose either 1 or 2.")

def jungle(score, has_knife):
    print_pause("\nLevel 2 – The Jungle")
    print_pause("The jungle is dark and scary.")
    print_pause("You hear something moving in the trees!")

    knife = input("You find a knife on the ground. Do you want to take it? (yes / no): ")
    if knife.lower() == 'yes':
        score += 10
        has_knife = True
        print_pause("You take the knife.")
    elif knife.lower() == 'no':
        score -= 5
        print_pause("You try to run, but the plants stop you.")
        print_pause("Something scratches your leg.")
        print_pause("Your legs are bleeding.")
    else:
        print_pause("Invalid choice. Please choose 'yes' or 'no'.")
        score -= 5
        jungle(score, has_knife)
        return

    score = random.choice([Tiger, Monkey, Wind])(score, has_knife)
    temple(has_knife, score)

def Monkey(score, *_):
    print_pause("There is a monkey on the tree.")
    print_pause("The monkey threw at you a banana!")
    print_pause("You ate the banana, and gained some energy.")
    score += 5
    return score

def Wind(score, *_):
    print_pause("The trees are moving... What do you think is coming?")
    wind = input("Do you think it's a monster coming to attack you? (yes / no): ")
    if wind.lower() == "yes":
        print_pause("Nothing happened. You scared yourself!")
        score -= 5
    elif wind.lower() == "no":
        print_pause("You are brave. It's just some wind.")
    else:
        print_pause("Invalid choice. Please answer yes or no.")
        score -= 5
    return score

def Tiger(score, has_knife):
    print_pause("Oh no! A tiger launched at you attacking you!")
    if has_knife:
        print_pause("You killed the tiger. Now you are safe.")
        score += 10
    else:
        print_pause("The tiger killed you.")
        print_pause("Game Over.")
        print_pause(f"Your final score is: {score}")
        replay(score)
        return score  # to avoid None if replay ends
    return score

def temple(has_knife, score):
    print_pause("\nLevel 3 – The Temple")
    print_pause("You see an old temple.")
    print_pause("Inside, there is a gold statue on a stone table.")

    while True:
        choice_2 = input("What do you want to do?\n1. Take the statue\n2. Leave it and go out\nWhat do you want to do? (1 or 2): ")
        if choice_2 == '1':
            print_pause("You take the gold statue.")
            score += 15
            print_pause("Suddenly, you hear a loud sound! Rocks fall from the roof!")
            print_pause("You run fast and escape.")
            volcano(True, score)
            break
        elif choice_2 == '2':
            print_pause("You look at the statue... but you walk away.")
            score += 5
            print_pause("You don’t find anything else.")
            volcano(False, score)
            break
        else:
            print_pause("Invalid choice. Please choose either 1 or 2.")
            score -= 5

def volcano(has_statue, score):
    print_pause("\nLevel 4 – The Volcano")
    print_pause("You climb a big mountain.")
    print_pause("It is a volcano.")
    print_pause("You see a helicopter in the sky!")

    if has_statue:
        print_pause("The sun hits the gold statue. It shines bright.")
        print_pause("The helicopter sees it!")
        print_pause("You are saved!")
        score += 20
    else:
        print_pause("You scream and wave...")
        print_pause("But the helicopter doesn’t see you.")
        print_pause("It flies away.")
        print_pause("The volcano explodes and you die.")
        score -= 10

    print_pause(f"Your final score is: {score}")
    replay(score)

def replay(score):
    while True:
        replay_choice = input("Do you want to play again? (yes / no): ")
        if replay_choice.lower() == 'yes':
            start_adventure()
            break
        elif replay_choice.lower() == 'no':
            print_pause("Thanks for playing!")
            break
        else:
            print_pause("Invalid choice. Please choose 'yes' or 'no'.")

# Start the game
start_adventure()
