
from datetime import datetime


def get_current_time():
    """Get current time."""

    current_time = datetime.now()

    return current_time.strftime("%I:%M %p")


def get_current_date():
    """Get today's date."""

    current_date = datetime.now()

    return current_date.strftime("%d %B %Y")


def get_current_day():
    """Get current day."""

    current_day = datetime.now()

    return current_day.strftime("%A")


def get_time_details():
    """Get complete date and time."""

    now = datetime.now()

    details = f"""
    Sir, here are the current details:

    Time       : {now.strftime("%I:%M:%S %p")}
    Date       : {now.strftime("%d-%m-%Y")}
    Day        : {now.strftime("%A")}
    Month      : {now.strftime("%B")}
    Year       : {now.strftime("%Y")}
    """

    return details


def handle_time_command(command):

    command = command.lower()

    if "time" in command:
        return f"Sir, the current time is {get_current_time()}"

    elif "date" in command:
        return f"Today's date is {get_current_date()}"

    elif "day" in command:
        return f"Today is {get_current_day()}"

    elif "details" in command:
        return get_time_details()

    else:
        return "Sorry, I don't understand the time command."


# Testing the feature
if __name__ == "__main__":

    print("JARVIS TIME FEATURE")

    while True:

        command = input("\nYou: ")

        if command.lower() == "exit":
            print("Jarvis: Goodbye Sir!")
            break

        response = handle_time_command(command)

        print("Jarvis:", response)
