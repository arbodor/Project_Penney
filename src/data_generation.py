import numpy as np


def generate_deck(random_state: int = None)-> np.ndarray:
    """Generates a deck of cards represented as a numpy array.
    0 represents a red card and 1 represents a black card.
    The deck consists of 26 red cards and 26 black cards.
    The order of the cards is shuffled randomly. 
    Args:
        random_state (int, optional): A seed for the random number generator to ensure reproducibility. Defaults to None.
    """
    if random_state is not None:
        rng= np.random.default_rng(seed=random_state)
    else:
        rng= np.random.default_rng()

    # Create a deck of cards with 26 red (0) and 26 black (1) cards
    cards=np.array(26*[0]+26*[1])
    
    # Shuffle the deck of cards randomly
    rng.shuffle(cards)

    return cards


def generate_data(num_samples: int, random_state: int = None, save_path: str = None) -> np.ndarray:
    """Generates a dataset of card sequences.
    Each sample in the dataset is a sequence of 52 cards, where each card is represented as 0 (red) or 1 (black).
    The order of the cards in each sequence is shuffled randomly.
    Args:
        num_samples (int): The number of samples to generate.
        random_state (int, optional): A seed for the random number generator to ensure reproducibility. Defaults to None.
        save_path (str, optional): The path to save the generated dataset. Defaults to None.
    Returns:
        np.ndarray: A numpy array of shape (num_samples, 52) containing the generated card sequences.
    """
    
    # Initialize the random number generator with the provided random state for reproducibility
    if random_state is not None:
        rng = np.random.default_rng(seed=random_state)
    else:
        rng = np.random.default_rng()

    # Generate unique seeds for each sample to ensure different shuffling for each deck
    seeds= rng.integers(low=0, high=2**32, size=num_samples)
    
    #Initialize an array to hold the generated data
    data= np.zeros((num_samples, 52), dtype=int)
    
    #Generate the specified number of samples by creating shuffled decks of cards
    for i in range(num_samples):
        deck = generate_deck(random_state=seeds[i])
        data[i] = deck

    #Save the generated dataset to a file if a save path is provided
    if save_path is not None:
        np.save(save_path, data)
    
    return data

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
    # Define the possible triples of colors (red and black)
    triples = ['BBB','BBR','BRB','BRR','RRR','RRB','RBR','RBB']
    if p1_triple not in triples or p2_triple not in triples:
        raise ValueError("Invalid triple. Please choose from the following: 'BBB','BBR','BRB','BRR','RRR','RRB','RBR','RBB'.")
    elif p1_triple == p2_triple:
        raise ValueError("Both players cannot choose the same triple. Please choose different triples for each player.")
    
    for card in range(len(deck)-2):
        triple = ''.join(['R' if c == 0 else 'B' for c in deck[card:card+3]])
        if triple == p1_triple:
            print(f"Player 1's triple {triple} found at card #{card+1}")
            p1_score+=1
        elif triple == p2_triple:
            print(f"Player 2's triple {triple} found at card #{card+1}")
            p2_score+=1
    
    print(f"Final Score - Player 1: {p1_score}, Player 2: {p2_score}")
    if p1_score > p2_score:
        print("Player 1 wins!")
    elif p2_score > p1_score:  
        print("Player 2 wins!")
    else:
        print("It's a tie!")
    
    