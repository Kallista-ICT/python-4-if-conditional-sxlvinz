# Ask for the user birth year
birth_year = int(input("Please enter your birth year (e.g., 1990):"))

# Determine the generation based on the user input
if birth_year < 1946:                           # First threshold condition
    generation = 'Silent Generation'            # Category for the first condition
elif birth_year < 1965:                         # Second threshold condition
    generation = 'Baby Boomer'                  # Category for the second condition
elif birth_year < 1981:                         # Third threshold condition
    generation = 'Generation X'                 # Category for the third condition
elif birth_year < 1997:                         # Fourth threshold condition
    generation = 'Millennials'                  # Category for the fourth condition
elif birth_year < 2013:                         # Fifth threshold condition
    generation = 'Generation Z'                 # Category for the fifth condition
else :                                          # Default condition for all the other condition
    generation = 'Generation Alpha'             # Default categories for all the other categories

# Print the identified generation
print(f"Your generation is: {generation}")