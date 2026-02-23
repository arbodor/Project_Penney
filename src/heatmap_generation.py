import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_shape(file_path:str) -> int:
    '''
    Load a wins_array from data_generation.py and get the shape of it.
    Args:
        file_path (str): The path to the file containing the wins array.
    Returns:
        total_decks (int): Number of decks, taken from the shape of the wins array.
    '''
    arr = 'data/card_sequences'
    total_decks = arr.size
    return total_decks

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

    return(f'Arrays loaded from {hnWin_path},{hnTie_path},{ronWin_path},{ronTie_path}.')

def hn_annotations(hn_wins:np.array, hn_ties:np.array, N_BITS=3) -> np.array:
    '''
    Creates an array of custom annotations (in the form of 'wins(ties)'for the original version heatmap.
    Args:
        hn_wins (np.array): A numpy array of the win rates for the original game version.
        hn_ties (np.array): A numpy array of the tie rates for the original game version.
        N_BITS (int): number of bits?
    Returns:
        hn_annot (np.array): An array of the custom annotations to go into the hn_heatmap function.
    '''
    N_BITS=3
    hn_annot = np.full(shape=hn_wins.shape, fill_value='', dtype='<U6')
    for i in range(2**N_BITS):
        for j in range(2**N_BITS):
            hn_annot[i,j] = f'{round(hn_wins[i,j]*100)}({round(hn_ties[i,j]*100)})'

    return hn_annot

def ron_annotations(ron_wins:np.array, ron_ties:np.array, N_BITS=3) -> np.array:
    '''
        Creates an array of custom annotations (in the form of 'wins(ties)'for the ron version heatmap.
    Args:
        hn_wins (np.array): A numpy array of the win rates for the ron game version.
        hn_ties (np.array): A numpy array of the tie rates for the ron game version.
        N_BITS (int): number of bits?
    Returns:
        ron_annot (np.array): An array of the custom annotations to go into the ron_heatmap function.
    '''
    N_BITS=3
    ron_annot = np.full(shape=ron_wins.shape, fill_value='', dtype='<U6')
    for i in range(2**N_BITS):
        for j in range(2**N_BITS):
            ron_annot[i,j] = f'{round(ron_wins[i,j]*100)}({round(ron_ties[i,j]*100)})'

    return ron_annot

def hn_heatmap(hn_wins:np.array, hn_ties:np.array, hn_annot:np.array) -> str:
    '''
    Creates a heatmap out of the array of integers holding the original game version win rates (percentages) after scoring all 
    provided samples.

    Arguments:
        data (np.array): An array of integers containing the win rates.
    Returns:
        String: A statement confirming that the heatmap was saved to the filepath provided in the required 
        save_path argument. Heatmap will show up as an SVG called "hn_Heatmap.svg" (for the original version of the HN game) in 
        the folder identified in the required save_path argument.
    '''
    hn_save_path = 'figures/hn_Heatmap.svg'

    axis_labels = ['BBB','BBR','BRB','BRR','RBB','RBR','RRB','RRR']
    df = pd.DataFrame(hn_wins, columns=axis_labels, index=axis_labels)

    heatmap = sns.heatmap(df, annot=hn_annot, fmt='', cmap='Blues', vmin=0, vmax=100, cbar=False, square=False)
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")
    plt.title("My Chance of Win(Draw) by Cards")
    heatmap.savefig(hn_save_path, dpi=300, bbox_inches='tight') 

    return(f'Original version heatmap saved to {hn_save_path}.')

def ron_heatmap(ron_wins:np.array, ron_ties:np.array, ron_annot:np.array) -> str:
    '''
    Creates a heatmap out of the array of integers holding the ron's game version win rates (percentages) after scoring all 
    provided samples.

    Arguments:
        data (np.array): An array of integers containing the win rates.
    Returns:
        String: A statement confirming that the heatmap was saved to the filepath provided in the required 
        save_path argument. Heatmap will show up as an SVG called "ron_Heatmap.svg" (for the original version of the HN game) in 
        the folder identified in the required save_path argument.
    '''
    ron_save_path = 'figures/ron_Heatmap.svg'

    axis_labels = ['BBB','BBR','BRB','BRR','RBB','RBR','RRB','RRR']
    df = pd.DataFrame(ron_wins, columns=axis_labels, index=axis_labels)

    heatmap = sns.heatmap(df, annot=ron_annot, fmt='', cmap='Blues', vmin=0, vmax=100, cbar=False, square=False)
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")
    plt.title("My Chance of Win(Draw) by Tricks, N = {total_decks}")
    heatmap.savefig(ron_save_path, dpi=300, bbox_inches='tight') 

    return(f'Ron version heatmap saved to {ron_save_path}')

# to do: annotations, grey out the diagonal