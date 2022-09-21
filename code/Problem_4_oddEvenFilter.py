
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


