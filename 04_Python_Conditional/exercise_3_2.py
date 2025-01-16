"""
# Previous Code

hours_worked = float(input("Enter Hours:"))
rate_per_hour = float(input("Enter Your Rate Per Hour:"))

gross_pay = hours_worked * rate_per_hour

if hours_worked <= 40:
    print("Regular pay :", gross_pay)
else:
    over_time = hours_worked - 40
    over_time_pay = over_time * rate_per_hour * 0.5
    overtime_gross_pay = gross_pay + over_time_pay
    print("Overtime pay :", overtime_gross_pay)

gross_pay = hours_worked * rate_per_hour

"""

# -----------------------------------------------------

# --- New Code ! using try...except

# try:
#     hours_worked = float(input("Enter Hours:"))
# except:
#     print("Bad value, please enter a number")
#     exit()
# try:
#     rate_per_hour = float(input("Enter Your Rate Per Hour:"))
# except:
#     print("Bad value, please enter a number")
#     exit()

# gross_pay = hours_worked * rate_per_hour

# if hours_worked <= 40:
#     print("Regular pay :", gross_pay)
# else:
#     over_time = hours_worked - 40
#     over_time_pay = over_time * rate_per_hour * 0.5
#     overtime_gross_pay = gross_pay + over_time_pay
#     print("Overtime pay :", overtime_gross_pay)

# gross_pay = hours_worked * rate_per_hour

# -----------------------------------------------------

# --- New Code ! using try...except

import sys


def get_user_input(prompt):
    """Helper function to get a float input with error handling."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Bad value, please enter a number")
        sys.exit()


def calculate_pay(hours, rate):
    """Calculate gross pay including overtime if applicable."""
    if hours <= 40:
        return hours * rate

    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.5
    return regular_pay + overtime_pay


# Input
hours_worked = get_user_input("Enter Hours: ")
rate_per_hour = get_user_input("Enter Your Rate Per Hour: ")

# Calculation
total_pay = calculate_pay(hours_worked, rate_per_hour)

# Output
if hours_worked <= 40:
    print(f"Regular pay: {total_pay:.2f}")
else:
    print(f"Overtime pay: {total_pay:.2f}")
