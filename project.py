print("\t\t\tWelcome to E-Commerce System")
b=str(raw_input("Enter your name: "))
print("Welcome "+b)
print("Menu:\n1. Customer to customer\n2. Customer to Business\n3. Business to Customer\n4. Business to Business")
a=int(input("Enter a number form above choices: "))
if(a==1):
    print("Welcome to Customer to Customer system")
    print("Here you get various products from different customers")
    print("List of products you can get from customers\n1. Electronic Gadgets\n2. Laptops\n")
    c=int(input("Enter a number from the above: "))
    if(c==1):
        print("Here you can find some branded phones given by some of the used customers\n1. Apple\n2. Redmi\n3. Samsung\n4. Google")
        d=int(input("Enter a number according to brand name: "))
        if(d==1):
            print("You have chosen a phone from Apple Company")
            print("The models availble in Apple are:\n1. iPhone 6\n2. iPhone 6s\n3. iPhone 10\n4. iPhone 11")
            e=int(input("Enter a number from 1 to 4 according to your need: "))
            if(e==1):
                print("You chose iPhone 6 from another customer")
                print("Cost of the phone is Rs 12,000/-")
                print("Your order is successfully placed")
            elif(e==2):
                print("You chose iPhone 6s from another customer")
                print("Cost of the phone is Rs 25,000/-")
                print("Your order is successfully placed")
            elif(e==3):
                print("You chose iPhone 10 from another customer")
                print("Cost of the phone is Rs 45,000/-")
                print("Your order is successfully placed")
            elif(e==4):
                print("You chose iPhone 11 from another customer")
                print("Cost of the phone is Rs 73,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
        elif(d==2):
            print("You have chosen a phone from Redmi Company")
            print("The models availble in Redmi are:\n1. Redmi 3s 6\n2. Redmi Note5 \n3. Redmi 7A\n4. Redmi 4A")
            f=int(input("Enter your choice"))
            if(f==1):
                print("You chose Redmi 3s from another customer")
                print("Cost of the phone is Rs 9,999/-")
                print("Your order is successfully placed")
            elif(f==2):
                print("You chose Redmi Note5 from another customer")
                print("Cost of the phone is Rs 17,899/-")
                print("Your order is successfully placed")
            elif(f==3):
                print("You chose Redmi 7A from another customer")
                print("Cost of the phone is Rs 7,999/-")
                print("Your order is successfully placed")
            elif(f==4):
                print("You chose Redmi 4A from another customer")
                print("Cost of the phone is Rs 8,999/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
        elif(d==3):
            print("You have chosen a phone from Samsung Company")
            print("The models available in Samsung are:\n1. Samsung on5\n2. Samsung on5 pro\n3. Samsung M30")
            g=int(input("Enter your choice"))
            if(g==1):
                print("You chose Samsung on5 from another customer")
                print("Cost of the phone is Rs 8,000/-")
                print("Your order is successfully placed")
            elif(g==2):
                print("You chose Samsung on5 pro from another customer")
                print("Cost of the phone is Rs 10,000/-")
                print("Your order is successfully placed")
            elif(g==3):
                print("You chose Samsung M30 pro from another customer")
                print("Cost of the phone is Rs 15,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
        elif(d==4):
            print("You have chosen a phone from Google company")
            print("Models available in Google are:\n1. Google Pixel\n2. Google Pixel 2")
            h=int(input("Enter your choice :"))
            if(h==1):
                print("You chose Google Pixel from another customer")
                print("Cost of the phone is Rs 26,000/-")
                print("Your order is successfully placed")
            elif(h==2):
                print("You chose Google Pixel 2 from another customer")
                print("Cost of the phone is Rs 27,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
    elif(c==2):
        print("Here you find some laptops from various companies used by another customers")
        print("List of various laptop comapnies:\n1. Lenovo\n2. Dell\n3. HP")
        a1=int(input("Enter your choice:"))
        if(a1==1):
            print("You have chosen a laptop from Lenovo company")
            print("The models available are:\n1. Lenovo XT72U76\n2. Lenovo Idea pad")
            b1=int(input("Enter your choice: "))
            if(b1==1):
                print("You chose Lenovo XT72U76 from another customer")
                print("Cost of the laptop is Rs 53,000/-")
                print("Your order is successfully placed")
            elif(b1==2):
                print("You chose Lenovo Idea pad from another customer")
                print("Cost of the phone is Rs 46,000/-")
                print("Your order is successfully placed")
        elif(a1==2):
            print("You have chosen a laptop from Dell company")
            print("The models available are:\n1. Dell CT74U26\n2. Dell CT76U26")
            b2=int(input("Enter your choice: "))
            if(b2==1):
                print("You chose Dell CT74U26 from another customer")
                print("Cost of the laptop is Rs 54,000/-")
                print("Your order is successfully placed")
            elif(b2==2):
                print("You chose Dell CT76U26 from another customer")
                print("Cost of the phone is Rs 42,000/-")
                print("Your order is successfully placed")
        elif(a1==3):
            print("You have chose a laptop from HP Comapny")
            print("The models available are:\n1. HP XT72U76\n2. HP MT98TU7")
            b3=int(input("Enter your choice: "))
            if(b3==1):
                print("You chose HP XT72U76 from another customer")
                print("Cost of the laptop is Rs 53,000/-")
                print("Your order is successfully placed")
            elif(b3==2):
                print("You chose HP MT98TU7 from another customer")
                print("Cost of the phone is Rs 46,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
    else:
        print("Sorry we didn't got correct information")
elif(a==2):
    print("Welcome to Customer to Business system")
    print("Here you can sell your products from the categories given below to any company")
    print("1. Sell Mobile\n2. Sell Car")
    c1=int(input("Enter your choice: "))
    if(c1==1):
        print("You chose to sell your phone")
        d3=int(input("Enter your mobile number: "))
        d5=int(input("How much is your phone actual cost: "))
        d4=int(input("How much do you expect from selling your mobile: "))
        d6=d4-d5
        print("So you're expecting"+ " RS " + str(d6) + " profit ")
        print("Your phone has been added to our list")
        print("Thanks for utilising our facilty " + b + " Have a good day")
    elif(c1==2):
        print("You chose to sell your car")
        f3=raw_input("Enter your car model name: ")
        f4=int(input("Actual cost of your car: "))
        f5=int(input("How much do you expect to get amount for it: "))
        f6=f5-f4
        print("So you're expecting"+ " RS " + str(f6) + " profit ")
        print("Your car has been added to our list")
        print("Thanks for utilising our facilty " + b + " Have a good day")
elif(a==3):
    print("Welcome to Business to Customer system")
    print("Here you get various products from different companies")
    print("List of products you can get from companies\n1. Electronic Gadgets\n2. Laptops\n")
    c=int(input("Enter a number from the above: "))
    if(c==1):
        print("Here you can find some branded phones given by some of the companies\n1. Apple\n2. Redmi\n3. Samsung\n4. Google")
        d=int(input("Enter a number according to brand name: "))
        if(d==1):
            print("You have chosen a phone from Apple Company")
            print("The models availble in Apple are:\n1. iPhone 6\n2. iPhone 6s\n3. iPhone 10\n4. iPhone 11")
            e=int(input("Enter a number from 1 to 4 according to your need: "))
            if(e==1):
                print("You chose iPhone 6")
                print("Cost of the phone is Rs 12,000/-")
                print("Your order is successfully placed")
            elif(e==2):
                print("You chose iPhone 6s")
                print("Cost of the phone is Rs 25,000/-")
                print("Your order is successfully placed")
            elif(e==3):
                print("You chose iPhone 10")
                print("Cost of the phone is Rs 45,000/-")
                print("Your order is successfully placed")
            elif(e==4):
                print("You chose iPhone 11")
                print("Cost of the phone is Rs 73,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
        elif(d==2):
            print("You have chosen a phone from Redmi Company")
            print("The models availble in Redmi are:\n1. Redmi 3s 6\n2. Redmi Note5 \n3. Redmi 7A\n4. Redmi 4A")
            f=int(input("Enter your choice: "))
            if(f==1):
                print("You chose Redmi 3s")
                print("Cost of the phone is Rs 9,999/-")
                print("Your order is successfully placed")
            elif(f==2):
                print("You chose Redmi Note5")
                print("Cost of the phone is Rs 17,899/-")
                print("Your order is successfully placed")
            elif(f==3):
                print("You chose Redmi 7A")
                print("Cost of the phone is Rs 7,999/-")
                print("Your order is successfully placed")
            elif(f==4):
                print("You chose Redmi 4A")
                print("Cost of the phone is Rs 8,999/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
        elif(d==3):
            print("You have chosen a phone from Samsung Company")
            print("The models available in Samsung are:\n1. Samsung on5\n2. Samsung on5 pro\n3. Samsung M30")
            g=int(input("Enter your choice"))
            if(g==1):
                print("You chose Samsung on5")
                print("Cost of the phone is Rs 8,000/-")
                print("Your order is successfully placed")
            elif(g==2):
                print("You chose Samsung on5 pro")
                print("Cost of the phone is Rs 10,000/-")
                print("Your order is successfully placed")
            elif(g==3):
                print("You chose Samsung M30 pro")
                print("Cost of the phone is Rs 15,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
        elif(d==4):
            print("You have chosen a phone from Google company")
            print("Models available in Google are:\n1. Google Pixel\n2. Google Pixel 2")
            h=int(input("Enter your choice :"))
            if(h==1):
                print("You chose Google Pixel")
                print("Cost of the phone is Rs 26,000/-")
                print("Your order is successfully placed")
            elif(h==2):
                print("You chose Google Pixel 2")
                print("Cost of the phone is Rs 27,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
    elif(c==2):
        print("Here you find some laptops from various companies used by another customers")
        print("List of various laptop comapnies:\n1. Lenovo\n2. Dell\n3. HP")
        a1=int(input("Enter your choice:"))
        if(a1==1):
            print("You have chosen a laptop from Lenovo company")
            print("The models available are:\n1. Lenovo XT72U76\n2. Lenovo Idea pad")
            b1=int(input("Enter your choice: "))
            if(b1==1):
                print("You chose Lenovo XT72U76")
                print("Cost of the laptop is Rs 53,000/-")
                print("Your order is successfully placed")
            elif(b1==2):
                print("You chose Lenovo Idea pad")
                print("Cost of the phone is Rs 46,000/-")
                print("Your order is successfully placed")
        elif(a1==2):
            print("You have chosen a laptop from Dell company")
            print("The models available are:\n1. Dell CT74U26\n2. Dell CT76U26")
            b1=int(input("Enter your choice: "))
            if(b1==1):
                print("You chose Dell CT74U26")
                print("Cost of the laptop is Rs 54,000/-")
                print("Your order is successfully placed")
            elif(b1==2):
                print("You chose Dell CT76U26")
                print("Cost of the phone is Rs 42,000/-")
                print("Your order is successfully placed")
        elif(a1==3):
            print("You have chose a laptop")
            print("The models available are:\n1. HP XT72U76\n2. HP MT98TU7")
            b1=int(input("Enter your choice: "))
            if(b1==1):
                print("You chose HP XT72U76")
                print("Cost of the laptop is Rs 53,000/-")
                print("Your order is successfully placed")
            elif(b1==2):
                print("You chose HP MT98TU7")
                print("Cost of the phone is Rs 46,000/-")
                print("Your order is successfully placed")
            else:
                print("Sorry you've entered wrong choice")
    else:
        print("Sorry we didn't got correct information")
elif(a==4):
    print("Welcome to Business to Business system")
    print("Here you can sell your products from the categories given below to any company")
    print("1. Sell Mobile\n2. Sell Car")
    c1=int(input("Enter your choice: "))
    if(c1==1):
        print("You chose to sell your phone")
        d3=int(input("Enter your mobile number: "))
        d5=int(input("How much is your phone actual cost: "))
        d4=int(input("How much do you expect from selling your mobile: "))
        d6=d4-d5
        print("So you're expecting"+ " RS " + str(d6) + " profit ")
        print("Your phone has been added to our list")
        print("Thanks for utilising our facilty " + b + " Have a good day")
    elif(c1==2):
        print("You chose to sell your car")
        f3=raw_input("Enter your car model name: ")
        f4=int(input("Actual cost of your car: "))
        f5=int(input("How much do you expect to get amount for it: "))
        f6=f5-f4
        print("So you're expecting"+ " RS " + str(f6) + " profit ")
        print("Your car has been added to our list")
        print("Thanks for utilising our facilty " + b + " Have a good day")