# Matt Curl
# HW 03
# Lab Section 13
# 11/5/2024
# Sources/Help: Googled "How to check for a leap year" and got https://learn.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year 
 
# set up a dictionary with the months and days that correspond to each month in a normal year
month_and_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# set up a list that is days of the week with sunday at 0 index
days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# set up a leap year checker function
def check_leap(year):
    # follow leap year laws from source
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# get what day janurary first is on using equations given
def day_jan_1(year):
    y = year - 1
    day_of = (36 + y + (y//4) - (y//100) + (y//400)) % 7
    return day_of
# check that the date is valid in every way
def check_validity(month,day,year):
    # check months and date is valid
    if month > 12 or month < 1 or day < 1:
        return False
    # check if its a leap year and append the dictionary accordingly
    if check_leap(year) == True:
     month_and_days[2] = 29
    else:
       month_and_days[2] = 28
    # check if the days are greater than the dictionary values
    if day <= month_and_days[month]:
        return True
    else:
        return False
# calculate the day of the week
def calculate_day(month,day,year):
    # use jan 1st of that year to start
    J_1_day = day_jan_1(year)
    # add the days using the sum of the range function on the dictionary keys + the days since 1st of month minus 1(since we want day of)
    days_since = sum(month_and_days[m] for m in range(1,month)) + (day - 1)
    # add the days since jan 1st and get remainder from 7 for day of week
    day_of = (J_1_day + days_since) % 7
    # get the day name from list
    day_name = days_of_week[day_of]
    return day_name
# make a while loop for user input
while True:
    user_day = input("Please put in a date in the format MM/DD/YYYY to get what day of the week it is: (say exit to exit)")
    if user_day.lower() == 'exit':
        break
    else:
        # split the input and make new variables from the list from splitting
        nums_str = user_day.split("/")
        u_month = int(nums_str[0])
        u_day = int(nums_str[1])
        u_year = int(nums_str[2])
        # check the validity of the date then calculate and print accordingly
        if check_validity(u_month, u_day, u_year) == True:
         day_n = calculate_day(u_month, u_day, u_year)
         print(f"{user_day} {day_n}")
        else :
         print(f"{user_day} Invalid Date")