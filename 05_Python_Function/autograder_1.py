<<<<<<< HEAD
=======
'''
>>>>>>> b3f7c80 (Committing local changes before pulling from remote)
def compute_pay(hours, rate):
    hours = float(input('Enter yours worked hours : '))
    rate = float(input('Enter yours rate pay : '))
    hours_rate = 40

    if hours > hours_rate:
        basic_pay = hours_rate * rate
        regulated_rate = rate * 1.5
        pay_amount = basic_pay + (hours - hours_rate) * regulated_rate
    else:
        pay_amount = hours * rate

    return pay_amount


p = compute_pay(10, 20)
print("Pay", p)
<<<<<<< HEAD
=======

'''


def compute_pay():
    hours = float(input('Enter yours worked hours : '))
    rate = float(input('Enter yours rate pay : '))
    hours_rate = 40

    if hours > hours_rate:
        basic_pay = hours_rate * rate
        regulated_rate = rate * 1.5
        pay_amount = basic_pay + (hours - hours_rate) * regulated_rate
    else:
        pay_amount = hours * rate

    return pay_amount


p = compute_pay()
print("Pay", p)
>>>>>>> b3f7c80 (Committing local changes before pulling from remote)
