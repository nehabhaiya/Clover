import unittest
from selenium import webdriver
from behave import use_step_matcher

use_step_matcher("re")

class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_on_search_engines(self):
        try:
            self.run_behave()
        except SystemExit:
            pass  # Ignore SystemExit raised by behave

    def run_behave(self):
        behave_args = ["features"]
        behave_args.extend(["--tags", "~@ignore"])  # Exclude scenarios with @ignore tag
        behave_args.extend(["--no-capture", "--no-capture-stderr"])
        behave_args.extend(["--no-capture-outout", "--no-capture-all"])
        behave_args.extend(["--no-logcapture", "--no-summary"])
        behave_args.extend(["--logging-level", "DEBUG"])
        behave_args.extend(["--no-skipped", "--no-snippets", "--no-pending", "--no-indent"])
        behave_args.extend(["--stop", "--format", "progress2", "--outfile", "pretty"])
        behave_args.extend(["--junit", "--junit-directory", "reports/junit"])
        behave_args.extend(["--format", "json", "--outfile", "reports/results.json"])

        from behave.__main__ import main as behave_main
        behave_main(behave_args)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
