# -------------------------------------------------------------------
# --- New Code ! using try...except


import sys


def get_user_input(prompt: str):
    """Helper function to get a float input with error handling."""
    try:
        return float(input(prompt))
    except ValueError:
        print("Bad value, please enter a number")
        sys.exit()


def calculate_pay(hours: float, rate: float):
    """Calculate gross pay including overtime if applicable."""
    if hours <= 40:
        return hours * rate

    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.5
    return regular_pay + overtime_pay


def main():
    """Main function used to invoke sub-functions and compute the global result."""
    # User Inputs
    hours_worked = get_user_input("Enter Hours: ")
    rate_per_hour = get_user_input("Enter Your Rate Per Hour: ")

    # Calculation
    total_pay = calculate_pay(hours_worked, rate_per_hour)

    # Output
    if hours_worked <= 40:
        print(f"Regular pay: {total_pay:.2f}")
    else:
        print(f"Overtime pay: {total_pay:.2f}")


main()
