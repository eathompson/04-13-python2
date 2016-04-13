import math

# Prompt the user for an Initial Balance (and save to a variable)
init_balance = input("Initial balance:")

# use the float() function to convert the input into a number.
float(init_balance)


# Prompt the user for an Annual Interest % (and save to a variable)
annual_interest = float(input("Annual interest %:"))

# use the float() function to convert the input into a number
#float(annual_interest)

# change the percentage number into a decimal (e.g. 6 turns into .06, 5 turns into .05, etc).
# remember to save your new value to a variable!
annual_interest = annual_interest/100

# Prompt the user for a Number of years (and save to a variable)
no_years = int(input("Number of years:"))
# use the int() function to convert the input into an integer


# Calculate the total value following the formula.
# You can use multiple steps and variables if necessary.
# Note that n = 12
total_earnings_and_value = init_balance*(1+(annual_interest/12)**(12*no_years))

# Calculate the interest earned based on the above value and the initial balance
interest_earned = total_earnings_and_value - init_balance

# Output the interest earned
print ("Interest earned in "+str(no_years)+" years: $"+str(interest_earned))


# Output the total value
#print str(total_earnings_and_value)
