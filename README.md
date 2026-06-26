# TestFramework
Develop a command-line based Python Test Automation Framework that allows users to manage and execute test cases. The framework should support executing individual tests, multiple selected tests, or all available tests, while recording execution details in log files and generating a summary report.

# Python Test Automation Framework

## Project Overview

This project is a command-line based Python Test Automation Framework that executes predefined test cases, manages execution, generates reports, and maintains logs.

It demonstrates:
- Object-Oriented Programming
- Modular Programming
- Exception Handling
- Subprocess Execution
- Logging

---

## Project Structure

TestFramework/
│── main.py
│── framework/
│   ├── executor.py
│   ├── logger.py
│   ├── reporter.py
│   ├── test_case.py
│   ├── test_runner.py
│   └── utils.py
│── tests/
│   └── sample_tests.py
│── logs/
│   └── framework.log
│── reports/
│   └── summary_report.txt

---

## How to Run

```bash
python main.py
