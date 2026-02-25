import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load processed arrays of wins and ties
def load_arrays(file_path:str) -> np.array:
    '''
    Loads four arrays of card sequences from the data folder.
    Args:
        file_path (str): The path to the file containing the dataset.
    Returns:
        hn_wins (np.array): An array containing the win percentages for each card combination for the original version of the game.
        hn_ties (np.array): An array containing the tie percentages for each card combination for the original version of the game.
        ron_wins (np.array): An array containing the win percentages for each card combination for Ron's version of the game.
        ron_ties (np.array): An array containing the tie percentages for each card combination for Ron's version of the game.
    '''
    hnWin_path = 'data/hn_wins.npy'
    hnTie_path = 'data/hn_ties.npy'
    ronWin_path = 'data/ron_wins.npy'
    ronTie_path = 'data/ron_ties.npy'

    hn_wins = np.load(hnWin_path)
    hn_ties = np.load(hnTie_path)
    ron_wins = np.load(ronWin_path)
    ron_ties = np.load(ronTie_path)

    return hn_wins, hn_ties, ron_wins, ron_ties

def hn_heatmap(hn_wins:np.array, hn_ties:np.array, N_BITS=3) -> np.array:
    '''
    Creates a heatmap out of the array of integers holding the win rates (percentages) for the original game version after scoring all 
    provided decks. Heatmap contains custom annotations, and it contains a masked diagonal because it is impossible for both 
    players to choose the same sequence of red/black cards.

    Args:
        hn_wins (np.array): An array of integers containing the win rates.
        hn_ties (np.array): An array of integers containing the tie rates.
        N_BITS (np.array): An integer value of the number of bits? Default is set to 3.

    Returns:
        String confirming heatmap creation and showing the file path where the heatmap can be found.
    '''
    # The final save path for the heatmap
    hn_save_path = 'figures/hn_Heatmap.svg'

    # Get the number of decks played so far to include in the title of the heatmap
    card_seq_path = 'data/card_sequences'
    card_seq_arr = np.load(card_seq_path)
    total_decks = card_seq_arr.size
    
    # Create annotations
    N_BITS=3
    hn_annot = np.full(shape=hn_wins.shape, fill_value='', dtype='<U6')
    for i in range(2**N_BITS):
        for j in range(2**N_BITS):
            hn_annot[i,j] = f'{round(hn_wins[i,j]*100)}({round(hn_ties[i,j]*100)})'

    # Set diagonal of wins array to NaN to be masked out
    num_col = hn_wins.shape[0]
    for i in range(num_col):
        hn_wins[i,i] = np.nan

    # Convert the wins array into a DataFrame for heatmap creation
    axis_labels = ['BBB','BBR','BRB','BRR','RBB','RBR','RRB','RRR']
    df = pd.DataFrame(hn_wins, columns=axis_labels, index=axis_labels)

    # Create heatmap
    heatmap = sns.heatmap(data=df, annot=hn_annot, annot_kws={"size":7}, fmt='', cmap='Blues', linewidths=0.5, linecolor='white', vmin=0, vmax=1, cbar=False, square=True)
    heatmap.set_facecolor('lightgrey')
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")
    plt.title(f"My Chance of Win(Draw)\nby Cards\nDecks = {total_decks}")
    heatmap.savefig(hn_save_path,dpi=300,bbox_inches='tight')
    
    return(f"Heatmap for original version created. Heatmap saved to {hn_save_path}")

def ron_heatmap(ron_wins:np.array, ron_ties:np.array, N_BITS=3) -> str:
    '''
    Creates a heatmap out of the array of integers holding the win rates (percentages) for Ron's version of the game after scoring all 
    provided decks. Heatmap contains custom annotations, and it contains a masked diagonal because it is impossible for both 
    players to choose the same sequence of red/black cards.

    Args:
        ron_wins (np.array): An array of integers containing the win rates.
        ron_ties (np.array): An array of integers containing the tie rates.
        N_BITS (np.array): An integer value of the number of bits? Default is set to 3.

    Returns:
        String confirming heatmap creation and showing the file path where the heatmap can be found.
    '''
    # The final save path for the heatmap
    ron_save_path = 'figures/ron_Heatmap.svg'

    # Get the number of decks played so far to include in the title of the heatmap
    card_seq_path = 'data/card_sequences'
    card_seq_arr = np.load(card_seq_path)
    total_decks = card_seq_arr.size
    
    # Create annotations
    N_BITS=3
    ron_annot = np.full(shape=ron_wins.shape, fill_value='', dtype='<U6')
    for i in range(2**N_BITS):
        for j in range(2**N_BITS):
            ron_annot[i,j] = f'{round(ron_wins[i,j]*100)}({round(ron_ties[i,j]*100)})'

    # Set diagonal of wins array to NaN to be masked out
    num_col = ron_wins.shape[0]
    for i in range(num_col):
        ron_wins[i,i] = np.nan

    # Convert the wins array into a dataframe for heatmap creation
    axis_labels = ['BBB','BBR','BRB','BRR','RBB','RBR','RRB','RRR']
    df = pd.DataFrame(ron_wins, columns=axis_labels, index=axis_labels)

    # Create heatmap
    heatmap = sns.heatmap(data=df, annot=ron_annot, annot_kws={"size":7}, fmt='', cmap='Blues', linewidths=0.5, linecolor='white', vmin=0, vmax=1, cbar=False, square=False)
    heatmap.set_facecolor('lightgrey')
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")
    plt.title(f"My Chance of Win(Draw)\nby Tricks\nDecks = {total_decks}")
    heatmap.savefig(ron_save_path,dpi=300,bbox_inches='tight')
    
    return(f"Heatmap for Ron's version created. Heatmap saved to {ron_save_path}")