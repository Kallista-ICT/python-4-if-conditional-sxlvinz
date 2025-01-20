# Step 1: Get the grade from the user  
user_grade = int(input("Enter your grade: "))  

# Step 2: Determine the grade symbol  
if user_grade < 60:  
    category_name = "F"  
elif user_grade >= 60:  
    category_name = "D"  
elif user_grade >= 70:  
    category_name = "C"  
elif user_grade >= 80:  
    category_name = "B"  
elif user_grade >= 90:  
    category_name = "A"  

# Step 3: Print the grade symbol  
print(f"Your grade symbol is: {category_name}")  