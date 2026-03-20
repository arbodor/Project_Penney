# Project_Penney
This is a project for W&M Data440. We will be simulating and visualizing results from two versions of the Humble-Nishiyama Randomness game.    

## Humble-Nishiyama Randomness Game   
The Humble-Nishiyama Randomness Game is similar to Penney's game. In Penney's game, Player 1 chooses any sequence of 3 results from 3 tosses of a fair coin (for example, "HHT" or "THT"). Player 2 then chooses any different sequence. The fair coin is flipped over and over, and the result of each toss is recorded. The first player to have their chosen sequence reflected in the successive coin toss results wins the game. The trick of the game is that, given Player 1's sequence choice, there is always a sequence choice that Player 2 should pick that gives Player 2 a statistically higher chance of winning the game.    
    
In the Humble-Nishiyama Randomness (HN) Game, a deck of cards is used instead of a coin, with red and black cards replacing heads and tails. Note that while coin tosses are all independent of each other, each draw of a card from a deck without replacement is not. Therefore, the win probabilities for the HN game and Penney's game will be different. However, the trick is the same: Player 2 has the advantage because they can choose a more statistically likely sequence if they know what Player 1's sequence is. However, according to mathematicians Steve Humble and Yutaka Nishiyama, the finite nature of the deck of cards makes the advantage much greater; that is, Player 2 is much more likely to win over Player 1 if cards are used instead of a coin. Scoring the HN game goes as follows: when a player's sequence is identified in the random deck, the cards are taken from the deck and recorded as 1 trick. At the end of the deck, each player counts the number of tricks they got. Whoever has more tricks wins the game. This version of the HN game will in these files be known as "by tricks" or "hn version".    
    
In a different version of the HN game (here known as "by cards" or "Ron's version"), when a player's sequence appears in the deck, that player takes their winning sequence cards and all of the cards that have been drawn from the deck since the last trick was scored (by either player). Again, the trick is the same, but the winning probabilities for each combination of player sequence choices is different.

## Our Project
In this project, we simulate both versions of the HN game (by tricks and by cards) and create heat maps to visualize the winning probabilities (and probabilities of a tie) for each combination of player choices.    

**How to run our code**    
Download the GitHub repository and run the following code:    
*uv sync*    
*uv run main.py*    
    
You will be prompted with choices to clear the data folder and to generate a datset of cardsequences and store the results. You will then be prompted to enter the number of decks to generate, and then scoring will take place. Your heat maps will appear in a folder called 'figures' and your card sequences will appear in a folder called 'data' (see below: *Repository Structure*). After generating and scoring the decks, you will be prompted to generate and score additional decks, but this is optional. Note that decks are generated and scored in batches of 50,000.    
    
## Repository Structure    
Our repository is structured as follows:   
* *data* folder    
* *figures* folder    
* *src* folder (source)    
* *main.py* file

The data folder stores both the raw and processed data, including the randomly generated decks used in the simulation. It also stores summaries of the data (Pandas DataFrames storing win probabilities) and the final arrays used to create the heat maps.    

The figures folder stores the final versions of the heat maps. If you decided to generate and score additional decks, only the latest, most up-to-date versions of your heat maps will be stored.    

The source folder stores all source code. There are three .py files in the source folder: *data_generation.py*, *process_data.py*, and *heatmap_generation.py*. These three files, respectively, contain all code for generating the decks and data, playing/scoring both HN game versions and summarizing the results, and generating the heat maps and heat map annotations. In heatmap_generation.py, the function ron_heatmap is scored by cards, and the function hn_heatmap is scored by tricks.    

The *main.py* file is run in your computer's terminal and contains all of the code for prompting the user at the start of the simulation.    

## Results    
Based on the numerical results obtained for 3 million simulated decks, it appears that we likely simulated enough data so that our answers converged as percentages. The symmetry in the numbers that we would expect to see was almost perfect. For example: looking at the heat map for tricks, when I choose RBR and my opponent then chooses RRR, there is a 66% chance of my opponent winning and a 13% chance of a tie. However, if I choose BRB and my opponent then chooses BBB, there is a 67% of my opponent winning and a 12% chance of a tie. The difference between these win and draw values is small; in all cases, whole number percentages are off from their symmetrical counterpart by no more than 1. However, given that black and red cards are equally likely in a standard deck, we would assume that with infinite decks, these probabilities would converge to be equal to each other. Other examples of this near-perfect symmetry can be seen on the heat map for tricks, as well as on the heat map for cards.    

An additional million decks added to the simulation produced identical heat maps for both tricks and cards versions. Additionally, the winning probabilities for tricks almost perfectly match (off by about 1 percentage point) those of the published results provided by Humble and Nishiyama, found here (https://www.futilitycloset.com/2016/12/31/humble-nishiyama-randomness-game/). This additional evidence leads us to believe that the whole number percentage results for 3 million simulated decks have converged.    

Comparing the two versions of the game, it appears that HN by cards produces greater winning probabilities than HN by tricks. For example, according to our results for the combination (BRR/RRR), HN by tricks predicts a 99% win rate and HN by cards predicts an 100% win rate. For a different combination (BBR/RBR), our results show that HN by tricks predicts a 73% win rate and HN by cards predicts a 93% win rate. Not every sequence combination shows a greater win probability in HN by cards than in HN by tricks, but this is the general trend.

### Optimal Strategies    
**By tricks:**
* *Player 1:* Do not choose BBB or RRR. These give your lowest chances of winning.    
* *Player 2:* Take the opposite of the middle value of Player 1's sequence and move it to the beginning of Player 1's sequence. For example, our results show that if Player 1 (My choice) chooses 'BRR', Player 2 (Opponent's choice) should choose 'BBR'. This results in the highest probability of Player 2 winning (88%) and the lowest probability of Player 1 winning (5%). The probabilities for this combination almost perfectly match (off by about 1 percentage point) those of the originally published results, again found here (https://www.futilitycloset.com/2016/12/31/humble-nishiyama-randomness-game/). The results for other combinations also match to within about 1 percentage point.   

**By cards:**
* *Player 1:* Similar to "By tricks" above, do not choose BBB or RRR. These give your lowest chances of winning.
* *Player 2:* Similar to "By tricks" above, take the opposite of the middle value of Player 1's sequence and move it to the beginning of Player 1's sequence. For example, our results show that if Player 1 (My choice) chooses 'RBB', Player 2 (Opponent's choice) should choose 'RRB'. This results in the highest probability of Player 2 winning (96%) and the lowest probability of Player 1 winning (3%).