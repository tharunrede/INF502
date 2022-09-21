def grade_calc(grades_in, to_drop):
    grades_in.sort()         # sorting the grades in ascending order
    avg_mks = sum(grades_in[to_drop:])/len(grades_in[to_drop:])   # calculating the average of the remaing marks after dropping the required number of marks
    
    if avg_mks >= 90 and avg_mks < 100:   # checking if average of marks is greater than or equal to 90 and less than 100
        grade="A"
    elif avg_mks >= 80 and avg_mks < 90:   # checking if average of marks is greater than or equal to 80 and less than 90
        grade="B"
    elif avg_mks >= 70 and avg_mks < 80:   # checking if average of marks is greater than or equal to 70 and less than 80
        grade="C"
    elif avg_mks >= 60 and avg_mks < 70:   # checking if average of marks is greater than or equal to 60 and less than 70
        grade="D"
    else:    # checking if average of marks is less than 60
        grade = "F"
    
    
    return grade      #return grade
       

def main():
    print("print(grade_calc([66,54,89,91],2))")
    print(grade_calc([66,54,89,91],2))       #calling the function
    
    print("print(grade_calc([55,65,75,85,95],3))")
    print(grade_calc([55,65,75,85,95],3))       #calling the function
    
    print("print(grade_calc([54,76,97,99,75],1))")
    print(grade_calc([54,76,97,99,75],1))       #calling the function
    
main()      #calling the main function