"""
QueueSmart Studio
-----------------
Main interface for the QueueSmart system.
"""

from queue_smart import QueueSmart


class QueueSmartStudio:

    def __init__(self):

        self.queue_system = QueueSmart()

    # ----------------------------------
    # Add Person to Queue
    # ----------------------------------
    def add_person(self):

        print(
            "\n========== ADD PERSON ==========\n"
        )

        person_id = input(
            "Person ID: "
        ).strip()

        name = input(
            "Name: "
        ).strip()

        while True:

            try:

                service_duration = int(
                    input(
                        "Expected Service Duration (minutes): "
                    )
                )

                if service_duration <= 0:

                    print(
                        "Service duration must be greater than 0."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # Validate urgency
        valid_urgency = [

            "low",
            "medium",
            "high",
            "critical"

        ]

        while True:

            urgency = input(
                "Urgency (Low/Medium/High/Critical): "
            ).strip().lower()

            if urgency in valid_urgency:

                break

            print(
                "Invalid urgency level."
            )

        # Appointment
        appointment_input = input(
            "Has Appointment? (yes/no): "
        ).strip().lower()

        has_appointment = (

            appointment_input == "yes"

            or

            appointment_input == "y"

        )

        person = self.queue_system.add_person(

            person_id,

            name,

            service_duration,

            urgency,

            has_appointment

        )

        print(
            "\nPerson added successfully."
        )

        print(
            f"Priority Score: "
            f"{person['Priority Score']}"
        )

    # ----------------------------------
    # View Queue
    # ----------------------------------
    def view_queue(self):

        self.queue_system.display_queue()

    # ----------------------------------
    # View Next Person
    # ----------------------------------
    def view_next_person(self):

        person = self.queue_system.next_person()

        if not person:

            print(
                "\nQueue is currently empty."
            )

            return

        print(
            "\n========== NEXT PERSON ==========\n"
        )

        print(
            f"Name           : "
            f"{person['Name']}"
        )

        print(
            f"Person ID      : "
            f"{person['ID']}"
        )

        print(
            f"Urgency        : "
            f"{person['Urgency'].title()}"
        )

        print(
            f"Priority Score : "
            f"{person['Priority Score']}"
        )

        print(
            f"Estimated Wait : "
            f"{person['Estimated Wait']} minutes"
        )

    # ----------------------------------
    # Serve Next Person
    # ----------------------------------
    def serve_next_person(self):

        person = self.queue_system.serve_next()

        if not person:

            print(
                "\nQueue is currently empty."
            )

            return

        print(
            "\n========== PERSON SERVED ==========\n"
        )

        print(
            f"Name: "
            f"{person['Name']}"
        )

        print(
            f"Service Duration: "
            f"{person['Service Duration']} minutes"
        )

        print(
            "\nQueue has been updated."
        )

    # ----------------------------------
    # Queue Summary
    # ----------------------------------
    def queue_summary(self):

        self.queue_system.queue_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print(
                "                  QUEUESMART"
            )
            print("=" * 60)

            print("1. Add Person to Queue")
            print("2. View Smart Queue")
            print("3. View Next Person")
            print("4. Serve Next Person")
            print("5. View Queue Summary")
            print("6. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_person()

            elif choice == "2":

                self.view_queue()

            elif choice == "3":

                self.view_next_person()

            elif choice == "4":

                self.serve_next_person()

            elif choice == "5":

                self.queue_summary()

            elif choice == "6":

                print(
                    "\nThank you for using QueueSmart."
                )

                break

            else:

                print(
                    "\nInvalid choice. Please try again."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = QueueSmartStudio()

    studio.menu()
