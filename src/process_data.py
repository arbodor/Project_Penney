import numpy as np
import pandas as pd

# Define the possible triples of colors (red and black)
TRIPLES = ['BBB','BBR','BRB','BRR','RRR','RRB','RBR','RBB']

def load_data(file_path: str) -> np.ndarray:
    """Loads a dataset of card sequences from a specified file path.
    Args:
        file_path (str): The path to the file containing the dataset.
    Returns:
        np.ndarray: A numpy array containing the loaded card sequences.
    """
    data = np.load(file_path)
    return data



def hn_game(deck: np.ndarray, p1_triple: str, p2_triple: str) -> np.ndarray:
    """The HN Randomness game is played as follows, with a traditional deck of cards, where each player
    selects a triple of the colors black and red (e.g. RBR, BBB, BRR). 
    Turn the cards over one at a time, placing them in a line, until one of the chosen triples appears. 
    The winning player takes the upturned cards, having won that trick. 
    The game continues with the rest of the unused cards, with players collecting tricks as their triples come up, until all the cards in the pack have been used. 
    The winner of the game is the player that has won the most tricks.
    Args:
        data (np.ndarray): A numpy array of shape (num_samples, 52) containing the card sequences for each sample.
    """
    p1_triple = p1_triple.upper()
    p2_triple = p2_triple.upper()

    p1_score = 0
    p2_score = 0

    if p1_triple not in TRIPLES or p2_triple not in TRIPLES:
        raise ValueError("Invalid triple. Please choose from the following: 'BBB','BBR','BRB','BRR','RRR','RRB','RBR','RBB'.")
    elif p1_triple == p2_triple:
        raise ValueError("Both players cannot choose the same triple. Please choose different triples for each player.")
    
    card_num=0
    while card_num<50:
        triple = ''.join(['R' if c == 0 else 'B' for c in deck[card_num:card_num+3]])
        if triple == p1_triple:
            print(f"Player 1's triple {triple} found at card #{card_num+1}")
            p1_score+=1
            card_num+=2
        elif triple == p2_triple:
            print(f"Player 2's triple {triple} found at card #{card_num+1}")
            p2_score+=1
            card_num+=2
        card_num+=1
    
    print(f"Final Score - Player 1: {p1_score}, Player 2: {p2_score}")
    if p1_score > p2_score:
        print("Player 1 wins!")
    elif p2_score > p1_score:  
        print("Player 2 wins!")
    else:
        print("It's a tie!")
    
    return {p1_triple: int(p1_score > p2_score), p2_triple: int(p2_score > p1_score)}

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

    triples_pairs=[(t1, t2) for t1 in TRIPLES for t2 in TRIPLES if t1 != t2]

    results=[0]*num_decks*len(triples_pairs)
    for i, deck in enumerate(data):
        for j, (p1_triples, p2_triples) in enumerate(triples_pairs):
            results[i*len(triples_pairs) + j] = hn_game(deck, p1_triples, p2_triples) 
    return results

def summarize_results(results: list) -> pd.DataFrame:
    """Summarizes the results of multiple HN Randomness games by calculating the average score for each possible triple of colors.
    Args:
        results (list): A list of dictionaries containing the scores for each game.
    Returns:
        pd.DataFrame: A DataFrame containing the average score for each possible triple of colors.
    """
    df = pd.DataFrame(index=TRIPLES, columns=TRIPLES, data=0)
    
    for result in results:
        df.loc[list(result.keys())[0], list(result.keys())[1]] += list(result.values())[0]
    
    df=df/(len(results)/56)
    return df

 


