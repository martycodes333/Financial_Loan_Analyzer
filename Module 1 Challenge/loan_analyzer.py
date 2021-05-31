# Module 1 Challenge by Martique Henton


# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
total_number_of_loans = len(loan_costs) # used the len function to calculate the total number of loans in the list 'loan_costs'
print(f"The total number of loans is: {total_number_of_loans}") # print the number of loans to verify code is working


# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
total_loan_value = sum(loan_costs) # created a variable called 'total_loan_value' to save the result from the sum of 'loan_costs'
print(f"The total value of the loans is: ${total_loan_value}") # print the total value to verify code is working

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

avg_loan = sum(loan_costs) / len(loan_costs) # created a new variable called 'avg_loan' to hold the value of the average loan amount
    
print(f"The average loan amount is: ${avg_loan}") # print the average loan amount ot verfiy code is working
    


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

fv = loan.get("future_value") # created the variables 'fv', 'rm', and 'cost_of_loan' to hold the extracted data from the loan dict
rm = loan.get("remaining_months") 
cost_of_loan = loan.get("loan_price")

print(f"The Future Value is: {fv}") # printed variables to verify code is working
print(f"The Remaining Months are: {rm}")
# print(cost_of_loan) # created a variable, and printed 'cost of loan' to use in conditional statement below to ensure the conditional is working properly


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

fair_value = fv / (1+ 0.20/12) ** rm  # used the present value formula to calculate the 'fair_value', which is 861.77
# print(f"The fair value for the loan is: ${fair_value: .2f}") # printed to verify my code is working

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

if fair_value >= cost_of_loan: # cost_of_loan extracted from the 'loan' dict
    print("This loan is worth at least the cost to buy it.") # if the present value or 'fair_value' is greater than or equal to the cost print this
else:
    print("The loan is too expensive and not worth the price.") # else print this



"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

# test_value = 1000 / (1+ 0.20/12) ** 12
# print(f"the test value is: {test_value}") 

def calculate_present_value(future_value, remaining_months, annual_discount_rate): # parameters used to define function
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months # calculation for present value of the loan
    # print(f"PV, {present_value: .2f}")
    return present_value # return present value for the loan


    

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = 0.20
new_loan_calculation = calculate_present_value( # new loan calculation using the 'calculate_present_value' function
    new_loan["future_value"], 
    new_loan["remaining_months"],
    annual_discount_rate
)
 # print(f"The present value of the new loan is: ${new_loan_calculation: .2f}"), used a print statement to verify the function is working 


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list



for item in loans:
   # print(item)
    # loan_price = item.get("loan_price"), tested alternative action to extract data from 'loans'
    if item["loan_price"] < 500: # if the loan price with the 'loans' dict is less than 500, append to 'inexpensive_loans'
        inexpensive_loans.append(item) # append the inexpensive loan(s) to the 'inexpensive_loans' list
        # print("loan_price: ", loan_price), a print statement to verify the correct loan was extracted from the 'loans' dict
    
              

# @TODO: Print the `inexpensive_loans` list
        print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# print("writing the data to a csv file..."), a print statement to verify path is working 

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w') as csvfile: #use 'with open' to open a new CSV file
    csvwriter = csv.writer(csvfile) # create a csvwriter using the csv library
    csvwriter.writerow(header) # use the csvwriter to write the 'header' variable as the first row
    for loan in inexpensive_loans: # use a for loop to iterate through each loan in 'inexpensive loans
        csvwriter.writerow(loan.values()) # use the csvwriter to write the loan.values() to a row in the CSV file 

# print(loan.values()) # a print statement to verify code is working
       


