# Smart CLI Calculator

A production-style command-line calculator built in Python to strengthen core software engineering fundamentals such as clean architecture, input validation, state management, exception handling, and modular programming.

This project is intentionally designed without external libraries or AI-generated code to build real engineering intuition from first principles.

---

# Objective

The goal of this project is not just to create a calculator, but to develop the ability to:

* Think computationally
* Structure programs cleanly
* Handle edge cases properly
* Write reusable logic
* Design maintainable terminal applications
* Practice engineering-oriented coding habits

This challenge is part of a long-term journey from:

> “I can code”

to

> “I can engineer systems.”

---

# Features

## Supported Operations

* Addition
* Subtraction
* Multiplication
* Division
* Power
* Modulo

---

# Engineering Features

## Input Validation

Prevents invalid numerical inputs.

Example:

```bash
Enter first number: abc
Invalid number. Please enter a valid numeric value.
```

---

## Divide-by-Zero Protection

Gracefully handles division errors without crashing the application.

Example:

```bash
Cannot divide by zero.
```

---

## Persistent Program Loop

Runs continuously until the user chooses to exit.

---

## History Tracking

Stores calculation history during runtime.

Example:

```bash
1. 5 + 7 = 12
2. 9 / 3 = 3
```

---

## File Persistence

Exports history into:

```bash
history.txt
```

---

# Tech Stack

* Python 3
* Pure standard library only

No external libraries used.

---

# Project Structure

```bash
smart-cli-calculator/
│
├── calculator.py
├── history.txt
├── README.md
```

---

# Concepts Practiced

This project focuses heavily on engineering fundamentals:

* Functions
* Loops
* Dictionaries
* Conditional Logic
* Exception Handling
* File Handling
* State Management
* Code Reusability
* Program Flow Design
* Input Validation
* Modular Thinking

---

# Core Engineering Principles Followed

## 1. Clean Architecture

The application logic is separated into reusable functions instead of large repetitive condition blocks.

---

## 2. DRY Principle

Avoided unnecessary repeated code.

(Don’t Repeat Yourself)

---

## 3. Fault Tolerance

The program handles:

* invalid inputs
* mathematical errors
* unexpected user behavior

without crashing.

---

## 4. Scalability Mindset

The calculator is designed in a way that allows future expansion such as:

* scientific calculations
* expression parsing
* GUI integration
* API integration
* logging systems

---

# Example Usage

```bash
Enter operation: add
Enter first number: 5
Enter second number: 7

Result: 12
```

---

# Future Improvements

Potential upgrades planned for future versions:

* Scientific calculator support
* Expression evaluator
* GUI version
* Unit conversion system
* Logging system
* Database-based history storage
* REST API version
* Dockerized deployment

---

# Learning Outcome

This project helped strengthen understanding of:

* how terminal applications work
* organizing logic properly
* designing reusable code
* debugging runtime issues
* handling user interaction
* building software from first principles

---

# Engineering Reflection Questions

Before building this project, the following engineering questions were considered:

* How should operations be organized cleanly?
* How can repetitive code be avoided?
* How should program state/history be stored?
* How should invalid user input be handled?
* How can the program run continuously without failure?

---

# Why This Project Matters

Small projects like this build the foundation required for advanced systems such as:

* ETL pipelines
* Backend services
* AI systems
* Distributed systems
* Real-time applications
* Networking tools
* Databases
* ML infrastructure

Every advanced engineer starts by mastering simple systems deeply.

---

# Next Engineering Challenges

Upcoming progression after this project:

* Password Manager
* Log Parser
* File Organizer
* Multi-threaded Downloader
* TCP Chat Application
* Custom HTTP Server
* ETL Pipeline
* Mini Redis Clone
* Vector Database
* Recommendation Engine
* Distributed Worker Queue
* Mini Transformer Model

---

# Author

Mahansh Gaur

Aspiring Data + AI/ML Engineer focused on:

* backend systems
* AI infrastructure
* ETL pipelines
* robotics
* distributed systems
* real-world engineering

GitHub: github.com/mahanshstarktech
