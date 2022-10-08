import json              # imprting modules

# creating a dictionary of periodic elements
periodic_table={"H":{"name":"Hydrogen", "number": 1, "row": 1, "column": 1},
                "He":{"name":"Helium", "number": 2, "row": 1, "column": 18},
                "Li":{"name":"Lithium", "number": 3, "row": 2, "column": 1},
                "Be":{"name":"Berylium", "number": 4, "row": 2, "column": 2},
                "B":{"name":"Boron", "number": 5, "row": 2, "column": 13},
                "C":{"name":"Carbon", "number": 6, "row": 2, "column": 14}
                }

# Creating the variable of string
message='''1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program'''

print(message)        # printing the message

inp = int(input("Choose your option: "))    # prompt user to choose an option.

while(inp!=7):           #Running loop till user enters option 7
    
    if inp==1:
        sym=input("Enter symbol of an element: ")    # prompt user to enter an element symbol.
        if sym in periodic_table.keys():           # checking if input in dictionary
            print("Here are the details about the element you entered")
            print("Name of the Element: ", periodic_table[sym]["name"])    # print name of the element.
            print("Number of the Element: ", periodic_table[sym]["number"])    # print Number of the element.
            print("Row of the Element: ", periodic_table[sym]["row"])    # print Row of the element.
            print("Column of the Element: ", periodic_table[sym]["column"])    # print column of the element.
            print()
            print(message)           # printing the message
            inp = int(input("Choose your option: "))    # prompt user to choose an option.
        else:
            print("Element not present")    # print message if symbol not in the dictionary
            print()
            print(message)    # printing the message
            inp = int(input("Choose your option: "))         # prompt user to choose an option.
    
    
    elif inp==2:
        srch = input("Enter which property you want to look up. Input name/ number/ row/ column: ")   # prompt user to choose a property.
        if srch.lower() == "name":                # checking if the property is name
            for i in list(periodic_table.keys()):   # iterating through the list of keys
                print("For symbol", i, "Name of element is:", periodic_table[i]["name"])   # printing name of element 
        elif srch.lower() == "number":                # checking if the property is number
            for i in list(periodic_table.keys()):   # iterating through the list of keys
                print("For symbol", i, "Number of element is:", periodic_table[i]["number"])   # printing number of element 
        
        elif srch.lower() == "row":                # checking if the property is row
            for i in list(periodic_table.keys()):   # iterating through the list of keys
                print("For symbol", i, "Number of element is:", periodic_table[i]["row"])   # printing row of element 
                
        elif srch.lower() == "column":           # checking if the property is column
            for i in list(periodic_table.keys()):   # iterating through the list of keys
                print("For symbol", i, "Number of element is:", periodic_table[i]["column"])  # printing column of element 
        else:
            print("Invalid property name")
        print()
        print(message)               # printing the message
        inp = int(input("Choose your option: "))         # prompt user to choose an option.
        print()    
    elif inp==3:
        
        new_ele=input("Enter symbol of element you want to add: ")    # prompt user to enter element symbol.
        periodic_table[new_ele]={}            # creating dictionary of the element
        #print(periodic_table)
        
        nam=input("Enter name of the Element: ")     #prompt user for name of element
        periodic_table[new_ele]["name"]= nam        # add name to dictionary of that element
        num=input("Enter number of the Element: ")    #prompt user for number of element
        periodic_table[new_ele]["number"]= num        # add number to dictionary of that element
        row=input("Enter row of the Element: ")    #prompt user for row of element
        periodic_table[new_ele]["row"]= row        # add row number to dictionary of that element
        col=input("Enter column of the Element: ")    #prompt user for column of element
        periodic_table[new_ele]["column"]= col        # add column number to dictionary of that element
        
        print(periodic_table)
        print()
        print(message)          # printing the message
        inp = int(input("Choose your option: "))           # prompt user to choose an option.
        print() 
    
    elif inp==4:
        
        ele_name=input("Enter the symbol of element u want to change the property: ")         # prompt user to choose an elemrnt.
        if ele_name in list(periodic_table.keys()):      
            prop_name=input("Enter the property u want to change: ")         # prompt user to choose a property.
            prop_val=input("Enter the value of the property: ")         # prompt user to enter value of the property.
            
            if prop_name in ["number","row","column"]:       # checking if property in "number","row", or "column"
                
                periodic_table[ele_name][prop_name]=int(prop_val)
            
            elif prop_name == "name":                 # checking if property is name
                periodic_table[ele_name][prop_name]=prop_val
            else:
                print("Invalid property name")
            print(periodic_table)
        else:
            print("Element not present")
            
            
        print()    
        
        print(message)    # printing the message
        inp = int(input("Choose your option: "))      # prompt user to choose an option.
        print()
    
    elif inp==5:
        with open('result.json', 'w') as fp:          # creating the file with name result.json
            json.dump(periodic_table, fp)          # enter dictionary into the json file
        print("Check Current Directory for the JSON file")
            
           
        print(periodic_table)
        
        print() 
        print(message)        # printing the message
        inp = int(input("Choose your option: "))      # prompt user to choose an option.
        print()
        
    elif inp==6:
        with open('periodicTableInp.json','r') as json_file: # opening file named "periodicTableInp.json" in read mode
            periodic_table = json.load(json_file) # input json file contents to periodic_table dictionary
        
        #print(temp_table)    
        print()    
        print("Periodic table Imported: ",periodic_table)
        print()
        print(message)  # printing the message
        inp = int(input("Choose your option: "))     # prompt user to choose an option.
        print()
    
    elif inp==7:
        
        break
    else:
        print("Invalid Option")
        print()
        print(message)  # printing the message
        inp = int(input("Choose your option: "))     # prompt user to choose an option.
    
    
    




