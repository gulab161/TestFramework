# -------------------------------------------------------------
# File Name   : reporter.py
# Description : Generates execution summary report after all
#               test cases are executed. Saves report inside
#               reports/summary_report.txt
# -------------------------------------------------------------

import os


class Reporter:

    def __init__(self):
        """
        Initializes reporter and ensures reports directory exists.
        """
        if not os.path.exists("reports"):
            os.makedirs("reports")

        self.report_file = "reports/summary_report.txt"

    def generate_report(self, test_cases):
        """
        Generates summary report from executed test cases.

        Args:
            test_cases (list): List of executed TestCase objects
        """

        total = len(test_cases)
        passed = 0
        failed = 0

        report_lines = []

        report_lines.append("=" * 40)
        report_lines.append("Execution Summary")
        report_lines.append("=" * 40)
        report_lines.append("")

        # Process each test case
        for tc in test_cases:

            if tc.status == "PASS":
                passed += 1
            else:
                failed += 1

            report_lines.append(f"Test ID   : {tc.test_id}")
            report_lines.append(f"Test Name : {tc.test_name}")
            report_lines.append(f"Command   : {tc.command}")
            report_lines.append(f"Status    : {tc.status}")
            report_lines.append(f"Output    : {tc.output}")
            report_lines.append("-" * 40)

        # Calculate percentage
        pass_percentage = (passed / total) * 100 if total > 0 else 0

        report_lines.append("")
        report_lines.append("=" * 40)
        report_lines.append("Final Summary")
        report_lines.append("=" * 40)
        report_lines.append(f"Total Tests : {total}")
        report_lines.append(f"Passed      : {passed}")
        report_lines.append(f"Failed      : {failed}")
        report_lines.append(f"Pass %      : {round(pass_percentage, 2)}%")
        report_lines.append("=" * 40)

        # Write to file
        with open(self.report_file, "w") as file:
            file.write("\n".join(report_lines))

        return "\n".join(report_lines)
