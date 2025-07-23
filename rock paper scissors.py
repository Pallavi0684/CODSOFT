import random

print("🎮 Welcome to Rock-Paper-Scissors Game!")

# Choices
options = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0
rounds_played = 0

while True:
    print("\n🔄 New Round")
    print("Choose: rock, paper, or scissors")

    # User input
    user_choice = input("Your choice: ").lower()

    if user_choice not in options:
        print("❌ Invalid choice. Please try again.")
        continue

    # Computer choice
    computer_choice = random.choice(options)

    print(f"\n🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round!")
        computer_score += 1

    rounds_played += 1

    # Show score
    print(f"\n📊 Score after {rounds_played} round(s):")
    print(f"🧑 You: {user_score} | 💻 Computer: {computer_score}")

    # Ask to play again
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n👋 Thanks for playing!")
        break

