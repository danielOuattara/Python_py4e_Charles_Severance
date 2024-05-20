
"""
# Previous Code

hours_worked = float(input("Enter Hours:"))
rate_per_hour = float(input("Enter Your Rate Per Hour:"))
gross_pay = hours_worked * rate_per_hour
print("Pay:", gross_pay)
"""

# --- New Code !

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
