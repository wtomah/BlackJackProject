### BlackJack Project
Programming Languages: Python

## Description
A blackjack card game played between the __user__ and a __dealer__. The program will prompt the user if they would like to initiate a game ('y' or 'n'). In this instance, if an invalid input is recorded, the statement "Invalid input. Please enter 'y' or 'n'." will be returned. 

Once the __user__ selects 'y', the __user__ is welcomed to the game and presented with a balance of $1000 to bet with. The bet placed will then be recorded and the game will commence. The __dealer__ reveals the first two cards to the __user__ and reveals their first card as well. After the cards are revealed, the __user__ has the choice of adding another card to their hand. Once the __user__ is satisfied with their hand, the dealer will then deal cards until their amount reaches at least 17. If either party goes over the score 21, the other representative wins the __bet__. In the case that both parties end up in a tie, the __bet__ is cancelled and __user__ ends up with their original balance before the __bet__.

In order to replicate the feeling of playing against a __dealer__, I implemented the __random__ module and created a method that deals cards from Ace to the King randomly. 
