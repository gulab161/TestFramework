# -------------------------------------------------------------
# File Name   : executor.py
# Description : Executes test case commands using subprocess,
#               captures output, error, exit code, and updates
#               test case status (PASS/FAIL).
# -------------------------------------------------------------

import subprocess
import time


class Executor:

    def __init__(self, logger):
        """
        Initializes executor with logger instance.
        """
        self.logger = logger

    def execute_test(self, test_case):
        """
        Executes a single test case and updates its result.

        Args:
            test_case (TestCase): Test case object

        Returns:
            TestCase: Updated test case object
        """

        self.logger.info(f"Starting Test {test_case.test_id}")
        self.logger.info(f"Command: {test_case.command}")

        start_time = time.time()

        try:
            # Execute command using subprocess
            process = subprocess.run(
                test_case.command,
                shell=True,
                capture_output=True,
                text=True
            )

            # Store results
            test_case.output = process.stdout.strip()
            test_case.error = process.stderr.strip()
            test_case.exit_code = process.returncode

            # Decide PASS / FAIL
            if process.returncode == 0:
                test_case.status = "PASS"
            else:
                test_case.status = "FAIL"

            end_time = time.time()
            test_case.execution_time = round(end_time - start_time, 3)

            self.logger.info(f"Result: {test_case.status}")
            self.logger.info(f"Output: {test_case.output}")

        except Exception as e:
            test_case.status = "FAIL"
            test_case.error = str(e)
            test_case.exit_code = -1

            self.logger.error(f"Exception occurred in {test_case.test_id}")
            self.logger.error(str(e))

        self.logger.info(f"Completed Test {test_case.test_id}")

        return test_case
