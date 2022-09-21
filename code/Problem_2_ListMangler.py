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