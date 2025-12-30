### BlackJack Project
Programming Languages: Python

## Description
A blackjack card game played between the __user__ and a __dealer__. The program will prompt the user if they would like to initiate a game ('y' or 'n'). In this instance, if an invalid input is recorded, the statement "Invalid input. Please enter 'y' or 'n'." will be returned. 

Once the <u>user</u> selects 'y', the <u>user</u> is welcomed to the game and presented with a balance of $1000 to bet with. The bet placed will then be recorded and the game will commence. The <u>dealer</u> reveals the first two cards to the <u>user</u> and reveals their first card as well. After the cards are revealed, the <u>user</u> has the choice of adding another card to their hand. Once the <u>user</u> is satisfied with their hand, the dealer will then deal cards until their amount reaches at least 17. If either party goes over the score 21, the other representative wins the <u>bet</u>. In the case that both parties end up in a tie, the <u>bet</u> is cancelled and <u>user</u> ends up with their original balance before the <u>bet</u>.

In order to replicate the feeling of playing against a <u>dealer</u>, I implemented the <u>random</u> module and created a method that deals cards from Ace to the King randomly. 
