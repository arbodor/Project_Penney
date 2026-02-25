from src.data_generation import generate_data
from src.process_data import score_and_save

def main():
    print("Hello from project-penney!")
    generate_data(num_samples=1000, random_state=42, save_name='card_sequences1.npy')
    score_and_save(deck_path='card_sequences1.npy')


    generate_data(num_samples=100, random_state=42, save_name='card_sequences2.npy')
    score_and_save(deck_path='card_sequences2.npy')



if __name__ == "__main__":
    main()
