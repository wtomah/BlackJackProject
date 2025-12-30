# BlackJack Project
## Programming Languages
- Python

## Description
This project is a command-line implementation of the Blackjack card game played between a *user* and a *dealer*. The program will prompt the user if they would like to initiate a game ('y' or 'n'). If an invalid input is recorded, the statement "Invalid input. Please enter 'y' or 'n'." will be returned. 

Once the *user* selects 'y', the *user* is welcomed to the game and presented with a balance of **$1000** to bet with. The bet placed will then be recorded and the game will commence. The *dealer* reveals the first two cards to the *user* and reveals their first card as well. After the cards are revealed, the *user* has the choice of adding another card to their hand. Once the *user* is satisfied with their hand, the dealer will then deal cards until their amount reaches at least 17. If either party goes over the score 21, the other representative wins the *bet*. Also, if a representative has a higher number than the other and the number is 21 and under, they will also win the bet and add to their balance. In the case that both parties end up in a tie, the *bet* is cancelled and *user* ends up with their original balance before the *bet*. 

In order to replicate the feeling of playing against a *dealer*, I implemented the built-in *random* module and created a method that deals cards with values ranging from Ace to the King. 

## Features
- Input validation 
- Betting system
- Ace value adjustment
- Dealer logic
- Unit-tested core logic 
