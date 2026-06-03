from datetime import date as dt


def calculate_age():
    """Takes a given date of birth and calculates the current age compared to the current date
    INPUT: Date of birth (Year, month, date)
    OUTPUT: Age"""
    given_year = input("Please provide a year: ")
    given_month = input("Please provide a month: ")
    given_day = input("Please provide a day of the month: ")

    today = dt.today()

    age = int(today.year) - int(given_year)

    if (int(today.month), int(today.day)) < (int(given_month), int(given_day)):
        age -= 1

    print(f' You are {age} years old!')


calculate_age()
