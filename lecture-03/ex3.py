hours_worked = int(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the horly pay rate: "))

if hours_worked <= 40 :
    print("The gross pay is ${:.2f}".format(hours_worked * pay_rate))
else:
    cal_pay = hours_worked - 40
    print("The gross pay is ${:.2f}".format(((hours_worked - cal_pay) * pay_rate) + (cal_pay * (pay_rate * 1.5))))