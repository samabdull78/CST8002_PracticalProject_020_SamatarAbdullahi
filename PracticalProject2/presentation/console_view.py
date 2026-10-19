# Author: Samatar Abdullahi
# Course: CST8002 Programming Language Research Project
# Professor: Stanley Pieda
# Due date: Oct 18, 2026
#[5] R. Python, “Defining Main Functions in Python – Real Python,” realpython.com. 
#   https://realpython.com/python-main-function/ 
#       (accessed Oct. 18, 2026).
import csv

from model.record import LakeRecord


STUDENT_NAME = "Samatar Abdullahi"


class ConsoleView:
    """Provide a console interface for the lake record application."""

    def __init__(self, service):
        """Receive the business service used by the interface."""
        self.service = service

    def show_name(self):
        """Display the student's name."""
        print(f"\nProgram by {STUDENT_NAME}")

    def read_integer(self, prompt):
        """ Ask until the user enters an integer."""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a whole number.")

    def read_percentage(self):
        """ Ask until a valid percentage is entered."""
        while True:
            try:
                value = float(input("Percent abundance (0-100): "))

                if 0 <= value <= 100:
                    return value

                print("Enter a number between 0 and 100.")
            except ValueError:
                print("Please enter a number.")

    def read_text(self, prompt):
        """ Ask until nonempty text is entered."""
        while True:
            value = input(prompt).strip()

            if value:
                return value

            print("This field cannot be empty.")

    def read_record(self, identification):
        """Get all other fields for a new or replacement record."""
        return LakeRecord(
            identification=identification,
            lake_identification=self.read_text(
                "Lake identification: "
            ),
            year=self.read_integer("Year: "),
            species_code=self.read_text("Species code: "),
            species=self.read_text("Species: "),
            percent_abundance=self.read_percentage(),
        )

    def display_records(self, records):
        """Display records and repeat the name every ten records."""
        if not records:
            print("There are no records to display.")
            return

        self.show_name()

        for number, record in enumerate(records, start=1):
            print(record.display())

            if number % 10 == 0:
                self.show_name()

        print(f"\nDisplayed {len(records)} record(s).")

    def show_menu(self):
        """Display available actions and the current record count."""
        self.show_name()
        print(f"Records in memory: {len(self.service.get_all())}")
        print("1. Reload original dataset")
        print("2. Save current records to a new CSV")
        print("3. Display one record")
        print("4. Display multiple records")
        print("5. Add a record")
        print("6. Edit a record")
        print("7. Delete a record")
        print("0. Exit")

    def add_record(self):
        """Collect and add a new record."""
        identification = self.read_integer("New identification: ")
        record = self.read_record(identification)
        self.service.add(record)

        print("Record added successfully.")
        print(record.display())

    def edit_record(self):
        """Collect replacement values for an existing record."""
        identification = self.read_integer(
            "Identification to edit: "
        )
        original = self.service.get_one(identification)

        print("Current record:")
        print(original.display())
        print("Enter all replacement values.")

        replacement = self.read_record(identification)
        self.service.update(identification, replacement)

        print("Record updated successfully.")
        print(replacement.display())

    def delete_record(self):
        """Remove a selected record after confirmation."""
        identification = self.read_integer(
            "Identification to delete: "
        )
        record = self.service.get_one(identification)
        print(record.display())

        confirmation = input("Delete this record? (y/n): ").strip().lower()

        if confirmation == "y":
            self.service.delete(identification)
            print(f"Record {identification} deleted.")
        else:
            print("Deletion cancelled.")

    def handle_choice(self, choice):
        """Perform the selected menu operation."""
        if choice == "1":
            count = self.service.reload()
            print(f"Reloaded {count} records from the original dataset.")

        elif choice == "2":
            path = self.service.save()
            print(f"Saved {len(self.service.get_all())} records.")
            print(f"Output file: {path}")

        elif choice == "3":
            identification = self.read_integer("Identification: ")
            record = self.service.get_one(identification)
            self.display_records([record])
        elif choice == "4":
            self.display_records(self.service.get_all())
        elif choice == "5":
            self.add_record()

        elif choice == "6":
            self.edit_record()

        elif choice == "7":
            self.delete_record()

        else:
            print("Please choose an option from 0 to 7.")

    def run(self):
        """Load initial data and run the interactive menu."""
        self.show_name()

        try:
            count = self.service.reload()
            print(f"Loaded {count} records.")
        except (OSError, ValueError, UnicodeError, csv.Error) as error:
            print(f"Could not load the dataset: {error}")
            print("You can correct the file and select Reload.")

        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "0":
                self.show_name()
                print("Goodbye.")
                return

            try:
                self.handle_choice(choice)
            except (OSError, ValueError, UnicodeError, csv.Error) as error:
                print(f"Operation failed: {error}")
            self.show_name()
            input("\nPress Enter to return to the menu...")