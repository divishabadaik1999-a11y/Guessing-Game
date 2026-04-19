import random

number = random.randint(1, 10)
attempts = 3

print("🎮 Guess the number between 1 and 10")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You win!")
        break
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

if attempts == 0:
    print("😢 Game Over! The number was", number)