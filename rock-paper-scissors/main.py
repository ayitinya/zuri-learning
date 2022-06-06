import random

def main():
    running = True
    while running:
        options = ["R", "P", "S"]
        options_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        valid_input = False
        while not valid_input:
            user_input = input("(R)ock (P)aper (S)cissors: ").upper()
            if user_input in options:
                valid_input = True

        cpu_input = random.choice(options)
        print(f"Player ({options_dict[user_input]}): CPU ({options_dict[cpu_input]})")

        if cpu_input != user_input:
            running = False

            if cpu_input == "R" and user_input == "S":
                print("You lose")
            elif cpu_input == "S" and user_input == "R":
                print("You win")
            elif cpu_input == "R" and user_input == "P":
                print("You win")
            elif cpu_input == "P" and user_input == "R":
                print("You lose")
            elif cpu_input == "P" and user_input == "S":
                print("You win")
            elif cpu_input == "S" and user_input == "P":
                print("You lose")
            break
        
        print("It's a tie")
        valid_input = False


if __name__ == "__main__":
    main()

