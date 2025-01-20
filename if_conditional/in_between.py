score = int(input("Enter your score (0-100): "))  

if 0 <= score <= 60:  # 0-60: F grade  
    grade = 'F'  
elif 60 < score <= 70:  # 61-70: D grade  
    grade = 'D'  
elif 70 < score <= 80:  # 71-80: C grade  
    grade = 'C'  
elif 80 < score <= 90:  # 81-90: B grade  
    grade = 'B'  
elif 90 < score <= 100:  # 91-100: A grade  
    grade = 'A'  
else:  # Invalid score condition  
    grade = 'Invalid score'  

print(f"Your grade is: {grade}")  