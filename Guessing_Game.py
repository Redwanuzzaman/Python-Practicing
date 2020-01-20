print("      WELCOME TO GUESSING GAME")
print("***************************************")
print("\n======================================")
print("  Your Hint: A Programming Language")
print("======================================")
secret_word = "Python"
guess_word = ""
guess_count = 0
limit = 5
out_of_chance = False

while guess_word.lower() != secret_word.lower() and not(out_of_chance):
    print("\n##########################")
    print("Remaining Chances: ", end = " ")
    print(limit - guess_count)
    guess_word = input("\nGuess The Word: ")
    guess_count += 1

    if(guess_count >= 5):
        out_of_chance = True
        break;


if out_of_chance:
    print("\nSorry, You are out of chances!\n GAME OVER")
else:
    print("\nCograts! YOU GUESSED IT..!")