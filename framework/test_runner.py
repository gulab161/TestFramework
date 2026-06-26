# -------------------------------------------------------------
# File Name   : test_runner.py
# Description : Controls test execution flow. Supports running
#               single, multiple, or all test cases and
#               integrates executor and reporter modules.
# -------------------------------------------------------------

from framework.executor import Executor
from framework.reporter import Reporter


class TestRunner:

    def __init__(self, logger, test_cases):
        """
        Initializes TestRunner with logger and test cases.
        """
        self.logger = logger
        self.test_cases = test_cases

        self.executor = Executor(logger)
        self.reporter = Reporter()

        self.last_report = ""

    def list_test_cases(self):
        """
        Displays all available test cases.
        """
        print("\nAvailable Test Cases:")
        print("-" * 60)

        for tc in self.test_cases:
            print(f"{tc.test_id} | {tc.test_name} | {tc.description}")

        print("-" * 60)

    def run_test_by_id(self, test_id):
        """
        Runs a single test case by ID.
        """
        for tc in self.test_cases:
            if tc.test_id == test_id:
                return self.executor.execute_test(tc)

        self.logger.error(f"Test case not found: {test_id}")
        return None

    def run_multiple_tests(self, test_ids):
        """
        Runs multiple selected test cases.
        """
        results = []

        for tid in test_ids:
            tc = self.run_test_by_id(tid.strip())

            if tc:
                results.append(tc)

        self.last_report = self.reporter.generate_report(results)
        return results

    def run_all_tests(self):
        """
        Runs all available test cases.
        """
        results = []

        for tc in self.test_cases:
            updated_tc = self.executor.execute_test(tc)
            results.append(updated_tc)

        self.last_report = self.reporter.generate_report(results)
        return results

    def get_last_report(self):
        """
        Returns last generated report.
        """
        return self.last_report
