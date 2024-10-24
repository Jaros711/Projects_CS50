def main():
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    while True:
        date_input = input("Enter a date (MM/DD/YYYY or Month Day, Year): ").strip()

        # Check MM/DD/YYYY format
        if '/' in date_input:
            try:
                month, day, year = map(int, date_input.split('/'))
                if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
                    print(f"{year}-{month:02}-{day:02}")
                    return
            except ValueError:
                pass  # If conversion fails, continue to prompt

        # Check Month Day, Year format
        else:
            parts = date_input.replace(',', '').split()  # Remove comma and split
            if len(parts) == 3:
                month_str, day_str, year_str = parts
                if ',' in date_input:  # Ensure there's a comma in the original input
                    try:
                        day = int(day_str)
                        year = int(year_str)
                        if month_str in months and 1 <= day <= 31 and year > 0:
                            month = months[month_str]
                            print(f"{year}-{month}-{day:02}")
                            return
                    except ValueError:
                        pass  # If conversion fails, continue to prompt

        print("Invalid date format. Please try again.")


if __name__ == "__main__":
    main()
