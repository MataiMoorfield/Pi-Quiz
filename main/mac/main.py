import getch
import sys

def load_pi_digits(filename):
    """Load pi digits from a text file."""
    with open(filename, 'r') as file:
        pi_digits = file.read().replace('\n', '')
    return pi_digits

def main():
    pi_digits = load_pi_digits('pi.txt')
    pi_digits = pi_digits[2:]
    print("Welcome to the Pi Memory Game!")
    print("Enter the digits of pi. Let's see how many you can get right.")
    print("3. ")

    correct_digits = 0
    for i, digit in enumerate(pi_digits):
        user_input = getch.getch()
        if user_input == digit:
            correct_digits += 1
            print(user_input, end='', flush=True)
        else:
            print("\nIncorrect! Game over.")
            break

    print(f"\nYour score: {correct_digits} digits of pi.")

if __name__ == "__main__":
    main()
