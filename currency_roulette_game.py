import random
import requests

def get_money_interval(difficulty):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_aCiW3v2dTiAkdM4RJM3x0Nzxhvr53Zx2sDawOl35"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["data"]["ILS"]

    usd_amount = random.randint(1, 100)
    total_value = usd_amount * exchange_rate
    lower_bound = total_value - (10 - difficulty)
    upper_bound = total_value + (10 - difficulty)
    return lower_bound, upper_bound, usd_amount

def get_guess_from_user(usd_amount):
    while True:
        try:
            guess = float(input(f"Guess the value of {usd_amount} USD in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def compare_results(lower_bound, upper_bound, user_guess):
    return lower_bound <= user_guess <= upper_bound

def play(difficulty):
    lower_bound, upper_bound, usd_amount = get_money_interval(difficulty)
    user_guess = get_guess_from_user(usd_amount)
    if compare_results(lower_bound, upper_bound, user_guess):
        print("You guessed correctly!")
        return True
    else:
        print("Sorry, that was incorrect.")
        return False
