
## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.

[Code File Here.](https://github.com/tharunrede/INF502/blob/main/code/Problem_1_PythagoreanThoerem.py)

Code:
```python
import math
def pythagoreanTheorem(length_a, length_b):       # creating function signature
    return math.sqrt(length_a**2 + length_b**2)   # calculating the length of Hypotenuse and returning the value

def main():
    print("For print(pythagoreanTheorem(3,4))")    
    print(pythagoreanTheorem(3,4))     #calling the function
    
    print("For print(pythagoreanTheorem(2,2))")
    print(pythagoreanTheorem(2,2))       #calling the function
    
    print("For print(pythagoreanTheorem(11,12))")
    print(pythagoreanTheorem(11,12))     #calling the function
    
    
main()          #calling main function

```
OUTPUT:
```
For print(pythagoreanTheorem(3,4))
5.0

For print(pythagoreanTheorem(2,2))
2.8284271247461903

For print(pythagoreanTheorem(11,12))
16.278820596099706
```


**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

[Code File Here.](https://github.com/tharunrede/INF502/blob/main/code/Problem_2_ListMangler.py)

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
    print("For print(list_mangler([1,2,3,4]))")    
    print(list_mangler([1,2,3,4]))       #calling the function
    
    print("For print(list_mangler([5,10,6,9]))")    
    print(list_mangler([5,10,6,9]))       #calling the function
    
    print("For print(list_mangler([9,13,8,6]))")    
    print(list_mangler([9,13,8,6]))       #calling the function
    
    
    
main()      #calling the main function


```

OUTPUT:
```
For print(list_mangler([1,2,3,4]))
[3, 4, 9, 8]

For print(list_mangler([5,10,6,9]))
[15, 20, 12, 27]

For print(list_mangler([9,13,8,6]))
[27, 39, 16, 12]
```

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

[Code File Here.](https://github.com/tharunrede/INF502/blob/main/code/Problem_3_gradeCalc.py)

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
    print("print(grade_calc([66,54,89,91],2))")
    print(grade_calc([66,54,89,91],2))       #calling the function
    
    print("print(grade_calc([55,65,75,85,95],3))")
    print(grade_calc([55,65,75,85,95],3))       #calling the function
    
    print("print(grade_calc([54,76,97,99,75],1))")
    print(grade_calc([54,76,97,99,75],1))       #calling the function
    
main()      #calling the main function


```

OUTPUT:
```
print(grade_calc([66,54,89,91],2))
A

print(grade_calc([55,65,75,85,95],3))
A

print(grade_calc([54,76,97,99,75],1))
B

```

**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

[Code File Here.](https://github.com/tharunrede/INF502/blob/main/code/Problem_4_oddEvenFilter.py)

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
    print("For print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])")
    print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))    #calling the function
    
    print("For print(odd_even_filter([22,6,58,96,21,55,47,63,22,11])")
    print(odd_even_filter([22,6,58,96,21,55,47,63,22,11]))    #calling the function
    
    print("For print(odd_even_filter([48,36,95,7,2,631,41,85,74])")
    print(odd_even_filter([48,36,95,7,2,631,41,85,74]))    #calling the function
    
main()      #calling the main function


```
OUTPUT:

```
For print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
([98, 50, 90, 2, 56], [71, 39, 79, 5, 89])

For print(odd_even_filter([22,6,58,96,21,55,47,63,22,11])
([22, 6, 58, 96, 22], [21, 55, 47, 63, 11])

For print(odd_even_filter([48,36,95,7,2,631,41,85,74])
([48, 36, 2, 74], [95, 7, 631, 41, 85])
```
