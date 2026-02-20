import numpy as np
import pandas as pd

# Define the possible triples of colors (red and black)
TRIPLES = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
TRIPLES_PAIRS =[(t1, t2) for t1 in TRIPLES for t2 in TRIPLES if t1 != t2]
NUM_TRIPLES_PAIRS = len(TRIPLES_PAIRS)

def load_data(file_path: str) -> np.ndarray:
    """Loads a dataset of card sequences from a specified file path.
    Args:
        file_path (str): The path to the file containing the dataset.
    Returns:
        np.ndarray: A numpy array containing the loaded card sequences.
    """
    data = np.load(file_path)
    return data



def hn_game(deck: np.ndarray, p1_triple: tuple, p2_triple: tuple) -> np.ndarray:
    """The HN Randomness game is played as follows, with a traditional deck of cards, where each player
    selects a triple of the colors black and red (e.g. RBR, BBB, BRR). 
    Turn the cards over one at a time, placing them in a line, until one of the chosen triples appears. 
    The winning player takes the upturned cards, having won that trick. 
    The game continues with the rest of the unused cards, with players collecting tricks as their triples come up, until all the cards in the pack have been used. 
    The winner of the game is the player that has won the most tricks.
    Args:
        data (np.ndarray): A numpy array of shape (num_samples, 52) containing the card sequences for each sample.
    """
    
    #Initialize the scores for both players to zero
    p1_score = 0
    p2_score = 0

    #Validate the input triples for both players to ensure they are valid and not the same
    if p1_triple not in TRIPLES or p2_triple not in TRIPLES:
        raise ValueError("Invalid triple. Please choose from the following: (0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1).")
    
    elif p1_triple == p2_triple:
        raise ValueError("Both players cannot choose the same triple. Please choose different triples for each player.")
    
    #Iterate through the deck of cards, checking for the presence of either player's chosen triple.
    card_num=0
    while card_num<50:
        triple = tuple(deck[card_num:card_num+3])
        
        #If player 1's triple is found, increment player 1's score and move the card number forward by 2 to skip the next two cards (as they are part of the triple).
        #If player 2's triple is found, increment player 2's score and move the card
        if triple == p1_triple:
            p1_score+=1
            card_num+=2
        
        elif triple == p2_triple:
            p2_score+=1
            card_num+=2
        
        card_num+=1
    
    #Return the final scores for both players as a dictionary
    return [(p1_triple,p2_triple), (p1_score,p2_score)]

def ronzor_game(deck: np.ndarray, p1_triple: tuple, p2_triple: tuple) -> np.ndarray:
    """The Ronzor game is played as follows, with a traditional deck of cards, where each player
    selects a triple of the colors black and red (e.g. RBR, BBB, BRR). 
    Turn the cards over one at a time, placing them in a line, until one of the chosen triples appears. 
    The winning player takes the upturned cards, having won that trick valued with the number of the cards within it. 
    The game continues with the rest of the unused cards, with players collecting tricks as their triples come up, until all the cards in the pack have been used. 
    The winner of the game is the player that has won the most cards.
    Args:
        data (np.ndarray): A numpy array of shape (num_samples, 52) containing the card sequences for each sample.
    """
    
    #Initialize the scores for both players to zero
    p1_score = 0
    p2_score = 0

    #Validate the input triples for both players to ensure they are valid and not the same
    if p1_triple not in TRIPLES or p2_triple not in TRIPLES:
        raise ValueError("Invalid triple. Please choose from the following: (0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1).")
    
    elif p1_triple == p2_triple:
        raise ValueError("Both players cannot choose the same triple. Please choose different triples for each player.")
    
    #Iterate through the deck of cards, checking for the presence of either player's chosen triple.
    card_num=0
    len_trick=0
    while card_num<50:
        triple = tuple(deck[card_num:card_num+3])
        len_trick += 1
        #If player 1's triple is found, increment player 1's score and move the card number forward by 2 to skip the next two cards (as they are part of the triple).
        #If player 2's triple is found, increment player 2's score and move the card
        if triple == p1_triple:
            p1_score+=len_trick
            card_num+=2
            len_trick=0
        
        elif triple == p2_triple:
            p2_score+=len_trick
            card_num+=2
            len_trick=0
        
        card_num+=1
    
    return [(p1_triple,p2_triple), (p1_score,p2_score)]

def play_games(file_path: str, random_state: int = None) -> list:
    """Simulates a specified number of HN Randomness games and calculates the average score for each possible triple of colors.
    Args:
        file_path (str): The path to the file containing the dataset.
        random_state (int, optional): A random seed for reproducibility. Defaults to None.
    Returns:
        dict: A dictionary containing the average score for each possible triple of colors.
    """
    # Initialize the random number generator with the provided random state for reproducibility
    if random_state is not None:
        rng= np.random.default_rng(seed=random_state)
    else:
        rng= np.random.default_rng()

    #load the dataset of card sequences from the specified file path
    data=load_data(file_path)
    
    #Determine the number of games to simulate based on the number of card sequences in the dataset
    num_decks=data.shape[0]

    #Initialize a list to hold the results of each game, where each result is a dictionary containing the scores for both players based on their chosen triples.
    results_hn=[0]*num_decks*NUM_TRIPLES_PAIRS
    results_ron=[0]*num_decks*NUM_TRIPLES_PAIRS
    for i, deck in enumerate(data):
        for j, (p1_triples, p2_triples) in enumerate(TRIPLES_PAIRS):
            results_hn[i*NUM_TRIPLES_PAIRS + j] = hn_game(deck, p1_triples, p2_triples)
            results_ron[i*NUM_TRIPLES_PAIRS + j] = ronzor_game(deck, p1_triples, p2_triples) 
    return results_hn, results_ron
def summarize_results(results: list) -> pd.DataFrame:
    """Summarizes the results of multiple Penney games by calculating the win probability for each possible triple of colors.
    Args:
        results (list): A list of lists containing the scores for each game.
    Returns:
        pd.DataFrame: A DataFrame containing the win probability for each possible triple of colors.
    """
    #Initialize a DataFrame to hold the win probability for each possible triple of colors
    wins_arr = np.array([[0]*len(TRIPLES) for _ in range(len(TRIPLES))])
    ties_arr = np.array([[0]*len(TRIPLES) for _ in range(len(TRIPLES))])

    #Accumulate the scores for each game by iterating through the results and updating the corresponding entries in the DataFrame
    for result in results:
        wins_arr[TRIPLES.index(result[0][0]), TRIPLES.index(result[0][1])] += int(result[1][0]>result[1][1])
        if result[1][0] == result[1][1]:
            ties_arr[TRIPLES.index(result[0][0]), TRIPLES.index(result[0][1])] += 1
    return wins_arr, ties_arr

def save_data(results: np.array, file_path: str) -> None:
    """Saves the results of multiple Penney games to a specified file path.
    Args:
        results (list): A list of lists containing the scores for each game.
        file_path (str): The path to the file where the results will be saved.
    """
    np.save(file_path, results)


