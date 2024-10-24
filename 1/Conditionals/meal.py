def main():
    time = input("What is the time (in 24h format ##:##): ")
    converted_time = convert(time)
    check_meal_time(converted_time)

def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60

def check_meal_time(time):
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
