score = int(input("Enter your score (0-100): "))  

if score in range(0, 61):  # 0-60: F grade  
    grade = 'F'  
elif score in range(61, 71):  # 61-70: D grade  
    grade = 'D'  
elif score in range(71, 81):  # 71-80: C grade  
    grade = 'C'  
elif score in range(81, 91):  # 81-90: B grade  
    grade = 'B'  
elif score in range(91, 101):  # 91-100: A grade  
    grade = 'A'  
else:  # Invalid score condition  
    grade = 'Invalid score'  

print(f"Your grade is: {grade}")  