import math
def pythagoreanTheorem(length_a, length_b):       # creating function signature
    return math.sqrt(length_a**2 + length_b**2)   # calculating the length of Hypotenuse and returning the value

def main():
    print("For print(pythagoreanTheorem(3,4))")
    print(pythagoreanTheorem(3,4))
    
    print("For print(pythagoreanTheorem(2,2))")
    print(pythagoreanTheorem(2,2))
    
    print("For print(pythagoreanTheorem(11,12))")
    print(pythagoreanTheorem(11,12))
    
    
main()