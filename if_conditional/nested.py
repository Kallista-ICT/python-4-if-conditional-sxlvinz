score = int(input("Enter your score (0-100): "))  

if score >= 0 and score <= 100:  # Check for valid score range  
    if score <= 60:  # 0-60: F grade  
        grade = 'F'  
    else:  # score > 60  
        if score < 70:  # 61-69: D grade  
            grade = 'D'  
        else:  # score >= 70  
            if score < 80:  # 70-79: C grade  
                grade = 'C'  
            else:  # score >= 80  
                if score < 90:  # 80-89: B grade  
                    grade = 'B'  
                else:  # score >= 90  
                    grade = 'A'  
else:  # Invalid score  
    grade = 'Invalid score'  

print(f"Your grade is: {grade}")