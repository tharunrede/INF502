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


