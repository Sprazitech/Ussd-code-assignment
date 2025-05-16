pin = 4190
current_balance = 100000
banks = [
    "Access Bank", "Zenith Bank", "GTBank", "First Bank", "Fidelity Bank", "UBA",
    "Union Bank", "Polaris Bank", "Keystone Bank", "Heritage Bank", "Wema Bank",
    "Sterling Bank", "Stanbic IBTC", "Unity Bank", "Providus Bank", "Globus Bank",
    "Titan Trust Bank", "Jaiz Bank", "SunTrust Bank", "Parallex Bank"
] 

disco = ["ekophc", "phphc", "josphc", "ibadanphc", "ikejaphc", "abujaphc", "abaphc", "ogunphc", "deltaphc", "ekitiphc"]

packages = {"Yanga": "1000", "Family": "2500", "Comoact": "5000", "Compact plus": "7000", "Premuim": "10000"}


Option1 = input ("1. Airtime \n2. Transfer \n3. Pay Bills \n4. Pay Bills \n5. Loans. \n\n")
if Option1 == "1":
    Option2 = input ("1. self \n2. Others. \n")
    if Option2 == "1":
        amount = input ("Enter amount: ")
        if current_balance >= int(amount):
            network_provider = input ("1. MTN \n2. Airtel \n3. Glo \n4. Etisalat. \n" )
            if network_provider in ["1", "2", "3", "4"]:
                correct_pin = input ("Enter correct pin: ")
                if pin == int(correct_pin):
                    print("Successful")
                else:
                    print("Invalid pin")  
            else:
                print("Invalid network_provide.")  
        else:
            print("Insufficient balance")        
          
            
    elif Option2 == "2":
        amount = input ("Enter amount: ")
        if current_balance >= int(amount):
            network_provider = input ("1. MTN \n2. Airtel \n3. Glo \n4. Etisalat. \n" )
            if network_provider in ["1", "2", "3", "4"]:
                phone_number = input ("Enter your phone number ")
                if len(phone_number) == 11:
                    correct_pin = input ("Enter correct pin: ")
                    if pin == int(correct_pin):
                        print("Successful")
                    else:
                        print("Invalid pin")    
                else:
                    print("Invalid phone number")   
            else:
                print("Invalid network_provide.")         
        else:
            print("Insufficient balance")            
    else:
        print("Invalid selection")
      
if Option1 == "2":
    Option2 = input ("1. GTB \n2. Others. \n")
    if Option2 == "1":
        amount = input ("Enter amount: ")
        if current_balance >= int(amount):
            account_number = input ("Enter Account number: ")
            if len(account_number) == 10 and account_number.isdigit():
                if account_number[:3] == "003":      #it is assumed gtb acc starts with 003
                    #if account_number.startwith(003)   #Gtb          
                    correct_pin = input("Enter correct pin: ")
                    if pin == int(correct_pin):
                        print("Successful")
                    else:
                        print("Invalid Pin")
                else:
                    print("Invalid GTB Acount number.")
            else:
                print("Account number must be 11 digits..")
        else:
            print("insufficient balance")
            
    elif Option2 == "2":
        select_banks = input("\nEnter name of bank: ")
        if select_banks in banks:
            amount = input ("Enter amount: ")
            if current_balance >= int(amount):
                account_number = input ("Enter Account Number: ")
                if len(account_number) == 10 and account_number.isdigit():
                    correct_pin = input ("Enter correct Pin: ")
                    if pin == int(correct_pin):
                        print("Successful")
                    else:
                        print("Invalid Pin.")
                else:
                    print("Account number must be 10 digits.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid Bank selection.")
    else:
        print("Invalid selection.")
        
        
if Option1 == "3":
    Option3 = input("1. DSTV \n2. Electricity \n")
    if Option3 == "1":
        decorder_number = input("Enter decorde number: ")
        if len(decorder_number) == 10:
            package_input = input("yanga \nfamily. \ncompact. \ncompact plus. \npremium.\n\n")
            if package_input in packages:
                expected_amount = packages[package_input]
                amount = input("Enter amount: ")
                if amount == expected_amount:
                    correct_pin = input("Enter pin: ")
                    if pin == int(correct_pin):
                        if current_balance >= int(amount):
                            print("The", package_input, "subscription is succesful")
                        else:
                            print("Insufficient fund")
                    else:
                        print("Incorrect pin")
                else:
                    print("Invalid amount for", package_input, "subscription")
            else:
                print("Invalid selection")
        else:
            print("invalid Decorder Number")
            
    elif Option3 == "2":
        meter_number = input("Enter meter number: ")
        if len(meter_number) == 11:
            selected_disco = input("1. ekophc\n2. phphc\n3. josphc\n4. ibadanphc\n5. ikejaphc\n6. abujaphc\n7. abaphc\n8. ogunphc\n9. deltaphc\n10. ekitiphc. \n\n")
            if selected_disco in disco:
                amount = input("Enter amount: ")
                if current_balance >= int(amount):
                    correct_pin =input("Enter pin: ")
                    if pin == int(correct_pin):
                        unit_bought = int(amount)/100
                        print("Your",selected_disco, "recharge of ₦",amount, "is successful\nyour unit bought is", unit_bought)
                    else:
                        print("Incorrect pin")
                else:
                    print("Insufficient balance")
            else:
                print("Invalid selection")
        else:
            print("Invalid meter number")
    else:
        print("Invalid selection.")
        
    
                    
            
                
                
                                       
                    
                        
            
        
                            
                            
                        
                
            
                        
                    
                        
        
        

        
                        
               
                    
                    
                        
    
        
