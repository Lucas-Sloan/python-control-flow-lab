# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    python_is_fun = True
    if python_is_fun == True:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Prompt to enter a letter
    letter = input("Enter a letter: ").lower()  # Convert input to lowercase for simplicity
    
    # Check if single alphabet letter
    if len(letter) == 1 and letter.isalpha():
        # Define vowels
        vowels = "aeiou"
        
        # Check if letter is a vowel or consonant
        if letter in vowels:
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical letter.")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Set the minimum voting age
    voting_age = 18

    try:
        # Prompt to input their age
        age = int(input("Please enter your age: "))

        # Validate input to ensure it's a non-negative number
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        else:
            # Check if the user is old enough to vote
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not old enough to vote.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    try:
        # Prompt the user to enter the dog's age
        dog_age = int(input("Input a dog's age: "))

        # Validate if input is a non-negative number
        if dog_age < 0:
            print("Age cannot be negative. Please enter a valid dog's age.")
        else:
            # Calculate the dog's age in dog years
            if dog_age <= 2:
                # The first two years count as 10 dog years each
                dog_years = dog_age * 10
            else:
                # First two years = 20 dog years, plus 7 dog years for each additional year
                dog_years = 20 + (dog_age - 2) * 7

            # Print age in dog years
            print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Prompt if it's cold
    cold = input("Is it cold? (yes/no): ").lower()
    
    # Prompt if it's raining
    raining = input("Is it raining? (yes/no): ").lower()

    # Provide clothing advice
    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")
    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")
    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")
    elif cold == 'no' and raining == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Define the months and ranges for the seasons
    winter_months = ('Dec', 'Jan', 'Feb', 'Mar')
    spring_months = ('Mar', 'Apr', 'May', 'Jun')
    summer_months = ('Jun', 'Jul', 'Aug', 'Sep')
    fall_months = ('Sep', 'Oct', 'Nov', 'Dec')

    # Prompt month and day
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    try:
        day = int(input("Enter the day of the month: "))

        # Ensure day is valid
        if day < 1 or day > 31:
            print("Invalid day. Please enter a day between 1 and 31.")
            return

        # Determine season
        if (month == 'Dec' and day >= 21) or (month in winter_months and month != 'Mar') or (month == 'Mar' and day <= 19):
            season = 'Winter'
        elif (month == 'Mar' and day >= 20) or (month in spring_months and month != 'Jun') or (month == 'Jun' and day <= 20):
            season = 'Spring'
        elif (month == 'Jun' and day >= 21) or (month in summer_months and month != 'Sep') or (month == 'Sep' and day <= 21):
            season = 'Summer'
        elif (month == 'Sep' and day >= 22) or (month in fall_months and month != 'Dec') or (month == 'Dec' and day <= 20):
            season = 'Fall'
        else:
            print("Invalid input. Please enter a valid date.")
            return

        # Print result
        print(f"{month} {day} is in {season}.")

    except ValueError:
        print("Invalid day. Please enter a valid number for the day.")

# Call the function
determine_season()

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Set a fixed target number for guessing
    target_number = 42
    
    # Inform about the range and number of attempts
    print("Guess a number between 1 and 100. You have 5 attempts.")
    
    # Allow up to 5 attempts
    for attempt in range(1, 6):
        try:
            # Prompt guess input
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            
            # Check if the guess is correct
            if guess == target_number:
                print("Congratulations, you guessed correctly!")
                return  # Exit the function if guess is correct
            elif guess < target_number:
                print("Your guess is too low.")
            elif guess > target_number:
                print("Your guess is too high.")
            
            # Give a last-chance warning on the 5th attempt
            if attempt == 5:
                print("Last chance!")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

    # If the loop completes without a correct guess
    print("Sorry, you failed to guess the number in five attempts.")

# Call the function
guess_number()