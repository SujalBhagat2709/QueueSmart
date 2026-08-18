"""
QueueSmart
----------
File : queue_smart.py

Purpose
-------
Manages a service queue and helps determine:

- Who should be served next
- Estimated waiting time
- Priority order
- Appointment-based priority
- Urgency-based priority

The system dynamically sorts the queue whenever
a new person is added.

Priority Factors
----------------
1. Urgency
2. Appointment Status
3. Arrival Order

Features
--------
✔ Add Person to Queue
✔ Set Service Duration
✔ Set Appointment Status
✔ Set Urgency Level
✔ Automatically Calculate Priority
✔ Estimate Waiting Time
✔ Display Smart Queue
✔ Serve Next Person
"""


class QueueSmart:

    def __init__(self):

        self.queue = []

        self.total_served = 0

    # ----------------------------------
    # Calculate Priority Score
    # ----------------------------------
    def calculate_priority(self,
                           urgency,
                           has_appointment,
                           arrival_number):

        score = 0

        urgency = urgency.lower()

        # Urgency score
        if urgency == "critical":

            score += 100

        elif urgency == "high":

            score += 70

        elif urgency == "medium":

            score += 40

        elif urgency == "low":

            score += 10

        # Appointment priority
        if has_appointment:

            score += 20

        # Earlier arrival gets
        # a small advantage
        score += max(
            0,
            10 - arrival_number
        )

        return score

    # ----------------------------------
    # Add Person
    # ----------------------------------
    def add_person(self,
                   person_id,
                   name,
                   service_duration,
                   urgency,
                   has_appointment=False):

        arrival_number = len(
            self.queue
        ) + self.total_served + 1

        priority_score = self.calculate_priority(

            urgency,

            has_appointment,

            arrival_number

        )

        person = {

            "ID":
                person_id,

            "Name":
                name,

            "Service Duration":
                service_duration,

            "Urgency":
                urgency.lower(),

            "Appointment":
                has_appointment,

            "Arrival Number":
                arrival_number,

            "Priority Score":
                priority_score

        }

        self.queue.append(
            person
        )

        self.sort_queue()

        return person

    # ----------------------------------
    # Sort Queue
    # ----------------------------------
    def sort_queue(self):

        self.queue.sort(

            key=lambda person: (

                -person["Priority Score"],

                person["Arrival Number"]

            )

        )

    # ----------------------------------
    # Estimate Waiting Times
    # ----------------------------------
    def estimate_waiting_times(self):

        waiting_time = 0

        for person in self.queue:

            person["Estimated Wait"] = (
                waiting_time
            )

            waiting_time += person[
                "Service Duration"
            ]

    # ----------------------------------
    # Get Next Person
    # ----------------------------------
    def next_person(self):

        if not self.queue:

            return None

        self.estimate_waiting_times()

        return self.queue[0]

    # ----------------------------------
    # Serve Next Person
    # ----------------------------------
    def serve_next(self):

        if not self.queue:

            return None

        self.estimate_waiting_times()

        person = self.queue.pop(0)

        self.total_served += 1

        return person

    # ----------------------------------
    # Display Queue
    # ----------------------------------
    def display_queue(self):

        if not self.queue:

            print(
                "\nQueue is currently empty."
            )

            return

        self.estimate_waiting_times()

        print(
            "\n========== SMART QUEUE ==========\n"
        )

        for position, person in enumerate(

                self.queue,

                start=1):

            appointment = (

                "Yes"

                if person["Appointment"]

                else "No"

            )

            print(
                f"{position}. "
                f"{person['Name']}"
            )

            print(
                f"   ID: "
                f"{person['ID']}"
            )

            print(
                f"   Urgency: "
                f"{person['Urgency'].title()}"
            )

            print(
                f"   Appointment: "
                f"{appointment}"
            )

            print(
                f"   Service Time: "
                f"{person['Service Duration']} minutes"
            )

            print(
                f"   Estimated Wait: "
                f"{person['Estimated Wait']} minutes"
            )

            print(
                f"   Priority Score: "
                f"{person['Priority Score']}"
            )

            print()

    # ----------------------------------
    # Queue Summary
    # ----------------------------------
    def queue_summary(self):

        total_people = len(
            self.queue
        )

        total_waiting_time = sum(

            person["Service Duration"]

            for person in self.queue

        )

        print(
            "\n========== QUEUE SUMMARY ==========\n"
        )

        print(
            f"People Waiting : "
            f"{total_people}"
        )

        print(
            f"Total Queue Time: "
            f"{total_waiting_time} minutes"
        )

        print(
            f"People Served: "
            f"{self.total_served}"
        )


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    queue_system = QueueSmart()

    queue_system.add_person(

        "P001",

        "Rahul",

        15,

        "low",

        False

    )

    queue_system.add_person(

        "P002",

        "Priya",

        10,

        "high",

        True

    )

    queue_system.add_person(

        "P003",

        "Amit",

        20,

        "medium",

        False

    )

    queue_system.add_person(

        "P004",

        "Sneha",

        5,

        "critical",

        False

    )

    queue_system.display_queue()

    print(
        "========== NEXT PERSON =========="
    )

    next_person = queue_system.next_person()

    if next_person:

        print(
            f"\nServe Next: "
            f"{next_person['Name']}"
        )

    served_person = queue_system.serve_next()

    if served_person:

        print(
            f"\nServed: "
            f"{served_person['Name']}"
        )

    queue_system.queue_summary()
