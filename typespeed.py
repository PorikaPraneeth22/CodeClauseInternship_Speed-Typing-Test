import random
import time
def generate_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells sea shells by the sea shore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "Sally sells seashells by the seashore.",
        "Betty Botter bought some butter, but she said the butter’s bitter.",
        "I scream, you scream, we all scream for ice cream.",
        "Red lorry, yellow lorry, red lorry, yellow lorry.",
        "I wish to wish the wish you wish to wish, but if you wish the wish the witch wishes, I won’t wish the wish you wish to wish."
    ]
    return random.choice(sentences)
def calculate_typing_speed(start_time, end_time, typed_chars):
    total_time = (end_time - start_time) / 60.0  # Convert to minutes
    words_per_minute = len(typed_chars) / 5 / total_time  # Assuming an average word length of 5 characters
    return words_per_minute
def calculate_typing_accuracy(original_sentence, typed_sentence):
    correct_chars = sum(1 for i in range(len(original_sentence)) if original_sentence[i] == typed_sentence[i])
    accuracy = (correct_chars / len(original_sentence)) * 100
    return accuracy
def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start the test...")
    sentence = generate_random_sentence()
    print(f"\nType the following sentence:\n\n{sentence}\n")
    input("Press Enter when you're ready to start typing...")
    start_time = time.time()    
    typed_sentence = input("Start typing here: ")
    end_time = time.time()    
    typing_speed = calculate_typing_speed(start_time, end_time, typed_sentence)
    typing_accuracy = calculate_typing_accuracy(sentence, typed_sentence)
    print("\nTest results:")
    print(f"Typing Speed: {typing_speed:.2f} words per minute")
    print(f"Typing Accuracy: {typing_accuracy:.2f}%")   
if __name__ == "__main__":
    main()