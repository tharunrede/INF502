
## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.

Code:
```python
import math
def pythagoreanTheorem(length_a, length_b):       # creating function signature
    return math.sqrt(length_a**2 + length_b**2)   # calculating the length of Hypotenuse and returning the value

def main():
    print(pythagoreanTheorem(3,4))      #calling the function
    
main()      #calling the main function

```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

Code:

```python

def list_mangler(list_in):      #creating function signature
    output_list=[]      # creating a list to store outputs
    for i in list_in:   # iterating through the list
        if i % 2 == 0:    # checking if the number is even
            output_list.append(i*2)       # doubling the number and adding it to list if it is even
        else:             # checking if the number is odd
            output_list.append(i*3)     # Tripling the number and adding it to list if it is odd
    return output_list   

def main():
    print(list_mangler([1,2,3,4]))      #calling the function
    
main()      #calling the main function

```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

Code:

```python

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
    print(grade_calc([66,54,89,91],2))      #calling the function
    
main()      #calling the main function

```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

For example:
```python

def odd_even_filter(numbers):    # creating function signature
    even=[]  # creating emplyt list to add even numbers
    odd=[]   # creating emplyt list to add odd numbers
    
    for i in numbers:    #iterating through the list
        if i%2==0:    # checking if the number is even
            even.append(i)     # add number to even list if it is even
        else:            # checking if the number is odd
            odd.append(i)          # add number to odd list if it is odd
    

    return even, odd            # Returning the lists
       

def main():    
    print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))      #calling the function
    
main()      #calling the main function




```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).
