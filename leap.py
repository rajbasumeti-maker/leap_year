def leapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"

if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
        print(leapYear(year))
    except EOFError:
        pass