
import os
from datetime import datetime

NOTES_FILE = "jarvis_notes.txt"


def add_note(note):
    """Save a new note."""

    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(NOTES_FILE, "a") as file:
        file.write(f"{date_time} | {note}\n")

    return "Your note has been saved successfully."


def read_notes():
    """Read all saved notes."""

    if not os.path.exists(NOTES_FILE):
        return "You don't have any saved notes."

    with open(NOTES_FILE, "r") as file:
        notes = file.read()

    if not notes.strip():
        return "Your notes list is empty."

    return notes


def search_note(keyword):
    """Search notes using a keyword."""

    if not os.path.exists(NOTES_FILE):
        return "No notes available."

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()

    results = [
        note.strip()
        for note in notes
        if keyword.lower() in note.lower()
    ]

    if results:
        return "\n".join(results)

    return "Sorry, I couldn't find that note."


def handle_note_command(command):
    """Process Jarvis voice commands."""

    command = command.lower().strip()

    if command.startswith("save note"):
        note = command.replace("save note", "", 1).strip()

        if note:
            return add_note(note)

        return "Please tell me what note to save."

    elif command in ["read notes", "show notes"]:
        return read_notes()

    elif command.startswith("search note"):
        keyword = command.replace("search note", "", 1).strip()

        if keyword:
            return search_note(keyword)

        return "Please tell me what to search."

    return "Unknown notes command."


# Test the feature
if __name__ == "__main__":

    print("JARVIS NOTES MANAGER")

    while True:
        command = input("\nYou: ")

        if command.lower() == "exit":
            print("Jarvis: Goodbye!")
            break

        response = handle_note_command(command)

        print("Jarvis:", response)
