import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path:str) -> pd.DataFrame:
    '''
    Loads a dataset of card sequences from a specified file path.
    Args:
        file_path (str): The path to the file containing the dataset.
    Returns:
        pd.DataFrame: A pandas data frame containing the average scores.
    '''
    df = np.load(file_path)
    return df

# Create heatmap; percentage values could be useful here, for the sake of clarity
def create_heatmap(data:pd.DataFrame) -> str:
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
    heatmap = sns.heatmap(data, annot=True, fmt=".2f", cmap='Blues', vmin=0, vmax=100, cbar=False, square=True)
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")

    #if hn_version = og:
        #plt.title("Percentage of Games Won (by Choice), Original Version")
        #save_path = 'figures/HN_Heatmap_Original.svg'
    #elif hn_version = ron:
        #plt.title("Percentage of Games Won (by Choice), Ron's Version")
        #save_path = 'figures/HN_Heatmap_Ron's.svg'

    heatmap.savefig(save_path, dpi=300, bbox_inches='tight') 

    return(f'Heatmap saved to {save_path}.')

