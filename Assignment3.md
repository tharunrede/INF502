# Assignment 3: Python Basics
## Problem 1: Wallets

Write a Python program that request a user to provide numbers representing the value in cash for different wallets. Your program should store these values in a list. The user should be able to add as many values as they want. One example of a filled `wallets` list (in this example, with 5 wallets) would be:

```
print(wallets)

Output: [1023, 984, 192, 1842, 12]
```

After the user adds the values for the wallets, your application should provide the following information:
* The fattest wallet has `$value` in it.
* The skinniest wallet has `$value` in it.
* All together, these wallets have `$value` in them.
* All together, the total value of these wallets is worth `$value` dimes.

Please try to think about different functions to complete your work.

SOURCE CODE: File attached [Here](https://github.com/tharunrede/INF502/blob/main/code/Wallet.py)
```python

wallet=[]                            # creating empty list
#wallet =  [200, 20, 263, 45, 5165, 5455, 54553, 54]
inp= input("Enter amount to add into wallet or say 'DONE': ")          # prompt user to input number or done

while (inp!="DONE"):              # running loop till user enters "DONE"
    
    wallet.append(int(inp))        # adding input to list
    inp= input("Enter amount to add into wallet or say 'DONE': ")          # prompt user to input number or done

print("Wallet = ", wallet)      # printing contents of the list


print("The fattest wallet has", max(wallet),"in it.")              # printing maximum value from the list
print("The skinniest wallet has", min(wallet),"in it.")              # printing minimum value from the list
print("All together, these wallets have", sum(wallet),"in them.")     # printing sum of values from the list

# consider 1 coin is 100 dimes and printing number of dimes in a list
print("All together, the total value of these wallets is worth",sum(wallet)*100,"dimes.")


```

OUTPUT:

```
Enter amount to add into wallet or say 'DONE': 200
Enter amount to add into wallet or say 'DONE': 156
Enter amount to add into wallet or say 'DONE': 65
Enter amount to add into wallet or say 'DONE': 48
Enter amount to add into wallet or say 'DONE': 9
Enter amount to add into wallet or say 'DONE': 5
Enter amount to add into wallet or say 'DONE': 6
Enter amount to add into wallet or say 'DONE': 85
Enter amount to add into wallet or say 'DONE': 15
Enter amount to add into wallet or say 'DONE': 63
Enter amount to add into wallet or say 'DONE': DONE
Wallet =  [200, 156, 65, 48, 9, 5, 6, 85, 15, 63]
The fattest wallet has 200 in it.
The skinniest wallet has 5 in it.
All together, these wallets have 652 in them.
All together, the total value of these wallets is worth 65200 dimes.
```
## Periodic Table 

The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe.
Write a terminal application that lets you enter information about each element in the periodic table.
Make sure you include the following information:
* symbol, name, atomic number, row, and column

You must save the elements in a dictionary where the `symbol` is the key and the other attributes are nested inside `symbol`. The nested keys are `name`, `number`, `row`, `column`.

To populate your dictionary with data, provide a menu of options to the users:

1. Search the element by symbol (see all the details).
2. Search by a property (`name`, `number`, `row`, `column`) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program


SOURCE CODE: File attached [Here](https://github.com/tharunrede/INF502/blob/main/code/periodic_table.py)
```python
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
    
```

OUTPUT: 

```
1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 1
Enter symbol of an element: H
Here are the details about the element you entered
Name of the Element:  Hydrogen
Number of the Element:  1
Row of the Element:  1
Column of the Element:  1

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 1
Enter symbol of an element: Za
Element not present

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 2
Enter which property you want to look up. Input name/ number/ row/ column: name
For symbol H Name of element is: Hydrogen
For symbol He Name of element is: Helium
For symbol Li Name of element is: Lithium
For symbol Be Name of element is: Berylium
For symbol B Name of element is: Boron
For symbol C Name of element is: Carbon

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 2

Enter which property you want to look up. Input name/ number/ row/ column: weight
Invalid property name

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 3

Enter symbol of element you want to add: N
Enter name of the Element: Nitrogen
Enter number of the Element: 7
Enter row of the Element: 2
Enter column of the Element: 15
{'H': {'name': 'Hydrogen', 'number': 1, 'row': 1, 'column': 1}, 'He': {'name': 'Helium', 'number': 2, 'row': 1, 'column': 18}, 'Li': {'name': 'Lithium', 'number': 3, 'row': 2, 'column': 1}, 'Be': {'name': 'Berylium', 'number': 4, 'row': 2, 'column': 2}, 'B': {'name': 'Boron', 'number': 5, 'row': 2, 'column': 13}, 'C': {'name': 'Carbon', 'number': 6, 'row': 2, 'column': 14}, 'N': {'name': 'Nitrogen', 'number': '7', 'row': '2', 'column': '15'}}

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 4

Enter the symbol of element u want to change the property: H
Enter the property u want to change: name
Enter the value of the property: Hydro
{'H': {'name': 'Hydro', 'number': 1, 'row': 1, 'column': 1}, 'He': {'name': 'Helium', 'number': 2, 'row': 1, 'column': 18}, 'Li': {'name': 'Lithium', 'number': 3, 'row': 2, 'column': 1}, 'Be': {'name': 'Berylium', 'number': 4, 'row': 2, 'column': 2}, 'B': {'name': 'Boron', 'number': 5, 'row': 2, 'column': 13}, 'C': {'name': 'Carbon', 'number': 6, 'row': 2, 'column': 14}, 'N': {'name': 'Nitrogen', 'number': '7', 'row': '2', 'column': '15'}}

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 4

Enter the symbol of element u want to change the property: Za
Element not present

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 5

Check Current Directory for the JSON file
{'H': {'name': 'Hydro', 'number': 1, 'row': 1, 'column': 1}, 'He': {'name': 'Helium', 'number': 2, 'row': 1, 'column': 18}, 'Li': {'name': 'Lithium', 'number': 3, 'row': 2, 'column': 1}, 'Be': {'name': 'Berylium', 'number': 4, 'row': 2, 'column': 2}, 'B': {'name': 'Boron', 'number': 5, 'row': 2, 'column': 13}, 'C': {'name': 'Carbon', 'number': 6, 'row': 2, 'column': 14}, 'N': {'name': 'Nitrogen', 'number': '7', 'row': '2', 'column': '15'}}

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 6

Periodic table Imported:  {'N': {'name': 'Nitrogen', 'number': 7, 'row': 2, 'column': 15}, 'O': {'name': 'Oxygen', 'number': 8, 'row': 2, 'column': 16}, 'F': {'name': 'Fluorine', 'number': 9, 'row': 2, 'column': 17}, 'Ne': {'name': 'Neon', 'number': 10, 'row': 2, 'column': 18}, 'Na': {'name': 'Sodium', 'number': 11, 'row': 3, 'column': 1}, 'Mg': {'name': 'magnesium', 'number': 12, 'row': 3, 'column': 2}}

1. Search the element by symbol (see all the details).
2. Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program
Choose your option: 7

```
