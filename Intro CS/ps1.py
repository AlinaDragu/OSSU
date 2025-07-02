#### Part A: Saving for a House
# You have just graduated from MIT and have a job! You move to the Bay Area and decide that you want to start saving for a home. Houses are fairly
# expensive, so you start saving up for the down payment on your dream home.
# Your goal is to find the number of months it takes to save up for a down payment. The cost of your down payment is calculated by multiplying the
# total cost of your dream house by the down payment percentage.

# User Inputs. Ask the user to enter the following variables and cast them as floats. They must be initialized in the following order at the beginning of
# your program, before declaring other variables.
# 1. The starting yearly salary ( yearly_salary)
# 2. The portion of salary to be saved ( portion_saved). This variable should be in decimal form (e.g. 0.1 for 10%).
# 3. The cost of your dream home ( cost_of_dream_home)

# Writing the Program. You will need to determine how many months it will take given the following information:
# 1. yearly_salary, as described above.
# 2. portion_saved, as described above.
# 3. cost_of_dream_home, as described above.
# 4. portion_down_payment, the percentage of the total cost needed for a down payment. Assume portion_down_payment = 0.25 (25%).
# 5. The amount that you have saved thus far is amount_saved, which starts at $0.
# 6. You get an annual rate of return r. In other words, at the end of each month, you receive an additional amount_saved * (r/12) funds for your
# savings (the 12 is because r is an annual rate). Assume r = 0.05 (5%).
# 7. At the end of each month, your savings increase by (1) a percentage of your monthly salary and (2) the monthly return on your investment. (Note:
# The investment amount used to calculate the monthly return is the amount you had saved at the start of each month.)

# Output.
# 1. Your program should store the number of months required to save for the down payment using a variable called months.

yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
r = 0.05
amount_saved = 0.0
monthly_salary = yearly_salary / 12
down_payment = cost_of_dream_home * portion_down_payment

months = 0
for month in range(1, 1000):
    amount_saved += amount_saved * (r / 12) + (monthly_salary * portion_saved)
    if amount_saved >= down_payment:
        months = month
        break

print(f"Number of months: {months}")





#### Part B: Saving with a raise
# In Part A, we assumed that your salary did not change over time. However, you are an MIT graduate, and clearly you are going to be worth more to your
# company over time! In this part, we will build on your solution to Part A by adding a salary raise every six months. Copy over your solution from Part A
# into the corresponding sections in ps1b.py.

# User Inputs. There is one additional user input in Part B. Remember to cast these inputs as floats and in the following order before declaring other
# variables.
# 1. The starting yearly salary ( yearly_salary)
# 2. The portion of salary to be saved ( portion_saved)
# 3. The cost of your dream home ( cost_of_dream_home)
# 4. The semi-annual salary raise ( semi_annual_raise), which is a decimal percentage (e.g. 0.1 for 10%)

# Writing the Program. Write a program to calculate how many months it will take for you to save up for a down payment. You can reuse much of the
# code from Part A. Like before, assume that your investments earn an annual rate of return r = 0.05 (or 5%) and that portion_down_payment =
# 0.25 (or 25%). In this version, yearly_salary increases by semi_annual_raise at the end of every six months.

# Output.
# 1. Like Part A, your program should store the number of months required to save up for your down payment using a variable called months.

yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
r = 0.05
amount_saved = 0.0
monthly_salary = yearly_salary / 12
down_payment = cost_of_dream_home * portion_down_payment

months = 0
for month in range(1, 1000):
    if month % 6 == 1 and month != 1:  # Apply raise every 6 months
        yearly_salary += yearly_salary * semi_annual_raise
        monthly_salary = yearly_salary / 12
    amount_saved += amount_saved * (r / 12) + (monthly_salary * portion_saved)
    if amount_saved >= down_payment:
        months = month
        break

print(f"Number of months: {months}")



#  Part C: Choosing an Interest Rate
# In Part A and B, you explored how (1) the percentage of your salary saved each month and (2) a semi-annual raise affects how long it takes to save for a
# down payment given a fixed rate of return, r.
# In Part C, we will have a fixed initial amount and the ability to choose a value for the rate of return, r. Given an initial deposit amount, our goal is to find
# the lowest rate of return that enables us to save enough money for the down payment in 3 years.

# User Inputs. Cast the user input as a float in the beginning of your program.
# 1. The initial amount in your savings account ( initial_deposit)

# Writing the Program. Write a program to calculate the minimum rate of return r needed in order to reach your goal of a sufficient down payment in 3
# years, given an initial_deposit. To simplify things, assume:
# 1. The cost of the house that you are saving for is $800,000.
# 2. The down payment is 25% of the cost of the house.

# Use the following formula for compound interest in order to calculate the predicted savings amount given a rate of return r, an initial_deposit, and
# months: 
# amount_saved = initial_deposit × (1 + r/12 ) months
# You will use bisection search to determine the lowest rate of return r that is needed to achieve a down payment on a $800,000 house in 36 months.
# Since hitting this exact amount is a bit of a challenge, we only require that your savings be within $100 of the required down payment. For example, if
# the down payment is $1000, the total amount saved should be between $900 and $1100 (exclusive).
# Your bisection search should update the value of r until it represents the lowest rate of return that allows you to save enough for the down payment in 3
# years. r should be a float (e.g. 0.0704 for 7.04%). Assume that r lies somewhere between 0% and 100% (inclusive).

initial_deposit = float(input("Enter your initial deposit: "))

total_cost = 800000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
months = 36
epsilon = 100
low = 0.0
high = 1.0
steps = 0
found = False

for _ in range(100):  # max 100 steps to find the best r
    r = (low + high) / 2
    amount_saved = initial_deposit * ((1 + r / 12) ** months)
    steps += 1

    if abs(amount_saved - down_payment) < epsilon:
        found = True
        break
    elif amount_saved < down_payment:
        low = r
    else:
        high = r

if found:
    print(f"Best savings rate: {r:.5f}")
    print(f"Steps in bisection search: {steps}")
else:
    print("It is not possible to pay the down payment in 3 years.")