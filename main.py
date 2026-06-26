# -------------------------------------------------------------
# File Name   : main.py
# Description : Entry point of the Python Test Automation
#               Framework. Provides menu-driven interface
#               to execute test cases and view reports.
# -------------------------------------------------------------

from framework.logger import Logger
from framework.test_runner import TestRunner
from tests.sample_tests import get_test_cases


def main():

    # Initialize logger
    logger = Logger()
    logger.info("Framework Started")

    # Load test cases
    test_cases = get_test_cases()

    # Initialize test runner
    runner = TestRunner(logger, test_cases)

    while True:

        print("\n====================================")
        print("Python Test Automation Framework")
        print("====================================")
        print("1. List All Test Cases")
        print("2. Run Test by ID")
        print("3. Run Multiple Tests")
        print("4. Run All Tests")
        print("5. View Last Report")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        # 1. List all test cases
        if choice == "1":
            runner.list_test_cases()

        # 2. Run single test
        elif choice == "2":
            test_id = input("Enter Test ID: ")
            runner.run_test_by_id(test_id)

        # 3. Run multiple tests
        elif choice == "3":
            ids = input("Enter Test IDs (comma separated): ")
            test_list = ids.split(",")
            runner.run_multiple_tests(test_list)

        # 4. Run all tests
        elif choice == "4":
            runner.run_all_tests()

        # 5. View last report
        elif choice == "5":
            report = runner.get_last_report()
            if report:
                print("\n" + report)
            else:
                print("\nNo report available. Run tests first.")

        # 6. Exit
        elif choice == "6":
            logger.info("Framework Shutdown")
            print("Exiting Framework...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
