# -------------------------------------------------------------
# File Name   : test_case.py
# Description : Defines the TestCase class used to store all
#               information related to a test case such as
#               test ID, name, command, expected result, and
#               execution status.
# -------------------------------------------------------------

class TestCase:
    """
    Represents a single test case in the automation framework.
    """

    def __init__(self, test_id, test_name, description,
                 command, expected_result):

        self.test_id = test_id
        self.test_name = test_name
        self.description = description
        self.command = command
        self.expected_result = expected_result

        # Execution result fields (updated after execution)
        self.status = "NOT RUN"
        self.output = ""
        self.error = ""
        self.exit_code = -1
