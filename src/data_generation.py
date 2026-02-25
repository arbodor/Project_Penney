import numpy as np
import os

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


def generate_data(num_samples: int, random_state: int = None, save_name: str = None) -> np.ndarray:
    """Generates a dataset of card sequences.
    Each sample in the dataset is a sequence of 52 cards, where each card is represented as 0 (red) or 1 (black).
    The order of the cards in each sequence is shuffled randomly.
    Args:
        num_samples (int): The number of samples to generate.
        random_state (int, optional): A seed for the random number generator to ensure reproducibility. Defaults to None.
        save_name (str, optional): The name of the file to save the generated dataset. Defaults to None.
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

    #Save the generated dataset to a file if a save name is provided
    if save_name is not None:
        if os.path.exists(f'data/{save_name}'):
            data = np.concatenate([data,np.load(f'data/{save_name}')], axis=0)
        np.save(f'data/{save_name}', data)
    
    return data

