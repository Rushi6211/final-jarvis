
from datetime import datetime
import calendar


def get_today_date():
    today = datetime.now()
    return today.strftime("%d-%m-%Y")


def get_today_day():
    today = datetime.now()
    return today.strftime("%A")


def get_today_month():
    today = datetime.now()
    return today.strftime("%B")


def get_today_year():
    today = datetime.now()
    return today.year


def get_complete_date():
    today = datetime.now()

    return today.strftime(
        "Today is %A, %d %B %Y."
    )


def get_calendar():
    today = datetime.now()

    return calendar.month(
        today.year,
        today.month
    )


def handle_date_command(command):

    command = command.lower().strip()

    if "calendar" in command:
        return get_calendar()

    elif "year" in command:
        return f"The current year is {get_today_year()}"

    elif "month" in command:
        return f"The current month is {get_today_month()}"

    elif "day" in command:
        return f"Today is {get_today_day()}"

    elif "date" in command:
        return get_complete_date()

    else:
        return "Sorry, I don't understand this command."


# Test date feature
if __name__ == "__main__":

    print("JARVIS DATE FEATURE")

    while True:

        command = input("\nYou: ")

        if command.lower() == "exit":
            print("Jarvis: Goodbye Sir!")
            break

        response = handle_date_command(command)

        print("Jarvis:", response)
