import random

balance = 1000

class BlackJack:

    @staticmethod
    def deal_card():
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        return random.choice(cards)

    @staticmethod
    def add_card(hand):
        hand.append(BlackJack.deal_card())

    @staticmethod
    def calculate_score(hand):
        if sum(hand) == 21 and len(hand) == 2:
            return 0  # Blackjack
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
        return sum(hand)

    @staticmethod
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It's a draw!"
        elif computer_score == 0:
            return "Computer has Blackjack! You lose."
        elif user_score == 0:
            return "You have Blackjack! You win!"
        elif user_score > 21:
            return "You went over. You lose."
        elif computer_score > 21:
            return "Computer went over. You win!"
        elif user_score > computer_score:
            return "You win!"
        else:
            return "You lose."

    @staticmethod
    def play_game():
        global balance
        print("Welcome to Blackjack!")

        try:
            bet = int(input(f"You have ${balance}. How much would you like to bet? "))
            if bet <= 0 or bet > balance:
                raise ValueError
        except ValueError:
            print("Invalid bet.")
            return

        user_hand = []
        computer_hand = []

        for _ in range(2):
            BlackJack.add_card(user_hand)
            BlackJack.add_card(computer_hand)

        game_over = False

        while not game_over:
            user_score = BlackJack.calculate_score(user_hand)
            computer_score = BlackJack.calculate_score(computer_hand)

            print(f"Your cards: {user_hand}, score: {user_score}")
            print(f"Computer's first card: {computer_hand[0]}")

            if user_score == 0 or user_score > 21:
                game_over = True
            else:
                choice = input("Type 'y' to hit, 'n' to stand: ")
                if choice == 'y':
                    BlackJack.add_card(user_hand)
                    if len(user_hand) == 5:
                        game_over = True
                else:
                    game_over = True

        computer_score = BlackJack.calculate_score(computer_hand)
        while computer_score != 0 and computer_score < 17:
            BlackJack.add_card(computer_hand)
            computer_score = BlackJack.calculate_score(computer_hand)

        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        result = BlackJack.compare(user_score, computer_score)
        print(result)

        if "win" in result:
            balance += bet
        elif "lose" in result:
            balance -= bet

        print(f"Your new balance is: ${balance}")

        if balance == 0:
            print("Game Over!")
            quit()


while input("Do you want to play a game of Blackjack? (y/n): ") == 'y':
    BlackJack.play_game()
