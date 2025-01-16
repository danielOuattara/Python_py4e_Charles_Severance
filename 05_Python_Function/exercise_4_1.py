import sys


def compute_pay_1(hours: int, rate: float):
    """
    This function take 2 parameters and return the pay amount.
    Caution: This function does not handle error in inputs

    :param `hours`: int
    :param `rate`: rate pay for an hour of work.
                 if the total number of worked hours exceed 40hrs,
                 then the rate is increased by 50%
    :return: the pay amount according to hours and rate
    """

    hours_worked = float(hours)
    rate_per_hour = float(rate)

    gross_pay = hours_worked * rate_per_hour

    if hours_worked > 40:
        over_time = hours_worked - 40
        over_time_pay = over_time * rate_per_hour * 0.5
        gross_pay += over_time_pay
    return gross_pay


pay_1 = compute_pay_1(40, 10)
print("pay_1 = ", pay_1)

pay_2 = compute_pay_1(41, 10)
print("pay_2 = ", pay_2)


# -------------------------------------------------------------------

def compute_pay_2(hours: int, rate: float):
    """
    This function take 2 parameters and return the pay amount.
    This function does not handle error in inputs

    :param hours: int
    :param rate: rate pay for an hour of work.
                 if the total number of worked hours exceed 40hrs,
                 then the rate is increased by 50%
    :return: the pay amount according to hours and rate
    """
    try:
        hours_worked = float(hours)
        rate_per_hour = float(rate)
    except:
        print("Error in pay_input_2 : \nPlease, provide numeric for inputs value")
        exit()

    gross_pay = hours_worked * rate_per_hour

    if hours_worked > 40:
        over_time = hours_worked - 40
        over_time_pay = over_time * rate_per_hour * 0.5
        gross_pay += over_time_pay
    return gross_pay


pay_1 = compute_pay_2("hello", 10)
print("pay_1 = ", pay_1)

pay_2 = compute_pay_2(41, 10)
print("pay_2 = ", pay_2)
