import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TRIPLES = ['BBB','BBR','BRB','BRR','RBB','RBR','RRB','RRR']
# TRIPLES = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]

# Load processed arrays of wins and ties
def load_arrays(file_path:str) -> pd.DataFrame:
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

# Create heatmap; percentage values could be useful here, for the sake of clarity
def hn_heatmap(hn_wins:np.array, hn_ties:np.array) -> str:
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

    heatmap = sns.heatmap(df, annot=True, fmt=".0f", cmap='Blues', vmin=0, vmax=100, cbar=False, square=False)
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")
    plt.title("My Chance of Win(Draw) by Cards (og)")
    heatmap.savefig(hn_save_path, dpi=300, bbox_inches='tight') 

    return(f'Original version heatmap saved to {hn_save_path}.')

def ron_heatmap(ron_wins:np.array, ron_ties:np.array) -> str:
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

    heatmap = sns.heatmap(df, annot=True, fmt=".0f", cmap='Blues', vmin=0, vmax=100, cbar=False, square=False)
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")
    plt.title("My Chance of Win(Draw) by Tricks (Ron)")
    heatmap.savefig(ron_save_path, dpi=300, bbox_inches='tight') 

    return(f'Original version heatmap saved to {ron_save_path}. Ron version heatmap saved to {ron_save_path}')

# to do: annotations, grey out the diagonal, update title with number of decks played