from lib2to3.pgen2.literals import simple_escapes
import math
# Create a program that allows the user to access two different financial calculators:
# A investment calculator & A Home loan repayment calculator : 
# Create a varibale to store & determine which calculator the user wants to run.
menu = input(f"""Choose either 'investment' or 'bond' from the menu below to proceed: 
investment - to calculate the amount of intrest you'll earn on intrest. 
bond       - to calculate the amount you'll have to pay on a home loan. 
Enter here: """)

# Use .lower() function to manipulate how user capitalises their selection.
# If the user doesn’t type in a valid input, show an appropriate error message.
# Create an if statement to validate all the conditions for 'investment'.
if menu.lower() == "investment" : 
    inv_price = int(input("Please enter a deposit amount: "))
    inv_rate = int(input("Please enter intrest rate as a percenatge without the symbol (%) : "))
    inv_time = int(input("Please enter the number of years you plan to invest: "))
    intrest = input("""Please select either :
 * simple - Anually, calculated on the initial deposit invested.
 * compound - Continually, calculated on the initial deposit invested. 
 Enter here: """)

# Depending on whether the user inputed “simple” or “compound”, calculate and output the interest rate. 
# Look below for “Interest formulae” : 
# Simple interest is calculated as follows: A =P*(1+r*t)
# Compound intrest is calculated as follows: A = P* math.pow((1+r),t)
# Create an if condition to validate simple intrest caluclations.
# Convert the rate inputed by user to a percentage by dividing it by 100.
    if intrest.lower() == "simple" :
        simple_intrest = round(inv_price * ( 1 + (inv_rate/100) * inv_time), 2)
        print(simple_intrest)

# Create a elif condition to validate compound intrest calculations.
    elif intrest.lower() == "compound" :
        compound_intrest = round((inv_price * math.pow((1 + (inv_rate/100)) ,inv_time)), 2)
        print(compound_intrest)

# Create a defualt incase the user makes a mistake.
    else :
        print("invalid entry , please read question carefully") 

# Create an if statement to validate all the conditions for 'bond'.
# The monthly interest rate, is calculated by dividing the annual interest rate by 12.
# Home loan repayment month to month calculation : (i.P)/(1 - (1+i)^(-n)) 
elif menu.lower() == "bond" :
    bon_price = float(input("Please enter the present value of house: "))
    bon_rate = int(input("Please enter the intrest rate as a percenatge without the symbol (%) : ")) / 100 / 12
    bon_time = int(input("Please enter the number of months you plan to repay the bond: "))
    bon_repayment = round(((bon_rate)* bon_price / (1 - (1 + (bon_rate)) ** (-bon_time))), 2)
    print(bon_repayment)

# Create a defualt incase the user makes a mistake.
else :
    print("invalid entry , please read question carefully") 
