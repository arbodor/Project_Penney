import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TRIPLES = ['BBB','BBR','BRB','BRR','RBB','RBR','RRB','RRR']
# TRIPLES = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]

# Load processed arrays of wins and ties
def load_data(file_path:str) -> pd.DataFrame:
    '''
    Loads four arrays of card sequences from the data folder.
    Args:
        file_path (str): The path to the file containing the dataset.
    Returns:
        og_wins (pd.DataFrame): A data frame containing the win percentages for each card combination for the original version of the game.
        og_ties (pd.DataFrame): A data frame containing the tie percentages for each card combination for the original version of the game.
        ron_wins (pd.DataFrame): A data frame containing the win percentages for each card combination for Ron's version of the game.
        ron_ties (pd.DataFrame): A data frame containing the tie percentages for each card combination for Ron's version of the game.
    '''
    hnWin_path = 'data/hn_wins.npy'
    hnTie_path = 'data/hn_ties.npy'
    ronWin_path = 'data/ron_wins.npy'
    ronTie_path = 'data/ron_ties.npy'

    hn_wins = np.load(hnWin_path)
    hn_ties = np.load(hnTie_path)
    ron_wins = np.load(ronWin_path)
    ron_ties = np.load(ronTie_path)

    return

# Create heatmap; percentage values could be useful here, for the sake of clarity
def hn_heatmap(win_data:pd.DataFrame, tie_data:pd.DataFrame) -> str:
    '''
    Creates a heatmap out of the data frame of integers holding the win rates (percentages) after scoring all 
    provided samples.

    Arguments:
        data (pd.DataFrame): A data frame of integers containing the win rates.
    
    Returns:
        String: A statement confirming that the heatmap was saved to the filepath provided in the required 
        save_path argument.

        Heatmap will show up as a PNG called "HN_Heatmap_Original.png" (for the original version of the HN game) in 
        the folder identified in the required save_path argument.
    '''
    # need to add custom annotations
    save_path = 'figures/hn_Heatmap.svg'
    heatmap = sns.heatmap(win_data, annot=True, fmt=".2f", cmap='Blues', vmin=0, vmax=100, cbar=False, square=True)
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")
    plt.title("Percentage of Games Won (by Choice), Original Version")
    heatmap.savefig(save_path, dpi=300, bbox_inches='tight') 

    return(f'Heatmap saved to {save_path}.')

def ron_heatmap():
    pass
        #elif hn_version = ron:
        #plt.title("Percentage of Games Won (by Choice), Ron's Version")
        #save_path = 'figures/Ron_Heatmap.svg'