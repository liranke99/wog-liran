def start_play():
    while True:
        print('''Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')

        while True:
            game = input("What is the number of the game you want to play: ")
            if game.isnumeric() and int(game) in [1, 2, 3]:
                game = int(game)
                if game == 1:
                    print("The game you choose is Memory Game!")
                elif game == 2:
                    print("The game you choose is Guess Game!")
                elif game == 3:
                    print("The game you choose is Currency Roulette!")
                break
            else:
                print("Invalid choice. Please select a valid game (1, 2, or 3).")

        while True:
            difficulty = input("Please select a difficulty level (1-5): ")
            if difficulty.isnumeric() and 1 <= int(difficulty) <= 5:
                difficulty = int(difficulty)
                break
            else:
                print("Invalid. Please choose a level between 1 and 5.")

        if game == 1:
            from memory_game import play
            play(difficulty)
        elif game == 2:
            from guess_game import play
            play(difficulty)
        elif game == 3:
            from currency_roulette_game import play
            play(difficulty)

        while True:
            play_again = input("Do you want to play another game? (yes/no): ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == 'no':
            print("Thank you for playing! Goodbye.")
            break
