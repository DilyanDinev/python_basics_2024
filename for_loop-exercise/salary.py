number_of_browsers = int(input())
salary = int(input())

for browser in range(number_of_browsers):
    name_browser = input()

    if name_browser == "Facebook":
        salary -= 150
    elif name_browser == "Instagram":
        salary -= 100
    elif name_browser == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")