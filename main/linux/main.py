import termios
import tty
import sys

def getch():
    """Get a single character without the need to press Enter (Linux)."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    def main():
        pi_digits = load_pi_digits('pi.txt')
        pi_digits = pi_digits[2:]
        print("Welcome to the Pi Memory Game!")
        print("Enter the digits of pi. Let's see how many you can get right.")
        print("3. ")

        correct_digits = 0
        for i, digit in enumerate(pi_digits):
            user_input = getch()
            if user_input == digit:
                correct_digits += 1
                print(user_input, end='', flush=True)
            else:
                print("\nIncorrect! Game over.")
                break

        print(f"\nYour score: {correct_digits} digits of pi.")

    main()
