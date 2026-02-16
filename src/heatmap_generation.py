import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data and create Data Frame
def create_dataframe(data_array:np.ndarray) -> pd.DataFrame:
    '''
    Creates a data frame out of the array holding the win rates (percentages) after scoring, with the options 
    for card triples on the axes.

    Arguments:
        data_array (np.ndarray): A numpy array holding the win rates.
    
    Returns:
        data (pd.DataFrame): A pandas data frame holding the win rates
    '''
    wins_df = pd.DataFrame(data_array, columns=['BBB', 'BBR', 'BRB', 'BRR', 'RRR', 'RRB', 'RBR', 'RBB'], index=['BBB', 'BBR', 'BRB', 'BRR', 'RRR', 'RRB', 'RBR', 'RBB'])
    return wins_df

# Create heatmap
def create_heatmap(data:pd.DataFrame, save_path:str) -> str:
    '''
    Creates a heatmap out of the data frame of integers holding the win rates (percentages) after scoring all 
    provided samples.

    Arguments:
        data (pd.DataFrame): A data frame of integers containing the win rates.
        save_path (str): A string of the file path where the heatmap produced will be saved 
        --- should go in the figures folder ---
    
    Returns:
        String: A statement confirming that the heatmap was saved to the filepath provided in the required 
        save_path argument.

        Heatmap will show up as a PNG called "HN_Heatmap_Original.png" (for the original version of the HN game) in 
        the folder identified in the required save_path argument.
    '''
    heatmap = sns.heatmap(data, annot=True, fmt=".2f", cmap='viridis')
    plt.title("Percentage of Games Won (by Choice)")
    plt.xlabel("My choice")
    plt.ylabel("Opponent's choice")

    ### should the filepath just be the figures folder with the name 'HN_Heatmap_Original.png'?
    heatmap.savefig(save_path, dpi=300, bbox_inches='tight') 

    return(f'Heatmap saved to {save_path}.')

