from src.data_generation import generate_data
from src.process_data import score_and_save
from src.heatmap_generation import load_arrays, hn_heatmap, ron_heatmap
import os
def main():
    
    data_files=[f for f in os.listdir('data')]
    clear_data=input('Would you like to clear the data folder before generating new datasets and scoring the results? (y/n): ')
    if clear_data.lower() == 'y':
        for file in data_files:
            os.remove(f'data/{file}')
    
    sequence_number=len([f for f in os.listdir('data') if f.startswith('card_sequences')])+1
    while True:
        prompt=input('Would you like to generate a dataset of card sequences and score the results? (y/n): ')
        if prompt.lower() != 'y':
            print("Exiting the program. Goodbye!")
            return
        num_samples=input("Enter the number of decks to generate: ")
        if int(num_samples)>50000:
            input("Will now score the results of the new batch of games. Note: Each batch is 50,000 decks. Press Enter to continue...")
            for i in range(int(num_samples)//50000):
                generate_data(num_samples=50000, random_state=42, save_name=f'card_sequences{sequence_number}.npy')
                score_and_save(deck_path=f'card_sequences{sequence_number}.npy')

                hn_wins, hn_ties, ron_wins, ron_ties, total_decks=load_arrays()
                hn_heatmap(hn_wins=hn_wins, hn_ties=hn_ties,total_decks=total_decks)
                ron_heatmap(ron_wins=ron_wins,ron_ties=ron_ties,total_decks=total_decks)
                sequence_number += 1
        else:
            generate_data(num_samples=int(num_samples), random_state=42, save_name=f'card_sequences{sequence_number}.npy')
            input("Will now score the results of the new batch of games. Press Enter to continue...")
            score_and_save(deck_path=f'card_sequences{sequence_number}.npy')

            hn_wins, hn_ties, ron_wins, ron_ties, total_decks=load_arrays()
            hn_heatmap(hn_wins=hn_wins, hn_ties=hn_ties,total_decks=total_decks)
            ron_heatmap(ron_wins=ron_wins,ron_ties=ron_ties,total_decks=total_decks)
            sequence_number += 1


if __name__ == "__main__":
    main()
