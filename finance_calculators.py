import math
def simple_Investment():
    ###SIMPLE_INVESTMENT###
    # User enters amount, percent and year.
    #ONLY USE INVESTMENT and add INTEREST on per year.
    #Take investment and divding by interest, multiply by year, and adding to investment
    present_Value = float(input("Please enter initial investment: R"))
    interest_Percent = float(input("Please enter the interest (Please do not enter the '%' symbol) :"))
    number_Years = float(input("Please enter the amount of years: "))
    total = present_Value + ((present_Value / interest_Percent) * number_Years)
    total = str(round(total, 2))
    print(f"Your total after {number_Years} years(s) will be R{total}")

def compound_Investment():
     ###COMPOUND_INVESTMENT###
    # User enters amount, percent and year.
    #ADD TOTAL FROM PREVIOUS YEAR
    #Take investment and divding by interest, multiply by year, then make a new total
    #total=principle_amount * math.pow((1 + interest), year)
    present_Value = float(input("Please enter initial investment: R"))
    interest_Percent = float(input("Please enter the interest (Please do not enter the '%' symbol) :"))
    number_Years= float(input("Please enter the amount of years: "))
    total = present_Value * math.pow((1 + (interest_Percent / 100)), number_Years)
    total = str(round(total, 2))
    print(f"Your total after {number_Years} year(s) will be R{total}")

def bond ():
    ########BOND FUNCTION##########
    #User enters house value
    #User enters interest rate
    #user enters total months
    #Print out monthly repayments.
    present_Value = float(input("Please enter the present value of your property: R"))
    interest_Percent = float(input("Please enter the interest rate (Don not enter the '%' symbol) : "))
    payment_Months = float(input("Please enter the amount of months to repay the bond: "))
    interest_Rate = float(interest_Percent / 12)
    repayment = present_Value * (interest_Rate * ((1 + (interest_Rate)) ** payment_Months)) / (((1 + interest_Rate) ** payment_Months) - 1)
    repayment = str(round(repayment, 2))
    print(f"You will have to pay {repayment} over {payment_Months} months")

###############TASK1###############
#User selects investment type. investment or bond
#must include upper and lower functions to prevent errors(.lower)
#Must show error messages
print("Investment    =     to calculate the amount of interest you'll earn on interest")
print("Bond          =     to calculate the amount you'll have to pay on a home loan")
option = input("Please enter if you would like to make an investment or pay off a bond: ").lower()
if option == "investment":
    conversion_choice = input("Would you like to apply for simple or compound investment: ").lower()
    if conversion_choice == "simple":
        simple_Investment()
    elif conversion_choice == "compound":
        compound_Investment()
    else:
        print("Invalid option.")
elif option == "bond":
    bond()
else:
    print("That is not an option.")