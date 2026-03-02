from src.data_generation import generate_data
from src.process_data import score_and_save
from src.heatmap_generation import load_arrays, hn_heatmap, ron_heatmap
import os
def main():
    data_files=[f for f in os.listdir('data')]
    for file in data_files:
        os.remove(f'data/{file}')
    
    print("Hello from project-penney!")
    num_samples=input("Enter the number of samples to generate: ")
    generate_data(num_samples=int(num_samples), random_state=42, save_name='card_sequences1.npy')
    input("Will now score the results of the first batch of games. Press Enter to continue...")
    score_and_save(deck_path='card_sequences1.npy')

    hn_wins, hn_ties, ron_wins, ron_ties, total_decks=load_arrays()
    hn_heatmap(hn_wins=hn_wins, hn_ties=hn_ties,total_decks=total_decks)
    ron_heatmap(ron_wins=ron_wins,ron_ties=ron_ties,total_decks=total_decks)

    num_samples=input("Now try to generate a few more samples: ")
    generate_data(num_samples=int(num_samples), random_state=42, save_name='card_sequences2.npy')
    input("Will now score the results of the second batch of games. Press Enter to continue...")
    score_and_save(deck_path='card_sequences2.npy')
    
    hn_wins, hn_ties, ron_wins, ron_ties, total_decks=load_arrays()
    hn_heatmap(hn_wins=hn_wins, hn_ties=hn_ties,total_decks=total_decks)
    ron_heatmap(ron_wins=ron_wins,ron_ties=ron_ties,total_decks=total_decks)


if __name__ == "__main__":
    main()
