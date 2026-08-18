# QueueSmart

## Overview

QueueSmart is a smart queue management system that organizes people based on multiple factors instead of using a simple first-come, first-served approach.

The system considers:

- Urgency level
- Appointment status
- Arrival order
- Expected service duration

It automatically calculates a priority score, dynamically organizes the queue, and estimates waiting times.

## Features

- Add Person to Queue
- Urgency-Based Priority
- Appointment-Based Priority
- Arrival Order Consideration
- Dynamic Queue Sorting
- Priority Score Calculation
- Estimated Waiting Time
- Next Person Recommendation
- Serve Next Person
- Queue Summary

## Project Structure

queue-smart/

├── queue_smart.py
├── queue_smart_studio.py
├── README.md
└── .gitignore

## Requirements

- Python 3.x
- No external libraries required

## Run

```bash
python queue_smart_studio.py
