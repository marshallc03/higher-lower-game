# Import random, import game_data, import art, import clear
import random
from game_data import data
from replit import clear
import art


def get_random():
  '''Randomly chooses from a list of entries.'''
  return random.choice(data)

def format_data(options):
  '''From the dictionary, assigns name, description, and country keys to a variable and formats them using an f-string to be used later in the game. '''
  name = options['name']
  description = options['description']
  country = options['country']
  return f"{name}, a {description} from {country}."

def check_answer(guess, a_followers, b_followers):
  '''Determines which option has more followers and returns a boolean.'''
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

def game():
  '''Plays through Higher or Lower game.'''
  game_on = True

  option_a = get_random()
  option_b = get_random()
  score = 0

  while game_on:
    print(art.logo)
    print(f'Your current score is {score}')
    print(f'Choice A: {format_data(option_a)}')
    print(art.vs)
    print(f'Choice B: {format_data(option_b)}')
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(user_guess)
    
    option_a_followers = option_a['follower_count']
    option_b_followers = option_b['follower_count']

    if check_answer(user_guess, option_a_followers, option_b_followers) == True:
      score += 1
      option_a = option_b
      option_b = get_random()
      clear()
    else:
      print(f"Sorry, you guessed incorrectly. Your final score is {score}")
      game_on = False

game()