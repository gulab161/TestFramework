# -------------------------------------------------------------
# File Name   : sample_tests.py
# Description : Contains all predefined test cases used by the
#               Test Automation Framework.
# -------------------------------------------------------------

from framework.test_case import TestCase


def get_test_cases():
    """
    Returns a list of all predefined test cases.
    """

    return [

        TestCase(
            "TC001",
            "Print Hello World",
            "Print Hello World",
            'python -c "print(\'Hello World\')"',
            "Hello World"
        ),

        TestCase(
            "TC002",
            "Display Python Version",
            "Display Python Version",
            "python --version",
            "Python"
        ),

        TestCase(
            "TC003",
            "Display Current Directory",
            "Display Current Directory",
            "cd",
            ""
        ),

        TestCase(
            "TC004",
            "List Files",
            "List Files",
            "dir",
            ""
        ),

        TestCase(
            "TC005",
            "Display Current Date",
            "Display Current Date",
            "date /T",
            ""
        ),

        TestCase(
            "TC006",
            "Display Current Time",
            "Display Current Time",
            "time /T",
            ""
        ),

        TestCase(
            "TC007",
            "Display Host Name",
            "Display Host Name",
            "hostname",
            ""
        ),

        TestCase(
            "TC008",
            "Display Logged-in User",
            "Display Logged-in User",
            "whoami",
            ""
        ),

        TestCase(
            "TC009",
            "Display IP Configuration",
            "Display IP Configuration",
            "ipconfig",
            ""
        ),

        TestCase(
            "TC010",
            "Print Custom Message",
            "Print Custom Message",
            "echo Test Automation Framework Running",
            "Test Automation Framework Running"
        )
    ]
