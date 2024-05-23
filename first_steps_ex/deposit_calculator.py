deposit = float(input())
months = int(input())
annual_percent = float(input())

monthly_interest = annual_percent / 12
monthly_sum = monthly_interest * deposit / 100
total_sum = deposit + months * monthly_sum
print(total_sum)


