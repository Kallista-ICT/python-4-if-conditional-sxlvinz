# Get the grade from the user as input  
user_grade = input("Enter your grade: ")   

# Determine the grade symbol based on the user's input  
if user_grade >= 90:  # Check if the grade is 90 or above  
    category_name = "A"  
elif user_grade >= 80:  # Check if the grade is 80 or above  
    category_name = "B"  
elif user_grade >= 70:  # Check if the grade is 70 or above  
    category_name = "C"  
elif user_grade >= 60:  # Check if the grade is 60 or above  
    category_name = "D"  
else:  # If none of the above, the grade is below 60  
    category_name = "F"  

# Print the corresponding grade symbol  
print(f"Your grade symbol is: {category_name}")  