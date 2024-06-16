import random
from country_list import countries_for_language

# Get a list of all countries in English
all_countries = countries_for_language('en')

# Randomly select a country
country = random.choice(countries).upper()
country_length = len(country)
guesses = country_length * 2  # Number of allowed guesses
display = ['-' if letter.isalpha() else letter for letter in country]

print(f"Guess the country name: {' '.join(display)}")

while guesses > 0 and '-' in display:
    guess = input("Enter a letter or the country name: ").upper()

    if len(guess) == 1 and guess.isalpha():
        if guess in country:
            print("Correct!")
            for i in range(country_length):
                if country[i] == guess:
                    display[i] = guess
        else:
            print("Incorrect!")
            guesses -= 1
    elif guess == country:
        print("Congratulations! You guessed the country correctly.")
        display = list(country)  # Update display to show the full country name
        break
    else:
        print("That's not the correct country.")
        guesses -= 1

    print(f"{' '.join(display)}")
    print(f"Guesses remaining: {guesses}")

if '-' not in display:
    print("Well done! You guessed the country!")
else:
    print(f"Sorry, you've run out of guesses. The country was {country}.")