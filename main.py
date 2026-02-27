from src.process_data import save_data
from src.data_generation import generate_data
from src.process_data import play_games, summarize_results

def main():
    print("Hello from project-penney!")
    generate_data(num_samples=100, random_state=42, save_path='data/card_sequences.npy')
    results_hn, results_ron = play_games(file_path='data/card_sequences.npy', random_state=42)
    wins_hn, ties_hn = summarize_results(results_hn)
    wins_ron, ties_ron = summarize_results(results_ron)
    save_data(wins_hn, 'data/hn_wins.npy')
    save_data(ties_hn, 'data/hn_ties.npy')
    save_data(wins_ron, 'data/ron_wins.npy')
    save_data(ties_ron, 'data/ron_ties.npy')
    



if __name__ == "__main__":
    main()
